# Sliders in Matplotlib (demo)

## Overview
This demo shows the use of sliders to create interactive plots in Matplotlib.

First, three subplots containing normal, gamma and uniform distributions are created. Next, a set of sliders is added to each plot, allowing interactive parametrization of the distributions:

- Two sliders control the mean and standard deviation of the normal distribution.
- Two sliders control the shape and scale of the gamma distribution.
- Two sliders control the min and max values of the uniform distribution.
- One slider controls the number of samples pulled from each distribution (between 1000 and 1000).

Plots are automatically updated during interaction.

## Dependencies
matplotlib==2.0.0, numpy==1.14.0


