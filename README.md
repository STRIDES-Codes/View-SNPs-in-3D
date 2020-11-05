# View SNP in 3D, or Find Symmetry of 3D Structure

## View SNP in 3D
iCn3D shows SNPs in the sequences. It will be interesting to show the mutated residues in 3D directly. We could use the leap program in AMBER, SCWRL, or other programs.

## Find Symmetry of 3D Structure
Find the symmetry of a structure (assembly,chain,domain) and display it in iCn3D. We could convert the source code of SYMM to a web service.

<b>Preliminary data</b>
1. Read the paper: https://academic.oup.com/nar/article/42/W1/W296/2435489. The web server is at https://galaxyproject.org/use/symd/.
2. The output of SYMD for the PDB 1KQ2 is https://www.ncbi.nlm.nih.gov/Structure/symd/symd.cgi?pdb=1. You can view the source to see the output. There are five parts. 
3. The T1 score threshold (in parts 2 and 3 of the output) should be 10 (or 8). If all T1 scores are less than 10, the structure has no symmetry.
4. The symmetry from RCSB is not complete. It didn't show the local symmetry: https://structure.ncbi.nlm.nih.gov/icn3d/share.html?bGH1BfLsiGFhhTDn8.

<b>Work items/b>
1. Based on the ouput above, determine how many symmetries in the structure.
2. What are the symmetries, such as C6, D2, etc.
3. Calculate the axis for each symmetry.
4. Display the symmetry in iCn3D.



