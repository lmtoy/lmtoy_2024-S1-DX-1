#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-DX-1"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["PG1402+261"] = \
 [ 131808, 131809, 131810, 131812, 131813,]



#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["PG1402+261"] = ""


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["PG1402+261"] = ""


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
