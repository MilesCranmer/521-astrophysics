"""This module plots the Johnson filters."""

# Use Numpy for calculations
import numpy as np
# Use astropy's unit package for scaling
import astropy.units as u
# Use matplotlib for plotting
import matplotlib.pyplot as plt


# The recorded data, with units.
filter_names = list("UBVRIJHKLM")

flux_density = np.array(
	[4.266, 6.822, 3.802, 1.738, 0.8318,
	0.3311, 3.981e-2, 8.128e-3, 2.375e-3, 1.230e-4])*1e-8*u.Unit("W/(m^2 micron)")

central_wavelength = np.array(
	[0.365, 0.433, 0.550, 0.700, 0.900,
	1.250, 2.200, 3.400, 4.800, 10.2])*u.micron

# Make sure we have recorded the same number for each!
assert len(filter_names) == flux_density.size == central_wavelength.size

nm_wavelengths = central_wavelength.to('nm').value
magnitudes = np.zeros(len(nm_wavelengths))
#x_positions = range(len(nm_wavelengths))

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

X = nm_wavelengths
Y = flux_density.value
ax1.scatter(X, Y, color='black', marker='o')
ax1.set_xlabel(r"$\lambda_c=$ Central effective wavelength $ {\rm(nm)}$")
ax1.set_xscale('log')
ax1.set_xlim(min(X)/1.5, max(X)*1.5)
ax1.set_ylabel(r"$F_\lambda=$ Flux density  $(\mathrm{ W m^{-2} \mu m^{-1}})$ ")
ax1.set_yscale('log')
ax1.set_ylim(min(Y)/1.5, max(Y)*1.5)
ax1.tick_params(axis=u'both', which=u'both',length=5)

ax2.set_xscale('log')
ax2.set_xlim(ax1.get_xlim())
ax2.set_xlabel("Johnson filter")
ax2.tick_params(axis=u'both', which=u'both',length=0)
ax2.set_xticks(nm_wavelengths)
ax2.set_xticklabels(filter_names)

for x_pos in X:
	ax2.axvline(x_pos, linestyle = 'dotted', lw=0.5, color='black')

for y_pos in Y:
	ax1.axhline(y_pos, linestyle = 'dotted', lw=0.5, color='black')

plt.savefig('johnson_filter_plot.png')


###(Since I am unsure if the question is asking for two plots in the same
### file, or actually in the same axes (as I did above), here is code for
### two different plots in the same image:)
