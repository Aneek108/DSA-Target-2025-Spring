import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)
m = 20
c = 10
partial_diff_1 = 2*X*(m*X + c - Y)
partial_diff_2 = 2*(m*X + c - Y)
x_equals_one = 2*(m + c - Y)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, partial_diff_1, cmap='viridis', edgecolor='none')
ax.plot_surface(X, Y, partial_diff_2, cmap='viridis', edgecolor='none')
ax.plot_surface(X, Y, X, color='red', edgecolor="none")
# ax.plot_surface(np.ones(X.shape), Y, x_equals_one, color='red', edgecolor="none")

plt.show()