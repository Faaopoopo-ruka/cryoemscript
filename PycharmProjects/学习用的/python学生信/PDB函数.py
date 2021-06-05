#Author：Alex.Zhang
import struct
pdb_format='6s5s1s4s1s3s1s1s4s1s3s8s8s6s6s10s2s3s'
amino_acids = {
         'ALA':'A', 'CYS':'C', 'ASP':'D', 'GLU':'E',
         'PHE':'F', 'GLY':'G', 'HIS':'H', 'LYS':'K',
         'ILE':'I', 'LEU':'L', 'MET':'M', 'ASN':'N',
         'PRO':'P', 'GLN':'Q', 'ARG':'R', 'SER':'S',
         'THR':'T', 'VAL':'V', 'TYR':'Y', 'TRP':'W','DT':'T','DC':'C','DA':'A','DG':'G'}
def threeletter2oneletter(residues):
    for i,threeletter in enumerate(residues):
        residues[i][0]=amino_acids[threeletter[0]]
