#Author：Alex.Zhang
import urllib.request
ur1=urllib.request.urlopen('http://www.uniprot.org/uniprot/p01308.fasta')
doc=ur1.read()
print(doc)