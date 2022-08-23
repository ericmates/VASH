# This script reads the energies and volumes of the optimised
# structures with the directories generated before and
# generates a plot to show the minimum E, V.

import re
from ase import Atoms
from ase.io import read
from ase.eos import EquationOfState
from glob import glob
import os
from matplotlib import pyplot as plt
import sys

def energy():
	outcar_lines = []
	lines = []
	with open('OUTCAR', 'rt') as energy_file:
		for energy_line in energy_file:
			outcar_lines.append(energy_line)
		substr = "energy(sigma->0)"
	for linenum, line in enumerate(outcar_lines):
		index = 0
		str = outcar_lines[linenum]
		index = str.find(substr, index)
		correct_lines = 0
		if index != -1:
				correct_lines = linenum
		if correct_lines != 0:
				line = correct_lines
				lines.append(line)
	number = max(lines)
	return re.findall("[-+]?\d+\.\d+", outcar_lines[max(lines)])[1]

def plot(self, filename=None, show=False, ax=None):
	"""Plot fitted energy curve.

	Uses Matplotlib to plot the energy curve.  Use *show=True* to
	show the figure and *filename='abc.png'* or
	*filename='abc.eps'* to save the figure to a file."""

	import matplotlib.pyplot as plt

	plotdata = self.getplotdata()

	ax = plot(*plotdata, ax=ax)
		if index != -1:
				correct_lines = linenum
		if correct_lines != 0:
				line = correct_lines
				lines.append(line)
	number = max(lines)
	return re.findall("[-+]?\d+\.\d+", outcar_lines[max(lines)])[1]

def plot(self, filename=None, show=False, ax=None):
	"""Plot fitted energy curve.

	Uses Matplotlib to plot the energy curve.  Use *show=True* to
	show the figure and *filename='abc.png'* or
	*filename='abc.eps'* to save the figure to a file."""

	import matplotlib.pyplot as plt

	plotdata = self.getplotdata()

	ax = plot(*plotdata, ax=ax)

	if show:
		plt.show()
	if filename is not None:
		fig = ax.get_figure()
		fig.savefig(filename)
	return ax

energies = []
volumes = []
lst = sys.argv.copy()
lst.pop(0)
for i in lst:
	os.chdir(str(i) + "/")
	cell = read("CONTCAR")
	#print(energy())
	#print(str(cell.get_volume()))
	energies.append(float(energy()))
	volumes.append(cell.get_volume())
	os.chdir("..")
c = cell.get_cell_lengths_and_angles()[2]
	return re.findall("[-+]?\d+\.\d+", outcar_lines[max(lines)])[1]

def plot(self, filename=None, show=False, ax=None):
	"""Plot fitted energy curve.

	Uses Matplotlib to plot the energy curve.  Use *show=True* to
	show the figure and *filename='abc.png'* or
	*filename='abc.eps'* to save the figure to a file."""

	import matplotlib.pyplot as plt

	plotdata = self.getplotdata()

	ax = plot(*plotdata, ax=ax)

	if show:
		plt.show()
	if filename is not None:
		fig = ax.get_figure()
		fig.savefig(filename)
	return ax

energies = []
volumes = []
lst = sys.argv.copy()
lst.pop(0)
for i in lst:
	os.chdir(str(i) + "/")
	cell = read("CONTCAR")
	#print(energy())
	#print(str(cell.get_volume()))
	energies.append(float(energy()))
	volumes.append(cell.get_volume())
	os.chdir("..")
c = cell.get_cell_lengths_and_angles()[2]

eos = EquationOfState(volumes, energies, eos='murnaghan')
v0, e0, B = eos.fit()
print(v0, c, e0)
#print(e0)
#eos.plot.set_title('R2: ' + str(r2_score(y_test, y_predicted)))
eos.plot(filename='plot.pdf')
