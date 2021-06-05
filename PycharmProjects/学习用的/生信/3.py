
# Author:pymingming
import pyperclip
def code_table():
    f = open('code.txt','r')
    s = f.readlines()
    l1,l2 = [],[]
    for line in s:
        key = line.split()[4]
        l1.append(key)
        value = line.split()[3]
        l2.append(value)
    code_dict = dict(zip(l1,l2))
    return code_dict

def geneseq():
    seq = input('输入cds基因序列：')
    seq = seq.replace('T','U')
    seq_code = [seq[x:x+3] for x in range(0,len(seq.strip()),3)]
    return seq_code

def match():
    list_aa_seq = []
    seq_code = geneseq()
    code_dict = code_table()
    for code in seq_code:
        for key in code_dict.keys():
            if code in key:
                list_aa_seq.append(code_dict[key])
        if code not in str(code_dict.keys()):
            list_aa_seq.append('*')
    aa_seq = ''.join(list_aa_seq)
    protein = '\n'.join(aa_seq[x:x+40] for x in range(0,len(aa_seq),40))
    return  protein

if __name__ == '__main__':
    result = match()
    print(result)
    pyperclip.copy(result)