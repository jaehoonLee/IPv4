__author__ = 'leejaehoon'

from os import listdir
from os.path import isfile, join, basename

onlyfiles = [f for f in listdir('.') if isfile(join('.', f)) if f != basename(__file__) if f != 'README.md']

for f in onlyfiles:
    file = open(f, 'r')
    str = file.readline()
    while str :
        str_ar = str.split('\t')
        str_ar[2] = str_ar[2].rstrip('\n')
        print str_ar
        str = file.readline()

    #print str_ar

