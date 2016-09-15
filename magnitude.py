"""This module performs flux ratio calculations for sources.
More specifically, it calculates the flux ratios given source
magnitude differences. It also plots this relationship.
"""

# Use numpy for calculations
import numpy as np
# Use matplotlib for creating plots
import matplotlib.pyplot as plt



def flux_ratio(magnitude_difference):
    """Calculate the flux ratio for a source

    Inputs:
        magnitude_difference = m2-m1 for sources 1 and 2
    Outputs:
        flux_ratio = 100^(magnitude_difference/5)
    """
    return np.power(100, magnitude_difference/5.)



# Generate some magnitude differences to try out
test_magnitude_differences = np.array([1, 2, 3, 4, 5, 6, 10, 20, 30])
# Numpy lets us pass these through the function in one go!
test_flux_ratios = flux_ratio(test_magnitude_differences)



# Plot this relationship with matplotlib
plt.plot(
    test_magnitude_differences, test_flux_ratios,
    linestyle='--', marker="v", color='black')
plt.yscale('log')
plt.xlabel('Magnitude difference $(m_2-m_1)$')
plt.ylabel('Flux ratio $(F_1/F_2)$')
plt.savefig('flux_vs_mag.png')