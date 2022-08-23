# This snippet generates the final structure to be calculated 
# from the lattice parameters obtained in the Birch-Murnaghan optimisation

from ase.io import read, write
from ase import Atoms
import os

slab = read("CONTCAR")
a = input("a LP: ")
b = input("b LP: ")
c = input("c LP: ")

slab.set_cell([a, b, c, slab.get_cell_lengths_and_angles()[3], slab.get_cell_lengths_and_angles()[4], slab.get_cell_lengths_and_angles()[5]], scale_atoms=True)
write("POSCAR", slab, format='vasp', sort=False)
