import random
import logging

from typing import List, Dict
from helper_functions import count_to_proportions, get_lists_difference, get_containers_counts_sum_map


class ProportionsControllingGA:
    def __init__(self,
                 chromosome_length: int,
                 containers_count_map: Dict[int, Dict[str, float]],
                 optimal_proportions: Dict[str, float],
                 labels_penalties: Dict[str, float],
                 selection_threshold: float = 1.0,
                 solution_threshold: float = 0.1,
                 crossover_probability: float = 0.9,
                 mutation_probability: float = 0.1,
                 number_of_mutations_per_occurrence: int = 1,
                 number_of_genes_per_mutation: int = 1,
                 population_size: int = 100,
                 max_iterations: int = 100,
                 random_seed: int = 42):
        """
        Constructor
        :param chromosome_length: the length of the chromosome (number of containers to be selected)
        :param containers_count_map: a map of (containers) and their count for each class (label)
        :param optimal_proportions: the optimal portions for each class (label)
        :param labels_penalties: the portions penalties
        :param selection_threshold: the selection threshold; the proportion of the population that will be selected in
         the selection phase. When set to 1.0, the selection phase will select all chromosomes
        :param solution_threshold: the solution threshold; the threshold for the solution to be considered as a
            solution. When set to 0.0, the solution will be considered as a solution only when the optimal proportions are
            reached. Otherwise, the solution will be considered as a solution when the difference between the optimal
            proportions and the actual proportions is less than the solution threshold.
        :param crossover_probability: the crossover probability
        :param mutation_probability: the mutation probability
        :param number_of_mutations_per_occurrence: the number of mutations to perform per one mutation operation
        :param number_of_genes_per_mutation: the number of genes to be mutated for each chromosome
        :param population_size: the population size
        :param max_iterations: the maximum number of iterations
        """

        # set the input parameters
        self.__chromosome_length = chromosome_length
        self.__containers_count_map = containers_count_map
        self.__optimal_proportions = optimal_proportions
        self.__labels_penalties = labels_penalties
        self.__selection_threshold = selection_threshold
        self.__solution_threshold = solution_threshold
        self.__crossover_probability = crossover_probability
        self.__mutation_probability = mutation_probability
        self.__number_of_mutations_per_occurrence = number_of_mutations_per_occurrence
        self.__number_of_genes_per_mutation = number_of_genes_per_mutation
        self.__population_size = population_size
        self.__max_iterations = max_iterations
        self.__random_seed = random_seed

        # calculate extra variables
        self.__containers_ids = list(containers_count_map.keys())
        self.__labels = list(self.__optimal_proportions.keys())
        self.__total_number_of_containers = len(self.__containers_ids)

        # initialize empty variables
        self.__population = self.__generate_population()
        self.__curr_population_size = len(self.__population)
        self.__fitness_values = list()
        self.__best_chromosome = None
        self.__best_fitness_value = float('inf')

        # initialize constants
        self.__OPTIMAL_FITNESS_VALUE = 0.0

    def __update_population(self, population: List[List[int]]):
        """
        Update the population
        :param population: the population
        """
        self.__population = population
        self.__curr_population_size = len(self.__population)

    def __get_containers_counts_sum_map(self, chromosome: List[int]) -> Dict[str, float]:
        """
        Get the containers counts sum map for the given chromosome
        :param chromosome: the chromosome
        :return: the containers counts sum map
        """
        containers_sum_map = get_containers_counts_sum_map(self.__containers_count_map, chromosome)
        for label in self.__labels:
            if label not in containers_sum_map:
                containers_sum_map[label] = 0
        return containers_sum_map

    def __calculate_fitness_value(self, chromosome: List[int]) -> float:
        """
        Calculates the fitness value of the given chromosome
        :param chromosome: the chromosome
        :return: the fitness value
        """
        chromosome_containers_counts_sum_map = self.__get_containers_counts_sum_map(chromosome)
        chromosome_containers_counts_proportions_map = count_to_proportions(chromosome_containers_counts_sum_map)
        fitness_value = 0
        for label in chromosome_containers_counts_proportions_map:
            fitness_value += abs(chromosome_containers_counts_proportions_map[label] - self.__optimal_proportions[label]) \
                             * self.__labels_penalties[label]
        return fitness_value

    def __calculate_fitness_values(self, chromosomes: List[List[int]]) -> List[float]:
        """
        Calculates the fitness values of the given chromosomes
        :param chromosomes: the chromosomes
        :return: the fitness values
        """
        return [self.__calculate_fitness_value(chromosome) for chromosome in chromosomes]

    def __calculations_phase(self):
        """
        Calculates the fitness values of the population, and save the best chromosome and its fitness value
        """
        logging.debug("Calculations phase ...")
        self.__fitness_values = self.__calculate_fitness_values(self.__population)
        best_fitness_value = min(self.__fitness_values)
        if best_fitness_value < self.__best_fitness_value:
            self.__best_fitness_value = best_fitness_value
            self.__best_chromosome = self.__population[self.__fitness_values.index(self.__best_fitness_value)]
            self.__best_chromosome_counts_sum_map = self.__get_containers_counts_sum_map(self.__best_chromosome)
            self.__best_chromosome_counts_proportions_map = count_to_proportions(self.__best_chromosome_counts_sum_map)
        logging.debug(f"Best fitness value: {self.__best_fitness_value}")
        logging.debug(f"Best chromosome: {self.__best_chromosome}")
        logging.debug(f"Best chromosome counts: {self.__best_chromosome_counts_sum_map}")
        logging.debug(f"Best chromosome proportions: {self.__best_chromosome_counts_proportions_map}")
        logging.debug("Calculations phase done")

    def __do_selection(self, population: List[List[int]]) -> List[List[int]]:
        """
        Selects the chromosomes from the population according to the fitness values and the selection threshold
        :param population: the population
        :return: the selected chromosomes
        """
        if self.__selection_threshold == 1.0:
            return population
        else:
            population_w_fitness = sorted(zip(population, self.__fitness_values), key=lambda x: x[1])
            population_w_fitness = population_w_fitness[:int(len(population) * self.__selection_threshold)]
            selected_population, _ = zip(*population_w_fitness)
            return list(selected_population)

    def __selection_phase(self):
        """
        The selection phase
        """
        logging.debug("Selection phase ...")
        self.__population = self.__do_selection(self.__population)
        logging.debug("Selection phase done")

    def __do_crossover(self, parent1: List[int], parent2: List[int]) -> List[int]:
        """
        Does crossover on the given chromosomes
        :param parent1: the first parent
        :param parent2: the second parent
        :return: the offspring
        """
        crossover_point = random.randint(0, self.__chromosome_length - 1)
        offspring = parent1[:crossover_point]
        remaining_genes = [gene for gene in parent2 if gene not in offspring]
        offspring.extend(remaining_genes[:self.__chromosome_length - len(offspring)])
        return offspring

    def __crossover_phase(self):
        """
        The crossover phase
        """
        logging.debug("Crossover phase ...")
        offspring = list()
        offspring_count = 0
        population_copy = self.__population.copy()
        while offspring_count < self.__population_size:
            if random.random() < self.__crossover_probability:
                parent1 = random.choice(population_copy)
                parent2 = random.choice(population_copy)
                offspring.append(self.__do_crossover(parent1, parent2))
                offspring_count += 1
            else:
                parent1 = population_copy.pop(random.randint(0, len(population_copy) - 1))
                parent2 = population_copy.pop(random.randint(0, len(population_copy) - 1))
                offspring.append(parent1)
                offspring.append(parent2)
                offspring_count += 2
        self.__update_population(offspring)
        logging.debug("Crossover phase done")

    def __do_mutation(self, chromosome: List[int]) -> List[int]:
        """
        Mutates the given chromosome
        :param chromosome: the chromosome
        :return: the mutated chromosome
        """
        mutated_chromosome = chromosome.copy()
        mutation_points = random.sample(range(self.__chromosome_length), self.__number_of_genes_per_mutation)
        for mutation_point in mutation_points:
            possible_values = get_lists_difference(self.__containers_ids, mutated_chromosome)
            mutated_chromosome[mutation_point] = random.choice(possible_values)
        return mutated_chromosome

    def __mutation_phase(self):
        """
        The mutation phase
        """
        logging.debug("Mutation phase ...")
        if random.random() < self.__mutation_probability:
            chromosomes_to_mutate_indexes = random.sample(range(self.__curr_population_size),
                                                          self.__number_of_mutations_per_occurrence)
            for chromosome_index in chromosomes_to_mutate_indexes:
                self.__population[chromosome_index] = self.__do_mutation(self.__population[chromosome_index])
        logging.debug("Mutation phase done")

    def __generate_population(self) -> List[List[int]]:
        """
        Generates the initial population
        :return: the initial population
        """
        containers_ids_copy = self.__containers_ids.copy()
        population = list()
        i, j = 0, 0
        while j < self.__population_size:
            end_index = i + self.__chromosome_length
            if end_index > self.__total_number_of_containers:
                random.shuffle(containers_ids_copy)
                i = 0
                end_index = self.__chromosome_length
            chromosome = containers_ids_copy[i: end_index]
            population.append(chromosome)
            i += self.__chromosome_length
            j += 1
        return population

    def __check_for_solution(self) -> bool:
        """
        Checks if the optimal solution or the solution the satisfies the given threshold has been found
        :return: True if the solution is found, False otherwise
        """
        return self.__best_fitness_value <= self.__solution_threshold \
            or self.__best_fitness_value == self.__OPTIMAL_FITNESS_VALUE

    def __display_solution_logging(self):
        logging.info(f"Solution: {self.__best_chromosome}")
        logging.info(f"Fitness: {self.__best_fitness_value}")
        logging.info(f"Count sums map: {self.__best_chromosome_counts_sum_map}")
        logging.info(f"Proportions map: {self.__best_chromosome_counts_proportions_map}")

    def solve(self):
        """
        Solves the problem
        """
        # set random seed
        random.seed(self.__random_seed)
        for i in range(self.__max_iterations):
            logging.info(f"Starting Iteration: {i + 1} of {self.__max_iterations};")
            self.__calculations_phase()
            if self.__check_for_solution():
                logging.info(f"Solution found in iteration {i + 1}")
                self.__display_solution_logging()
                break
            self.__selection_phase()
            self.__crossover_phase()
            self.__mutation_phase()
        logging.info("Solving done after iterating for the given number of iterations")
        self.__display_solution_logging()

    def get_the_solution(self) -> List[int]:
        """
        Returns the best chromosome
        :return: the best chromosome
        """
        return self.__best_chromosome
