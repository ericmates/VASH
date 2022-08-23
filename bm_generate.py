# This snippet generates the starting structures for Birch-Murnaghan
# Equation of State on surface slabs

from ase.io import read, write
from ase import Atoms
import os

slab = read("CONTCAR")
slab.center(7.5, axis=2)
a = slab.get_cell_lengths_and_angles()[0]
b = slab.get_cell_lengths_and_angles()[1]
c = slab.get_cell_lengths_and_angles()[2]

for i in range(0, 5):
        os.mkdir(str(i))
        os.chdir(str(i))
        os.system("cp ../* .")
        slab.set_cell([a*(1 - 0.01 + 0.005*i), b*(1 - 0.01 + 0.005*i), c, 
                       slab.get_cell_lengths_and_angles()[3], slab.get_cell_lengths_and_angles()[4], slab.get_cell_lengths_and_angles()[5]],
                       scale_atoms=True)
        write("POSCAR", slab, format='vasp', sort=False)
        os.system("sbatch run*")
        os.chdir("../")
