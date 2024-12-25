import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(X, y, theta, learning_rate, iterations, visualize=True):
    m = len(y)
    cost_history = []

    for i in range(iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = (1 / m) * X.T.dot(errors)
        theta -= learning_rate * gradient
        cost = (1 / (2 * m)) * np.sum(errors ** 2)
        cost_history.append(cost)

        if i % 50 == 0:
            print(f"Iteration {i}, Cost: {cost:.4f}")

    if visualize:
        plt.figure(figsize=(10, 6))
        plt.plot(range(iterations), cost_history, label="Cost Function", color="blue")
        plt.title("Cost Function Decrease")
        plt.xlabel("Iterations")
        plt.ylabel("Cost Value")
        plt.grid()
        plt.legend()
        plt.show()

    return theta, cost_history

if __name__ == "__main__":
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)

    X_b = np.c_[np.ones((100, 1)), X]
    theta_init = np.random.randn(2, 1)
    learning_rate = 0.1
    iterations = 500

    theta_opt, cost_hist = gradient_descent(X_b, y, theta_init, learning_rate, iterations)
    print("Optimal parameters:", theta_opt)