'''
1 noviembre 2018
Fernando Garcia Guevara

Leer el archivo .clstr creado con cdhit, a partir de all bgc biosynthetic genes

1 Crear un archivo tsv con el nombre de cada archivo gbk (33k) y el BGC representativo (o lista de BGC representativos)

2 Crear un archivo con el nombre de cada BGC representativo y la lista de los BGC que representa.


'''

#! /usr/bin/pyton2.7
import argparse
import os, re
#from Bio import SeqIO #fasta

#define blast subject object
class gene_clstr(object):
    def __init__(self,clstr_id):
        self.id=clstr_id
        self.reprsnt=""
        self.file_list=[]
        self.type="ND"
    # method calculate coverage of biosynthetic genes in BGC
    def add_member(self, line):
        gene_id=line.split(">")[1]
        filename=gene_id.split(";")[0]
        if re.search("\*$", line):
            self.reprsnt=filename
            self.file_list.append(filename)
            self.type=gene_id.split(";")[2]
        else:
            self.file_list.append(filename)

class bgc_repbgc(object):
    def __init__(self, filename, bgc_type):
        self.id=filename
        self.type=bgc_type
        self.representative_list=[]
    def add_files(self, representative_filename):
        if representative_filename not in self.representative_list:
            self.representative_list.append(representative_filename)

class bgc_clstr(object):
    def __init__(self,reprsnt,bgc_type):
        self.id=reprsnt
        self.file_list=[]
        self.type=bgc_type
     # add a filename to the gruop if not peviously included
    def add_files(self,filename_list):
        for name in filename_list:
            if name in self.file_list:
                continue
            else:
                self.file_list.append(name)        

# read in script parameters
# from collections import defaultdict

parser= argparse.ArgumentParser()
parser.add_argument('--clstr',
                    action='store',
                    dest='clstr',
                    help='.clstr file returned by cd-hit (use cd-hit -a option to preserve the complete sequence name)')
parser.add_argument('--out_name',
                    action='store',
                    dest="out_name",
                    default="output.txt",
                    help="name for output files and folder")

arg=parser.parse_args()


#leer .clstr file cdhit
#cada cluster comienza con >
#guarda la informacion del archivo en un hash/dictionary

clustr={}
cdhit_clusters= open(str(arg.clstr), "r" )
for line in cdhit_clusters:
    line=line.rstrip()
    if re.match(">", line):
        line=line.replace(">","")
        key=line
        clustr[key]=gene_clstr(key)
    else:
        clustr[key].add_member(line)
cdhit_clusters.close()

#recorre cada clustr y genera diccionario con info para primer archivo
bgc30k={}
bgcs={}
for key in clustr.keys():
#this part for getting filename of all gbk files and associate their respective representative
    for line in clustr[key].file_list:
        try:
            bgc30k[line]
        except:
            bgc30k[line]=bgc_repbgc(line, clustr[key].type)
            bgc30k[line].add_files(clustr[key].reprsnt)
        else:
            bgc30k[line].add_files(clustr[key].reprsnt)
#this part for associate the representative gbk and the files they represent
    try:
        bgcs[[key].reprsnt]
    except:
        bgcs[clustr[key].reprsnt]=bgc_clstr(clustr[key].reprsnt, clustr[key].type)
        bgcs[clustr[key].reprsnt].add_files(clustr[key].file_list)
    else:
        bgcs[ [key].reprsnt].add_files( [key].file_list)

outfile=arg.out_name + "_allBGC.tsv"
output= open(outfile, "w")
print len(bgc30k.keys())
for key in bgc30k.keys():
    output.write("%s\t" %key)
    for rep in bgc30k[key].representative_list:
        output.write("%s\t" %rep )
    output.write("\n")
output.close()

outfile=arg.out_name + "_rep_BGC.tsv"
output= open(outfile, "w")

print len(bgcs.keys())
for key in bgcs.keys():
    n= len(bgcs[key].file_list)
    output.write ("%s\t%s\t%s\t" %(key, bgcs[key].type, n))
    for file_name in bgcs[key].file_list:
        output.write ("%s\t" % file_name)
    output.write("\n")
output.close()

outfile=arg.out_name + "_clique.tsv"
output= open(outfile, "w")
print len(bgc30k.keys())
for key in bgc30k.keys():
    bgc_clique=[]
    output.write("%s\t" %key)
    for rep in bgc30k[key].representative_list:
        if rep not in bgc_clique:
            bgc_clique.append(rep)
        for name in bgcs[rep].file_list:
            if name not in bgc_clique:
                bgc_clique.append(name)
    output.write("%s\t" %len(bgc_clique) )
    for name in bgc_clique:
        output.write("%s\t" %name)
    output.write("\n")

output.close()
