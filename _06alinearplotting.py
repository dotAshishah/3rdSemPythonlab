import matplotlib.pyplot as plt
def linear_plot():
    x=[1,2,3,4,5,6]
    y=[3,7,9,11,14,18]
    plt.plot(x,y,label="Linear function : y= 2x")
    plt.title("Linear Plotting")
    plt.xlabel("X Value")
    plt.ylabel("Y Value")
    plt.show()
linear_plot()