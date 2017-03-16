from os.path import join
from os import listdir, rmdir
import fnmatch,os, re,sys

rootPath = r'C:\project_files\KC390\Physical_Architecture\source\AFD\platform\verification\tests\KC390'
pattern = '*_ATP.c'
sys.stdout=open(r'C:\Users\akumar4\Desktop\script\test.py','w+')
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        x = os.path.join(root, filename)

        with open(os.path.join(root, filename),'r') as f:
            data=''.join(f.readlines())    
        
        m=re.search(r'OID:(.+?)\n',data,re.M)

        if m: print( x +'\t\t\t\t\t\t\t\t' +m.group(1))
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
sys.stdout.close()

