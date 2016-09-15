from astropy import units as u
from astropy import constants as const
import numpy as np

def reduced_mass(m1, m2):
	"""Calculate the reduced mass"""
	return m1*m2/(m1+m2)

def orbital_momentum(M, m, a, e, P):
	"""Calculate the orbital momentum of a system"""
	return reduced_mass(M, m)*np.sqrt(const.G*M*a*(1-e**2))

def rotational_momentum_sphere(m, r, T):
	"""Rotational momentum of a sphere"""
	return 2./5*m*r*r*2*np.pi/T

def pprint(value):
	"""Print in scientific notation"""
	print "{0:0.03e}".format(value.si)


####Assignment 1
##2.6a
#print orbital_momentum(const.M_sun, const.M_jup, 5.2*const.au, 0.048, 11.86*u.yr)
##2.6b
#d_sun = 5.2/(const.M_sun/const.M_jup + 1) * const.au
#print (2*np.pi*(d_sun**2)*const.M_sun/(11.86*u.yr)).to('kg m2 / s')
##2.6c
#d_j = 5.2/(const.M_jup/const.M_sun + 1) * const.au
#print (2*np.pi*(d_j**2)*const.M_jup/(11.86*u.yr)).to('kg m2 / s')
##2.6d
#print "Sun:", rotational_momentum_sphere(const.M_sun, 6.96e8*u.m, 26*u.day).to('kg m2 / s')
#print "Jupiter:", rotational_momentum_sphere(const.M_jup, 6.9e7*u.m, 10*u.hr).to('kg m2 / s')
##2.8a
#print (const.R_earth+610*u.km)/(const.au)
###Non-text Questions
##7
d = 1/(0.742*u.arcsec)*u.arcsec*u.pc
print (((1.4e11 * u.cm)/d).si * u.rad).to('arcsec')