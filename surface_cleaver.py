# This script generates surfaces with all possible terminations
# from a list of Miller indices. 

from ase.io import read, write
from pymatgen.io.ase import AseAtomsAdaptor as a2p
from pymatgen.core.surface import SlabGenerator, generate_all_slabs, Structure, Lattice, Slab
# from pymatgen.analysis.wulff import WulffShape
# from pymatgen.analysis.bond_valence import BVAnalyzer
# from ase.visualize import view
import os

bulk_ase = read("CONTCAR")
bulk = a2p.get_structure(bulk_ase)

hkl_list = [(1,0,0), (1,0,1), (2,1,0), (0,1,1), (1,1,1), (2,0,1), (2,1,1), (0,1,0), (3,0,1), (3,1,1), (1,2,1), (1,0,2), (2,2,1), (1,1,2), (3,2,1), (3,0,2)]

for hkl in hkl_list:
    slabgen = SlabGenerator(bulk, hkl, 10, 15, lll_reduce=True, primitive=True)
    all_slabs = slabgen.get_slabs(symmetrize=True, repair=True)

    print("The %s slab has %i terminations." %(hkl, len(all_slabs)))
    dir = "%i%i%i" %hkl
    os.mkdir(dir)

    for i in range(0, len(all_slabs)):
        print("")
        surf_atoms = all_slabs[i].get_surface_sites()["top"]
        print("Slab #%i %i surfacial atoms:" %(i, len(surf_atoms)))
        for j in range(0, len(surf_atoms)):
            print(surf_atoms[j][0].species_string, surf_atoms[j][1])
        print("#Metals: ", len([site for site in surf_atoms if site[0].species_string=="Mg"]))
        # slab_oxi = BVAnalyzer().get_oxi_state_decorated_structure(all_slabs[i])
        name = "%s/POSCAR_%i" %(dir, i)
        write(name, a2p.get_atoms(all_slabs[i]))
    print("")
