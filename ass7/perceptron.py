#!/home/mormonjz/Anaconda3/bin/python python3
# -*- coding: utf-8 -*-
"""
Perceptron class represents a simplified neuron that categorizes inputs based
on x and y values.

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""
from matplotlib import pyplot as plot
from numpy import zeros, array, dot, ndarray


class Perceptron:
    """Perceptron emulator, works fine, though I forgot to introduce a bias.

    Single perceptron used to categorize two dimensional inputs. I forgot to
    add a bias input in it, this might be why I get bad results on test sample.
    """
    def __init__(self, alpha: float = 0.2):
        """Initialize perceptron with provided learning rate.

        Keyword Arguments:
            alpha (float, default: 0.2): Learning factor for perceptron.
        """
        self._average_training_error = list()
        self._average_test_error = list()
        self._weights = zeros(3)
        self._alpha = alpha

    def train_and_test(self, x_train: ndarray, y_train: ndarray,
                       x_test: ndarray, y_test: ndarray, epoch: int = 100):
        """Train and test perceptron on given data sets and plot errors.

        Takes in provided data sets and trains them for a given number of
        epochs. Uses _train, _test and _plot_errors functions.

        Arguments:
            x_train (ndarray): input values for training set.
            y_train (ndarray): output values for training set.
            x_test (ndarray): input values for testing set.
            y_test (ndarray): output values for testing set.

        Keyword Arguments:
            epoch (int, default: 100): number of epochs to run training on.
        """
        # Run training and testing methods for a specified number of epochs
        for _ in range(epoch):
            self._train(x_train, y_train)
            self._test(x_test, y_test)

        # Plot results of training and testing
        self._plot_errors()

    def _train(self, inputs: ndarray, outputs: ndarray):
        """Train perceptron on given data sets, updates weights.

        Arguments:
            inputs (ndarray): input values for training set.
            outputs (ndarray): output values for training set.
        """
        for x, y in zip(inputs, outputs):
            # Get estimate from f function (activation function)
            estimate = self._f_func(x)
            # Get error (difference between estimate and actual value)
            error = estimate - y
            # Update weights

            self._weights -= self._alpha * error * array([x[0], x[1], 1.5])

        # Add average error to list
        self._average_training_error.append(self._get_average_error(inputs,
                                                                    outputs))
        # Print out last added item
        print(f'Average training error: {self._average_training_error[-1]}')

    def _test(self, inputs: ndarray, outputs: ndarray):
        """Test perceptron's accuracy using test data sets.

        Arguments:
            inputs (ndarray): input values for testing set.
            outputs (ndarray): output values for testing set.
        """
        # Add average error to list
        self._average_test_error.append(self._get_average_error(inputs,
                                                                outputs))
        # Print out last added item
        print(f'Average testing error:  {self._average_test_error[-1]}')

    def _f_func(self, x: float) -> int:
        """Cutoff function for perceptron, 1 if x is over 0, 0 otherwise.

        Arguments:
            x (float): x value for input

        Returns:
            (int): 1 if x is over 0, 0 otherwise.
        """
        return 1 if (dot(x, self._weights[0:2]) + self._weights[2]) > 0 else 0

    def _get_average_error(self, inputs: ndarray, outputs: ndarray) -> float:
        """Returns average error for perceptron.

        Arguments:
            inputs (ndarray): input values for testing set.
            outputs (ndarray): output values for testing set.

        Returns:
            (float): Average error for perceptron.
        """
        # Sum up the error
        error = 0
        for x, y in zip(inputs, outputs):
            estimate = self._f_func(x)
            error += estimate - y

        # Return average
        return error / len(inputs)

    def _plot_errors(self):
        """Plot average errors for each epoch on both training and testing set.
        """
        print("Average training error graph:")
        plot.plot(self._average_training_error)
        plot.show()

        print("Average testing error graph:")
        plot.plot(self._average_test_error)
        plot.show()


training_set = array([
    [-10, 8],
    [-10, 14],
    [-9, 12],
    [-5, 5],
    [-3, 0],
    [2, -3],
    [5, -7],
    [5, -8],
    [5, -6],
    [5, 0],
    [4, 0],
    [1, 0],
    [1, 1],
    [-2, 5],
    [-3, 11],
    [-6, 18],
    [-10, 24],
])

training_results = array([
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
])

test_set = array([
    [-8, 4],
    [-6, 12],
    [-5, 6],
    [-5, 10],
    [0, 3],
    [1, 0],
    [6, -12],
    [6, -14],
    [-7, 18],
    [-9, 30],
    [-5, 15],
    [-1, 14],
    [1, 4],
    [2, 1],
    [2, 11],
    [3, 0],
    [6, -5],
])

test_results = array([
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
])

perceptron = Perceptron()
perceptron.train_and_test(training_set, training_results, test_set,
                          test_results, 80)
