#!/usr/bin/env python

import sys
import chimera

'''
November 8, 2020
smalkaram@wvstateu.edu
CSHL_Codeathon_2020

Dependencies
  1. install UCSF-Chimera package
  2. install "pychimera" python module (or) set Chimera python directory in PYTHONPATH 

Issues
 - Need to correct the running of script in terminal
'''

try:
  opts,args = getopt.getopt(argv, ":f:m:h:r:c:o:")
except:
  print("Usage: ChimeraMutateResidue.py -f <PDB file> -r <RESIDUE number> -c <CHAIN name> -m <MUTANT (3-letter) residue> -o <OUTPUT file>")
  sys.exit(2)

for opt,arg in opts:
  if opt == '-h':
    print("Usage: ChimeraMutateResidue.py -f <PDB file> -r <RESIDUE number> -c <CHAIN name> -m <MUTANT (3-letter) residue> -o <OUTPUT file>")
    sys.exit(2)
  elif opt in ("-f"):
    INPUT = str(arg)
  elif opt in ("-r"):
    RESIDUE = str(arg)
  elif opt in ("-c"):
    CHAIN = str(arg)
  elif opt in ("-m"):
    MUTANT = str(arg)
  elif opt in ("-o"):
    OUTPUT = str(arg)


PDBMODELS  = chimera.openModels.open(INPUT)
mol = PDBMODELS[0]
mutate_command = "swapaa " + MUTANT + " :" + RESIDUE + "." + CHAIN
chimera.runCommand(mutate_command)
select_command = "select :" + RESIDUE + "." + CHAIN
chimera.runCommand(select_command)
output_command = "write format pdb selected 0 " + OUTPUT
chimera.runCommand(output_command)

print("Residue " + RESIDUE + " is mutated to " + MUTANT + " and stored at " + OUTPUT)
