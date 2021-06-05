#Author：Alex.Zhang
import urllib.request
import re
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
    with open(titlee,'w',encoding='utf-8') as en:
        en.write('tile')
        en.write(title_text.group())
        en.write('\n')
        en.write('abstract:')
        en.write(abstract_text.group())

    print('Title:',title_text.group())
    print('abstract:',abstract_text.group())