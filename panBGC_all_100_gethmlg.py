'''
8 octubre 2018
Fernando Garcia Guevara

The following script find retrives pan genome matrices from a list of cd-hit clusters.

First read the names of the groups of bgcgbk files (output of panbcg.py script), the files were grouped by % identity of their constituent biosynthetic genes. Then for each group of BGC the script calls the program get homologues, and follow the instructions to retrieve a pan genome matrix.

The get_homologues program returns a series of outputs, some of them probably not used for later analisys, consider deleting them for saving space purposes. 

'''

#! /usr/bin/pyton2.7
import argparse, re
import os, subprocess
#from Bio import SeqIO #fasta

#define bgc_clster object
class bgc_clstr(object):
    def __init__(self,reprsnt,bgc_type):
        self.id =reprsnt
        self.file_list=[]
        self.type=bgc_type
# add a filename to the gruop if if not peviouly included 
    def add_filenames(self,line):
        self.file_list=line.split("\t")

bgcs={}
clstr= open( "output.txt", "r" )

for line in clstr:
    line=line.rstrip()
    if re.match(">", line):
        line=line.replace(">","")
        key=line.split("\t")[0]
        bgc_type=line.split("\t")[1]
        bgcs[key]=bgc_clstr(key,bgc_type)
    else:
        bgcs[key].add_filenames(line)
clstr.close()

#create folders with symlinks to group of bgcs, approximately 2500 folders
#**ensure those gbk files contain locus_tag field**

subprocess.call(["mkdir", "output_panbgc_pyscript"])
os.chdir("output_panbgc_pyscript")

for key in bgcs.keys():
    subprocess.call(["mkdir",key],)
    for filename in bgcs[key].file_list: 
        subprocess.call(["ln", "-s", filename, "."], cwd=key)

#subprocess.call(["cd", ".."])

#proc = subprocess.Popen("ls",stdout=subprocess.PIPE)
#folder_string = proc.stdout.read() 
#folder_list= folder_string.split("\n")

#call get_homologues using blau location, modifiy path for using only program name
#find clusters inside gbk files using orthoMCL algorithm -M, include all clusters -t 0, require equal pfam domain composition -D, optiional hmmer -o

#for folder in folder_list:
#    subprocess.call(["/scratch/share/apps/get_homologues-x86_64-20170105/get_homologues-est.pl", "-t", "0", "-M", "-d", folder])
#    hmlg_folder= folder + "_homologues"
#    matrix_folder=folder + "_matrix"
#    MCL_folder = subprocess.call(["find", hmlg_folder, "-name", "*_algOMCL_e0_", "-type","d"])
#    subprocess.call(["/scratch/share/apps/get_homologues-x86_64-20170105/compare_clusters.pl", "-o", matrix_folder , "-m", "-d", MCL_folder])

#consider removing non employed files, specially for large clusters of BGC, 

#**parse the pangenome matrix to calculate cloud shell and core genomes, genes present in one group not present in the rest view genomic context of any species in queried group, highlight genes absent ouside of the grpup., plot heatmat for requested BGC 

