### import sys and statistics modules used in this script
### import mean and quantiles functions

import sys
from statistics import mean
from statistics import quantiles

### input and output files
### input file came from Seurat output file with Averageexpression commend
f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'w')

### define local functions for calculation
### calculate relative values for each gene; transfer input list with original geneexpression value to relative expression
def cal_relative_exp(Exp_list):
    Exp_list_t = [float(i) for i in Exp_list]
    Mean_list = mean(Exp_list_t)
    Relative_list = [j / Mean_list for j in Exp_list_t]
    return Relative_list

