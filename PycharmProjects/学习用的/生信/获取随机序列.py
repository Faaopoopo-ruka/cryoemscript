#Author：Alex.Zhang
import random
length=input("here you input your favorite length of sequence:")
sequence=''
for i in range(int(length)):
    a=random.choice('atgc')
    sequence+=a
print(sequence.upper())
