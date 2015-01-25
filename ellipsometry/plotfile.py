#!/usr/local/bin/python
#plot of 2D data from two column .csv file

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import csv
import re
import sys

fname = sys.argv[1]
linestyle = sys.argv[2]
title_text = sys.argv[3]

# Check to see if first row in .csv file contains alpha characters
afile = open(fname, 'r+')
csvreader = csv.reader(afile)
row = csvreader.next()
lst = list(row[0])
header =  re.sub('  +', ',', row[0])
header = header.split(',')

skip = 0

for i in range (0,len(lst)):
  if lst[i].isalpha() == True:
    skip = 1


x = loadtxt(fname, unpack = True, usecols = [0], skiprows = skip) 
y = loadtxt(fname, unpack = True, usecols = [1], skiprows = skip) 

plot(x,y, linestyle, color='red')
xlabel(header[0])
ylabel(header[1])
ylim(2.3,3.5)
title(title_text)
show()


