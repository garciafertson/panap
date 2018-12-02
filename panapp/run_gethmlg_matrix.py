'''
8 octubre 2018
Fernando Garcia Guevara

First read the names of the groups of bgcgbk files (output of panbcg.py script), the files were grouped by % identity of their constituent biosynthetic genes. Then for each group of BGC the script calls the program get homologues, and follow the instructions to retrieve a pan genome matrix.

The get_homologues program returns a series of outputs, some of them probably not used for later analisys, consider deleting them for saving space purposes. 

'''

#! /usr/bin/pyton2.7
import os, subprocess
#from Bio import SeqIO #fasta
proc = subprocess.Popen("ls",stdout=subprocess.PIPE)
folder_string = proc.stdout.read()
folder_list= folder_string.split("\n")

#print(folder_list[0])

#call get_homologues using blau location, modifiy path for using only program name
#find clusters inside gbk files using orthoMCL algorithm -M, include all clusters -t 0, require equal pfam domain composition -D, optiional hmmer -o

for folder in folder_list:
    subprocess.call(["/scratch/share/apps/get_homologues-x86_64-20170105/get_homologues.pl", "-t", "0", "-M", "-d", folder])
    hmlg_folder= folder + "_homologues"
    matrix_folder=folder + "_matrix"
    proc = subprocess.Popen(["find", hmlg_folder, "-name", "*_algOMCL_e0_", "-type","d"],stdout=subprocess.PIPE )
    MCL_folder = proc.stdout.read()
    MCL_folder= str(MCL_folder)
    MCL_folder= MCL_folder.rstrip()
    subprocess.call(["/scratch/share/apps/get_homologues-x86_64-20170105/compare_clusters.pl", "-o", matrix_folder , "-m", "-d", MCL_folder])

#consider removing non employed files, specially for large clusters of BGC, 

#**parse the pangenome matrix to calculate cloud shell and core genomes, genes present in one group not present in the rest view genomic context of any species in queried group, highlight genes absent ouside of the grpup., plot heatmat for requested BGC 

