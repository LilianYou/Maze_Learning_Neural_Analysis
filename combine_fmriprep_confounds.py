#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:20:47 2018

@author: stark
"""

"""
Combines the passed-in confounds.tsv files and strips off the errant
NonSteadyStateOutlier00 column if it exists
"""

import pandas as pd
import sys
import os

if len(sys.argv) < 2:
    print('You must provide at least one confounds file to process')
    sys.exit()

def RemoveNonSteady(df):
    if 'NonSteadyStateOutlier00' in df.columns:
        df=df.drop('NonSteadyStateOutlier00',axis=1)
    if 'NonSteadyStateOutlier01' in df.columns:
        df=df.drop('NonSteadyStateOutlier01',axis=1)
    if 'NonSteadyStateOutlier02' in df.columns:
        df=df.drop('NonSteadyStateOutlier02',axis=1)
    return df

# Grab the first one
allconfounds=pd.read_csv(sys.argv[1],delim_whitespace=True)
print('Loading ' + sys.argv[1])
allconfounds=RemoveNonSteady(allconfounds)

if len(sys.argv) > 2:
    for fname in sys.argv[2:]:
        print('Loading ' + fname)
        confounds=pd.read_csv(fname,delim_whitespace=True)
        confounds=RemoveNonSteady(confounds)
        allconfounds=allconfounds.append(confounds)

        
if os.sep in sys.argv[1]:  # Input file has a directory name - try to extract it
    outname=os.path.dirname(sys.argv[1])+os.sep+'allconfounds.tsv'
else:
    outname='allconfounds.tsv'
print('Saving ' + outname)    
allconfounds.to_csv(outname,sep='\t',index=False)
allconfounds.to_csv(outname.replace('allconfounds.tsv','allconfounds_nohdr.tsv'),sep='\t',index=False,header=False)

        
