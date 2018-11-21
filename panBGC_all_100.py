'''
2 octubre 2018
Fernando Garcia Guevara
The following script find retrives pan genome matrices from a list of cd-hit clusters.
The script input requires: 
1 The folder path containing all gbk files of the GBC database
2 The .cluster file returned by cd-hit program removing redundancy from a .faa database of biosinthetic genes.

The script reads the .cluster of biosinthetic genes and using the information generates clusters of BGC (each one corresponding to a .gbk). Each cluster of BGC should have more than 3 .gbk files to continue trough the next stage. 

The script calls for the program get_homologues for each cluster of BGC, and follows the manual in get_homologues to create a pan-genome matrix
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

class bgc_clstr(object):
    def __init__(self,reprsnt,bgc_type):
        self.id=reprsnt
        self.file_list=[]
        self.type=bgc_type
# add a filename to the gruop if if not peviouly included 
    def add_files(self,filename_list):
        for name in filename_list:
            if name in self.file_list:
                continue
            else:
                self.file_list.append(name)
 
# read in script parameters
# from collections import defaultdict

parser= argparse.ArgumentParser()
parser.add_argument('--gbk_folder',
                    action='store',
                    dest='gbk_folder',
                    help='complete path to folder containing bgc gbk files found with AntiSMASH')
parser.add_argument('--clstr',
                    action='store',
                    dest='clstr',
                    help='.clstr file returned by cd-hit (use cd-hit -a option to preserve the complete sequence name)')
parser.add_argument('--out_name',
                    action='store',
                    dest="out_name",
                    help="name for output files and folder")

arg=parser.parse_args()

#check whether output_name exist or assign defaul value

#if arg.out_name

#leer .clstr file cdhit output
#estre archivo contiene la informacion de los clusters de genes
#cada cluster comienza con >, y luego enlista los genes que pertenecen al cluster
#recuperar el nombre del gbk para formar clusters de GBKs y no solo de biosynth genes

genes={}
bgcs={}

cdhit_clusters= open(str(arg.clstr), "r" )
for line in cdhit_clusters:
    line=line.rstrip()
    if re.match(">", line):
        line=line.replace(">","")
        key=line
        genes[key]=gene_clstr(key)
    else:
        genes[key].add_member(line)
cdhit_clusters.close()

for key in genes:
#    check whether members of list already present in list
    try:
        bgcs[genes[key].reprsnt]
    except:
        bgcs[genes[key].reprsnt]=bgc_clstr(genes[key].reprsnt, genes[key].type)    
        bgcs[genes[key].reprsnt].add_files(genes[key].file_list)
    else:
        bgcs[genes[key].reprsnt].add_files(genes[key].file_list)

#si tienen la misma longitud se trata del mismo gen, si es mas corto considerar esa informacion despues 
# an output folder, a file for all, a file for each or a folder for each with simbolic links
total=0
output= open("output.txt", "w")
for key in bgcs.keys():
    n=len(bgcs[key].file_list)
#    total+=n
    if n > 2:
        total+=n
        output.write (">%s\t%s\t%s\n" % (key, bgcs[key].type, n))
        for file_name in bgcs[key].file_list:
            output.write ("%s%s\t" %(arg.gbk_folder, file_name))
        output.write("\n")
output.close()

print total

