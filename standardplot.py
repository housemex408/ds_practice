import matplotlib.pyplot as pyplot
import numpy as numpy

x = numpy.linspace(0, 20, 100)     # Create a list of evenly-spaced numbers over the range
pyplot.plot(x, numpy.sin(x))       # Plot the sine of each x point
pyplot.show()                      # Display the plot