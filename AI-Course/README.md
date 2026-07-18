
# Artificial Intelligence Course

This directory contains instructional notebooks covering classical artificial intelligence, search algorithms, numerical optimization, probabilistic classification, decision trees, and neural-network fundamentals.

The materials are intended for classroom demonstrations, laboratory exercises, and independent practice.

## Learning Objectives

After completing these notebooks, students should be able to:

- explain state-space search and search-tree exploration;
- distinguish uninformed and informed search strategies;
- implement breadth-first, depth-first, uniform-cost, and heuristic search;
- explain the role of path cost and heuristic functions;
- apply alpha-beta pruning to game-tree search;
- use numerical optimization techniques;
- explain the bisection and BFGS optimization methods;
- construct and interpret decision trees;
- apply Naive Bayes classification;
- explain the basic components of a neural network;
- implement a simple neural network from first principles.

## Notebook Topics

### Search Algorithms

| Notebook | Topic |
|---|---|
| `Binary_Search.ipynb` | Binary search and ordered search spaces |
| `Breadth_First_Search.ipynb` | Introductory breadth-first search on a directed graph |
| `Breadth_First_Search_Examples.ipynb` | Additional breadth-first search examples using different graph structures |
| `Breadth_First_Search_Exercises.ipynb` | Guided breadth-first search exercises |
| `Depth_First_Search.ipynb` | Depth-first search |
| `Uniform_Cost_Search.ipynb` | Uniform-cost search |
| `A_Star_Search.ipynb` | A* search on a weighted graph using heuristic estimates |
| `A_Star_Search_Extended_Graph.ipynb` | Extended A* search example using a larger weighted graph |

### Game-Tree Search

| Notebook | Topic |
|---|---|
| `Alpha_Beta_Pruning.ipynb` | Alpha-beta pruning and reducing minimax search |

### Numerical Methods and Optimization

| Notebook | Topic |
|---|---|
| `Bisection_Method.ipynb` | Root finding using the bisection method |
| `BFGS.ipynb` | Quasi-Newton optimization using BFGS |

### Classification and Decision Trees

| Notebook | Topic |
|---|---|
| `Naive_Bayes_Classifiers.ipynb` | Probabilistic classification using Naive Bayes |
| `DecisionTree1.ipynb` | Decision-tree fundamentals |
| `DecisionTree2.ipynb` | Additional decision-tree implementation |
| `DecisionTree3.ipynb` | Extended decision-tree example |

### Neural Networks

| Notebook | Topic |
|---|---|
| `NeuralNetwork.ipynb` | Neural-network concepts and implementation |
| `Neural_Network_from_Scratch.ipynb` | Building a neural network from first principles |

## Suggested Study Sequence

A suitable progression is:

1. `Binary_Search.ipynb`
2. `Breadth_First_Search.ipynb`
3. `Breadth_First_Search_Examples.ipynb`
4. `Breadth_First_Search_Exercises.ipynb`
5. `Depth_First_Search.ipynb`
6. `Uniform_Cost_Search.ipynb`
7. `A_Star_Search.ipynb`
8. `A_Star_Search_Extended_Graph.ipynb`
9. `Alpha_Beta_Pruning.ipynb`
10. `Bisection_Method.ipynb`
11. `BFGS.ipynb`
12. `Naive_Bayes_Classifiers.ipynb`
13. `DecisionTree1.ipynb`
14. `NeuralNetwork.ipynb`
15. `Neural_Network_from_Scratch.ipynb`

The additional notebooks and exercise files may be used for reinforcement after the corresponding introductory lesson.

## Requirements

The notebooks primarily use:

```text
numpy
pandas
matplotlib
scipy
scikit-learn
