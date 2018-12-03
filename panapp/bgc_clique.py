#! /usr/bin/env python2.7

import os
def search_clique(self,gbk,database,cutoff):
    name=database+str(cutoff)+".tsv"
    input_handle=open(filename, "r")
    for line in input_hande:
        name=line.split("\t")[0]
        array=line.split("\t")[1]
        array=line.split("; ")#check tsv separation of clique
        if gbk in name:
            return (array)

def retrieve_clique(self,args):
    self.args=args
    minlim=self.args.mincutoff # review name of cutoff variable
    if minlim > 100 or minlim < 45:
        sys.exit("mimimun identity cutoff value for cliques out of range")
    idctoff=[100,95,90,80,70,60,45]
    clique_dict={}
    for cutoff in idctoff:
        if cutoff >= minlim:
           clique=search_clique(self.args.gbk, self.args.database, cutoff)
           clique_dict[str(cutoff)]=clique
    return(clique_dict)


