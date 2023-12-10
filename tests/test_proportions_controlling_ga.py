# /tests/test_proportions_controlling_ga.py
import pytest
from proportions_controlling_GA import ProportionsControllingGA

def test_pcga_initialization():
    ga = ProportionsControllingGA(
        chromosome_length=10,
        containers_count_map={1: {"Class1": 15, "Class2": 10}},
        optimal_proportions={"Class1": 0.4, "Class2": 0.6},
        labels_penalties={"Class1": 1, "Class2": 1},
        selection_threshold=1.0,
        solution_threshold=0.1,
        crossover_probability=0.9,
        mutation_probability=0.1,
        number_of_mutations_per_occurrence=1,
        number_of_genes_per_mutation=1,
        population_size=100,
        max_iterations=100,
        random_seed=42
    )
    assert ga is not None
    # More assertions can be added to check the correct initialization of attributes


def test_calculate_fitness_value():
    # Example initialization parameters
    chromosome_length = 10
    containers_count_map = {
        1: {"Class1": 15, "Class2": 10},
        2: {"Class1": 8, "Class2": 20},

        # ...
    }
    optimal_proportions = {"Class1": 0.4, "Class2": 0.6}
    labels_penalties = {"Class1": 1, "Class2": 1}
    
    ga = ProportionsControllingGA(
        chromosome_length=chromosome_length,
        containers_count_map=containers_count_map,
        optimal_proportions=optimal_proportions,
        labels_penalties=labels_penalties,
    )
    
    # Example chromosome for testing
    # Make sure all elements in this list exist in containers_count_map
    chromosome = [1, 2]  # Adjust this according to your data structure
    fitness_value = ga._ProportionsControllingGA__calculate_fitness_value(chromosome)
    assert isinstance(fitness_value, float)
    # Add more assertions here if necessary


