from rutermextract import TermExtractor
from topia.termextract import extract
term_extractor = TermExtractor()
f = open("text1.txt")
text = f.read()
for term in term_extractor(text.decode('cp1251')):
    print (term.normalized)
f1=open("text2.txt")
text1 = f1.read()
extractor = extract.TermExtractor()
extractor.filter = extract.permissiveFilter
extractor(text1)