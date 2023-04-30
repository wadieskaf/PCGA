Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

# Table of Contents

<!-- TOC -->
* [Table of Contents](#table-of-contents)
* [Proportions Controlling Genetic Algorithm (PCGA)](#proportions-controlling-genetic-algorithm-pcga)
  * [Problem Description](#problem-description)
  * [Algorithm Overview](#algorithm-overview)
  * [Class Description](#class-description)
    * [Main Methods](#main-methods)
    * [Helper Methods](#helper-methods)
  * [Usage](#usage)
    * [Example](#example)
  * [Future Enhancements](#future-enhancements)
  * [Contributing](#contributing)
  * [License](#license)
<!-- TOC -->

# Proportions Controlling Genetic Algorithm (PCGA)
This repository contains an implementation of a general purpose Genetic Algorithm (GA) to control the proportions of labels in a set of containers. The goal of this algorithm is to select a subset of containers to match the desired proportions while minimizing any potential biases.

A container in this context refers to a group of similar items that can be processed together. Examples of containers include a set of sentences that form a document, a set of images that form an album, a set of tweets that form a thread, etc.

The algorithm is designed to select a specified number of containers from a larger set, ensuring that the resulting proportions of labels in the selected containers are as close as possible to the desired proportions.

## Problem Description
The input data consists of:

1. A set of containers, where each container is represented by a unique ID and a count map of labels.
2. The desired proportions for each label.
3. Penalties associated with deviating from the desired proportions for each label.

The output is a list of container IDs that make up the selected set of containers.

## Algorithm Overview
The Proportions Controlling Genetic Algorithm (PCGA) is implemented in the `ProportionsControllingGA` class. The main steps of the algorithm are:

1. Initialization: Generate an initial population of chromosomes, where each chromosome represents a potential solution (i.e., a list of container IDs).
2. Fitness Evaluation: Calculate the fitness of each chromosome based on how closely its label proportions match the optimal proportions.
3. Selection: Select a subset of chromosomes based on their fitness values.
4. Crossover: Generate new offspring chromosomes by combining genes from parent chromosomes.
5. Mutation: Randomly change some genes in a subset of chromosomes.
6. Termination: Check if the optimal solution or a solution within a specified threshold has been found. If not, repeat steps 2-5 for a maximum number of iterations.
Algorithm Flowchart

## Class Description
The ProportionsControllingGA class has several methods that implement the main steps of the algorithm, as well as helper methods for working with chromosomes.

### Main Methods

* `__init__(...)`: Initializes the class with input parameters and generates the initial population.
* `solve()`: Runs the Genetic Algorithm to find the optimal solution or a solution within a specified threshold.
* `get_the_solution()`: Returns the best chromosome (solution) found by the algorithm.

### Helper Methods
These methods perform various tasks related to working with chromosomes, such as fitness calculation, selection, crossover, mutation, and checking for a solution.

## Usage
To use the `ProportionsControllingGA` class, follow these steps:

1. Import the class: `from proportions_controlling_ga import ProportionsControllingGA`
2. Create an instance of the class, passing the required input parameters: `ga = ProportionsControllingGA(...)`
3. Run the algorithm: `ga.solve()`
4. Get the solution: solution = `ga.get_the_solution()`
### Example
Please refer to the `example.py` file for an example of how to use the ProportionsControllingGA class.

## Use Cases Examples

The implementation of the Proportions Controlling Genetic Algorithm can be useful in several use cases, such as:

* Annotation bias reduction in machine learning: The algorithm can be used to control the proportions of labels in a set of containers before annotating them, ensuring that annotators are not biased towards a particular class when the majority of the labels are of that class.
* Balancing datasets for machine learning: By controlling the proportions of labels in a dataset, the algorithm can help balance the distribution of the classes, which can lead to improved performance of machine learning models trained on the data.
* Selecting a representative subset of data: The algorithm can be used to select a subset of containers that best represents the distribution of labels in a larger set, without having to annotate all the containers.
* Optimizing the use of resources: The algorithm can help optimize the use of resources by selecting only the most important containers to be processed, while still maintaining the desired proportions of labels.

## Future Enhancements
1. Implement additional selection, crossover, and mutation strategies to improve the algorithm's performance.
2. Integrate parallel processing techniques to speed up the algorithm.
3. Develop a user-friendly command-line interface or graphical user.
4. Better coding for the algorithm, such as using more structured classes and subclasses for Chormosome, Population, etc.
5. Implementing the algorithm in a faster language, such as Rust. (My personal future plan).

## Contributing
Contributions to this project are welcome. Feel free to implement any of the future enhancements listed above or suggest your own. 
In addition, If you have an idea for an improvement or find a bug, please create a new issue. If you'd like to contribute code, please fork the repository and submit a pull request with your changes.

## License
Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
