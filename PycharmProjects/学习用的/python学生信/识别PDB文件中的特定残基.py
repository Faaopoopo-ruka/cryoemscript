#Author：Alex.Zhang
import struct
pdb_format='6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s10s2s'
def parse_atom_line(line):
    tmp=struct.unpack(pdb_format,line.encode('utf-8'))
    atom=tmp[3].strip()
    res_type=tmp[5].strip()
    res_num=tmp[8].strip()
    chain=tmp[7].strip()
    x=float(tmp[11].strip())
    y=float(tmp[12].strip())
    z=float(tmp[13].strip())
    return chain,res_type,res_num,atom,x,y,z
def main(pdb_file,residues,outfile):
    with open(pdb_file,'r',encoding='utf-8') as pdb:
        outfile=open(outfile,'w')
        for line in pdb:
            if line.startswith('ATOM'):
                res_data=parse_atom_line(line)
                for a, num in residues:
                    if res_data[1]==a and res_data[2]== num:
                        outfile.write(line)
    outfile.close()
residues=[('ASP','102'),('HIS','57'),('SER','195')]
main('4qlc.pdb',residues,'new.pdb')