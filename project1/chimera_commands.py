import os
import chimera
import re

DIR = ""
RESNO = 113
RESNA = "leu"

os.chdir("DIR")

opened = chimera.openModels.open('project1/pdb1tup.ent')
mol = opened[0]

chimera.runCommand('swapaa leu :113.b')

f = open("project1/pdb1tup_mut.ent", "w")
f.write("%s\n" % "HEADER    Residue mutated by Chimera")
res = mol.residues[RESNO]

f.write("%s " % res.id)

#see https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/midas/swapaa.html
def cmdAddAttr(cmdName, args):
  from AddAttr import addAttributes
  from Midas.midas_text import doExtensionFunc
  doExtensionFunc(addAttributes, args,
  specInfo=[("spec", "models", "molecules")])

  from Midas.midas_text import addCommand
  addCommand("defattr", cmdAddAttr, help=True)
