import logging
from proportions_controlling_GA import ProportionsControllingGA

# Set up logging
logging.basicConfig(level=logging.INFO)

# Example input data
containers_count_map = {
    1: {"Class1": 15, "Class2": 10, "Class3": 5},
    2: {"Class1": 8, "Class2": 20, "Class3": 12},
    3: {"Class1": 30, "Class2": 10, "Class3": 10},
    4: {"Class1": 5, "Class2": 5, "Class3": 30},
    5: {"Class1": 20, "Class2": 15, "Class3": 15},
    6: {"Class1": 10, "Class2": 25, "Class3": 5},
    7: {"Class1": 5, "Class2": 5, "Class3": 40},
    8: {"Class1": 15, "Class2": 20, "Class3": 5},
    9: {"Class1": 12, "Class2": 8, "Class3": 20},
    10: {"Class1": 8, "Class2": 22, "Class3": 10},
    11: {"Class1": 20, "Class2": 10, "Class3": 20},
    12: {"Class1": 15, "Class2": 15, "Class3": 20},
    13: {"Class1": 8, "Class2": 12, "Class3": 30},
    14: {"Class1": 10, "Class2": 20, "Class3": 10},
    15: {"Class1": 25, "Class2": 15, "Class3": 10},
    16: {"Class1": 5, "Class2": 5, "Class3": 30},
    17: {"Class1": 20, "Class2": 10, "Class3": 10},
    18: {"Class1": 15, "Class2": 5, "Class3": 20},
    19: {"Class1": 10, "Class2": 25, "Class3": 5},
    20: {"Class1": 8, "Class2": 22, "Class3": 10},
    21: {"Class1": 5, "Class2": 5, "Class3": 40},
    22: {"Class1": 15, "Class2": 20, "Class3": 5},
    23: {"Class1": 30, "Class2": 10, "Class3": 10},
    24: {"Class1": 20, "Class2": 15, "Class3": 15},
    25: {"Class1": 8, "Class2": 20, "Class3": 12},
    26: {"Class1": 10, "Class2": 25, "Class3": 5},
    27: {"Class1": 15, "Class2": 10, "Class3": 5},
    28: {"Class1": 8, "Class2": 22, "Class3": 10},
    29: {"Class1": 20, "Class2": 10, "Class3": 20},
    30: {"Class1": 15, "Class2": 15, "Class3": 20},
    31: {"Class1": 8, "Class2": 12, "Class3": 30},
    32: {"Class1": 10, "Class2": 20, "Class3": 10},
    33: {"Class1": 25, "Class2": 15, "Class3": 10}
}

optimal_proportions = {"Class1": 0.4, "Class2": 0.3, "Class3": 0.3}
labels_penalties = {"Class1": 1, "Class2": 1, "Class3": 1}

num_containers_to_select = 10

# Initialize the algorithm
ga = ProportionsControllingGA(
    chromosome_length=num_containers_to_select,
    containers_count_map=containers_count_map,
    optimal_proportions=optimal_proportions,
    labels_penalties=labels_penalties,
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

# Solve the problem
ga.solve()

# Get the solution
solution = ga.get_the_solution()
print(f"Solution: {solution}")
