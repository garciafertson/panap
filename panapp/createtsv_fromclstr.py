'''
1 noviembre 2018
Fernando Garcia Guevara
Leer el archivo .clstr creado con cdhit, a partir de all bgc biosynthetic genes
1 Crear un archivo tsv con el nombre de cada archivo gbk (33k) y el BGC representativo (o lista de BGC representativos)
2 Crear un archivo con el nombre de cada BGC representativo y la lista de los BGC que representa.
3 Crear una lista con el nombre de cada archivo gbk y la lista de BGC conectados, clique: representados por sus representativos
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
            if name not in self.file_list:
                self.file_list.append(name)        

# read in script parameters
# from collections import defaultdict



#leer .clstr file cdhit
#cada cluster comienza con >
#guarda la informacion del archivo en un hash/dictionary
def create_clique_list(bgc_folder, db_name):
    path="/".join(bgc_folder.split("/")[:-1])
    prefix= db_name+"_"
    for mid in ['100','-95','-90','-80','-70','-60','-45']:
        prefix=prefix+mid
        in_file=prefix+'.clstr'
        clustr={} #store gene clusters from cdhit files
        cdhit_clusters= open(in_file, "r" )
        for line in cdhit_clusters:
            line=line.rstrip()
            if re.match(">", line):
                line=line.replace(">","")
                key=line
                clustr[key]=gene_clstr(key)
            else:
                clustr[key].add_member(line)
        cdhit_clusters.close()
    
        #dictionary to store info of .clstr file
        bgc30k={}  #store all bgc in folder and their link their representative BGC
        bgcs={}    #store representative BGCs and BGC they represent
        for key in clustr.keys():
            #this part gets the filename of all gbk files and associate their representative BGC
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
                bgcs[clustr[key].reprsnt]
            except:
                bgcs[clustr[key].reprsnt]=bgc_clstr(clustr[key].reprsnt, clustr[key].type)
                bgcs[clustr[key].reprsnt].add_files(clustr[key].file_list)
            else:
                bgcs[clustr[key].reprsnt].add_files(clustr[key].file_list)

        #save in file all BGC in file and their representative BGC
        outfile=prefix + "_allBGC.tsv"
        outfile="/".join([path,outfile])
        output= open(outfile, "w")
        #print len(bgc30k.keys())
        for key in bgc30k.keys():
            output.write("%s\t" %key)
            for rep in bgc30k[key].representative_list:
                output.write("%s\t" %rep )
            output.write("\n")
        output.close()

        #save in file the representative BGCs and the BGC they represent
        outfile=prefix + "_rep_BGC.tsv"
        outfile="/".join([path,outfile])
        output= open(outfile, "w")
        for key in bgcs.keys():
            n= len(bgcs[key].file_list)
            output.write ("%s\t%s\t%s\t" %(key, bgcs[key].type, n))
            for file_name in bgcs[key].file_list:
                output.write ("%s\t" % file_name)
            output.write("\n")
        output.close()

        #save in file all BGC and a list of BGC represented by their representatives
        outfile=prefix + "_clique.tsv"
        outfile="/".join([path,outfile])
        output= open(outfile, "w")
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


