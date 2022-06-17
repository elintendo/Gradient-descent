import numpy as np

x = np.array([1, 3, 7, 10, 15])
y = np.array([5, 9, 8, 9, 13])

def gradientDescent(x, y):
    m = b = 1
    iterations = 10000
    n = len(x)
    learning_rate = 0.01

    for i in range(iterations):
        approx = m * x + b
        cost = (1/n) * sum(elem**2 for elem in (y - approx))

        md = (-2/n) * sum(x * (y - approx))
        bd = (-2/n) * sum(y - approx)

        m -= learning_rate * md
        b -= learning_rate * bd

        print("m: {}, b: {}, i: {}, cost: {}".format(m, b, i, cost))

gradientDescent(x, y)