#Author：Alex.Zhang
complement = {'C':'G','G':'C','T':'A','A': 'T'}
list='GATGGAGG'


rev_dna=''
for i in list:

    rev_dna += complement[i]
rev_dna=rev_dna[::-1]
print(rev_dna)
