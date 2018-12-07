'''The next modules recieve the BGC.gbk to search cliques in the BGCcliques.tsv files
at different cutoff %identity values, recieve a GBK filename present in the GBK folder database
and a cutoff value, and return cliques for files above minimum identity cutoff
return a dictionary with the list of cliques at different identity cutoff
'''

import os, re, sys

def search_clique(gbk,filename):
    input_handle=open(filename, "r")
    for line in input_handle:
        line=line.rstrip()
        name=line.split("\t")[0]
        array=line.split("\t")[2:]
        if gbk in name:
            return (array)


def retrieve_clique(gbk,database,minlim):
    if minlim > 100 or minlim < 45:
        sys.exit("mimimun identity cutoff value for cliques out of range")
    path= "/".join(database.split("/")[:-1])
    idctoff=[100, 95, 90, 80, 70, 60, 45]
    prefix=database.split("/")[-1] #split folder by "/" character
    mid= ['_100','-95','-90','-80','-70','-60','-45']
    sufix="_clique.tsv"
    cliques=[]
    for i,cutoff in enumerate(idctoff):
        prefix+=mid[i]
        filename=path+"/"+prefix+sufix
        if cutoff >= minlim:
           clique=search_clique(gbk,filename)
           cliques.append(clique)
    return(cliques)


