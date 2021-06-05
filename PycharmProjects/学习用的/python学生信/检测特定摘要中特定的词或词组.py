#Author：Alex.Zhang#Author：Alex.Zhang
import urllib.request
import re
#word to be researched
keyword=re.compile('Schistosomiasis')
pmids=['18235848','18235847','18235849']
count=0
for pmid in pmids:
    count+=1
    url='https://www.ncbi.nlm.nih.gov/pubmed/?term=%s'%pmid
    handler=urllib.request.urlopen(url)
    html=handler.read()


    title_regexp=re.compile('<h1>.{5,400}</h1>')
    title_text=title_regexp.search(html.decode('utf-8'))
    abstract_regexp=re.compile('<h3>Abstract</h3><div class\=""><p>.{20,3000}</p></div>')
    abstract_text=abstract_regexp.search(html.decode('utf-8'))
    titlee='abstract'+str(count)
    title=title_text.group()
    abstract=abstract_text.group()
    words=keyword.finditer(abstract,re.IGNORECASE)
    if words:
        print(title)
    for word in words:
        print(word.group(),word.start(),word.end())

