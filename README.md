# VASH
A VASP + Bash utilities repository.

This repository includes the tools necessary to **construct** and **optimise** surfaces from any given bulk structure. Surfaces are first generated with the *surface_cleaver.py* code. All generated structures can then be optimised with the Birch-Murnaghan EOS using the *bm_generate.py* script, whose results can be read by the *bm_reader.py* script. The *bm_final.py* snippet generates the final structure representative of the surface slab.
