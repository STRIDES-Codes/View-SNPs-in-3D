# View SNPs in 3D, or Find Symmetries of 3D Structures

[iCn3D](https://github.com/ncbi/icn3d) provides a [web-based tool](https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?mmdbid=1TUP&showanno=1&show2d=1&showsets=1) for protein structure visualizing. Here we seek to expand the functionality of this tool to:
1. integrate 3D visualization of SNPs
2. Build on the functioning SymD integration to include local symmetry analysis capabilities

---

# Project 1: View SNPs in 3D
There are several tools available for visualizing structural homology modelling ([SCWRL](http://dunbrack.fccc.edu/scwrl4/SCWRL4.php), [AMBER](https://ambermd.org/)), most are not available in a web based format, or are not licensed outside for use outside of academia. We explored integration of both scap (http://honig.c2b2.columbia.edu/jackal), and chimera based scripts () to show mutated residues in 3D.


![Methodology](project1/flowchart.png)

## Preliminary Results

### Testing 

#### Mutating residue
Modeller's mutate\_model.py script was used to do the following mutations in 1TUP ([pdb1tup.ent](project1/pdb1tup.ent))
- L111-\>PRO in Chain A ([1tupPRO111.pdb](project1/1tupPRO111.pdb))
- F113-\>VAL in Chain B ([1tupVAL113.pdb](project1/1tupVAL113.pdb))

#### Output mutated residue pdb
- using script at github repo https://github.com/sridharacharya/bioStructureTools/Structure.py
```
- Usage: Structure.py -i <pdb-id> or -f <pdb-file> -r <included resno> -x <excluded resno> -o <output-file-name>
python Structure.py -f 1tupPRO111.pdb -r A111 -o 1tupPRO111_only.pdb 
python Structure.py -f 1tupVAL113.pdb -r B113 -o 1tupVAL113_only.pdb 
```
[1tupPRO111_only.pdb](project1/1tupPRO111_only.pdb)
[1tupVAL113_only.pdb](project1/1tupVAL113_only.pdb)


## References
1. Wang, Jiyao, et al. "iCn3D, a web-based 3D viewer for sharing 1D/2D/3D representations of biomolecular structures." Bioinformatics 36.1 (2020): 131-135.
2. Xiang, Zhexin, and Barry Honig. "Extending the accuracy limits of prediction for side-chain conformations." Journal of molecular biology 311.2 (2001): 421-430.

---

# Project 2: Find Symmetries of 3D Structures
Find the symmetry of a structure (assembly,chain,domain) and display it in iCn3D. We could convert the source code of SYMM to a web service.

## Preliminary data
1. Read the papers: https://academic.oup.com/nar/article/42/W1/W296/2435489 and https://pubmed.ncbi.nlm.nih.gov/27747230/. The web server is at https://galaxyproject.org/use/symd/.
2. The output of SYMD for the PDB 1KQ2 is at [symd-1KQ2.txt](https://github.com/STRIDES-Codes/Find-Symmetries-of-3D-Structures/blob/main/symd-1KQ2.txt). There are four parts. 
3. The Z1 score threshold (in parts 2 and 3 of the output) should be 10 (or 8). If all Z1 scores are less than 10, the structure has no symmetry.
4. The symmetry from RCSB is not complete. It didn't show the local symmetry: https://structure.ncbi.nlm.nih.gov/icn3d/share.html?bGH1BfLsiGFhhTDn8.

## Work items
1. Based on the ouput above, determine how many symmetries in the structure.
![Z1 scores](https://github.com/STRIDES-Codes/Find-Symmetries-of-3D-Structures/blob/main/z1score_angle.png?raw=true)
2. What are the symmetries, such as C6, D2, etc.
3. Calculate the axis for each symmetry.
4. Display the symmetry in iCn3D.


![Symmetry Types](https://github.com/STRIDES-Codes/Find-Symmetries-of-3D-Structures/blob/main/symmetriescategory-horizontal.jpg?raw=true)

## Preliminary results
1. You can test at https://www.ncbi.nlm.nih.gov/Structure/icn3d2/full.html?mmdbid=1kq2 by replacing 1kq2 with any pdb id. 
2. Click the menu "Analysis > Symmetry (SymD)". A popup window is shown. Click "Apply" to show the symmetry.
3. Click "Ctrl + Shift + i" to see the "console" tab. The output from SymD is shown in console.
4. You can select a subset of the structure to do this dynamic symmetry calculation as well.
5. So far it only works for cyclic symmetry. We need to test with more examples and improve it.

### Testing symmD output in iCn3D
About 15 structures were tested. 7 look good. Errors with other structures.
[Details here](project2/icn3d.symm.tests.pdf)

## References About Symmetry Types
1. CE-Symm: https://www.sciencedirect.com/science/article/pii/S0022283614001557
2. CE-Symm: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006842

---
