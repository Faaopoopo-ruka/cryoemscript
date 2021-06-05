aa_codes = {
         'ALA':'A', 'CYS':'C', 'ASP':'D', 'GLU':'E',
         'PHE':'F', 'GLY':'G', 'HIS':'H', 'LYS':'K',
         'ILE':'I', 'LEU':'L', 'MET':'M', 'ASN':'N',
         'PRO':'P', 'GLN':'Q', 'ARG':'R', 'SER':'S',
         'THR':'T', 'VAL':'V', 'TYR':'Y', 'TRP':'W','DT':'T','DC':'C','DA':'A','DG':'G'}
nucseq = ''
proseq=''

if __name__ == '__main__':
    print (">1TLD")

    for line in open( "4qlc.pdb" ):
        if line[0:6] == "SEQRES":
            columns = line.split()
            test=''.join(columns[4:5])
            if test[0]=='D':

                for resname in columns[4:]:
                    nucseq += aa_codes[resname]
    i = 0
    while i < len(nucseq ):
        print('核酸序列：',nucseq[i:i + 64] )
        i = i + 64
    for line in open( "4qlc.pdb" ):
        if line[0:6] == "SEQRES":
            columns = line.split()
            test=''.join(columns[4:5])
            if test[0] is not 'D':

                for resname in columns[4:]:
                    nucseq += aa_codes[resname]
    i = 0
    while i < len(nucseq ):
        print('蛋白序列：',nucseq[i:i + 64] )
        i = i + 64
