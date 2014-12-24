import requests
import lxml.html
import json

f1 = open('magoosh_basic', 'w')
f2 = open('magoosh_common','w')
f3 = open('magoosh_adv','w')
basic = 'http://quizlet.com/45473963/magoosh-gre-flashcards-basic-all-i-vii-flash-cards/'
common = 'http://quizlet.com/45473977/magoosh-gre-flashcards-common-all-i-vi-flash-cards/'
adv = 'http://quizlet.com/45473953/magoosh-gre-flashcards-advanced-all-i-vii-flash-cards/'
hxs = lxml.html.document_fromstring(requests.get(basic).content)
words = []
meanings = []
words = hxs.xpath('//span[@class="qWord lang-en"]/text()')
for elem in hxs.xpath('//span[@class="qDef lang-en"]'):
     meanings.append(''.join(elem.xpath('text()')))
print len(words)
for i,word in enumerate(words):
    f1.write(word+'\n')
    f1.write(meanings[i].encode('ascii', 'ignore')+'\n')
    f1.write("%\n")
f1.close()


hxs = lxml.html.document_fromstring(requests.get(common).content)
words = []
meanings = []
words = hxs.xpath('//span[@class="qWord lang-en"]/text()')
for elem in hxs.xpath('//span[@class="qDef lang-en"]'):
     meanings.append(''.join(elem.xpath('text()')))
print len(words)
for i,word in enumerate(words):
    f2.write(word+'\n')
    f2.write(meanings[i].encode('ascii', 'ignore')+'\n')
    f2.write("%\n")
f2.close()


hxs = lxml.html.document_fromstring(requests.get(adv).content)
words = []
meanings = []
words = hxs.xpath('//span[@class="qWord lang-en"]/text()')
for elem in hxs.xpath('//span[@class="qDef lang-en"]'):
     meanings.append(''.join(elem.xpath('text()')))
print len(words)
for i,word in enumerate(words):
    f3.write(word+'\n')
    f3.write(meanings[i].encode('ascii', 'ignore')+'\n')
    f3.write("%\n")
f3.close()
