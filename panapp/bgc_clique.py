#! /usr/bin/env python2.7

import os
import re

def search_clique(self,gbk,database,cutoff):
    name=database+str(cutoff)+".tsv"
    input_handle=open(filename, "r")
    for line in input_hande:
        name=line.split("\t")[0]
        array=line.split("\t")[1]
        array=line.split("; ")#check tsv separation of clique
        if gbk in name:
            return (array)

def parse_multigeneblast(self,gbk):
    input_handle=open("mgboutput.txt", "r")
    #parse content of the text file from Multigenblast run
    #if exist retrieve the name of the gbk with the highest score
    #display alignment stats of the best hit
    for line in input_handle:
        gbk
        rexp=re.compile(".*gbk")
        if re.match(rexp, line):
        #save file if best hit
            tmp=1##*complete code 
    return(besthit)
    print (blast_stats)

def retrieve_clique(self,gbk,database,minlim):
    gbk=parse_multigeneblast(gbk)
    if minlim > 100 or minlim < 45:
        sys.exit("mimimun identity cutoff value for cliques out of range")
    idctoff=[100,95,90,80,70,60,45]
    clique_dict={}
    for cutoff in idctoff:
        if cutoff >= minlim:
           clique=search_clique(gbk, database, cutoff)
           clique_dict[str(cutoff)]=clique
    return(clique_dict)


