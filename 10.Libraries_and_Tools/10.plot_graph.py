import matplotlib.pyplot as plt

def plot_graph():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bieu do Y = X^2')
    plt.show()

plot_graph()
