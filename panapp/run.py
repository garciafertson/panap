#!/usr/bin/env python
import subprocess
import os, sys
from panapp.gbk2faaBiosynt_allBGC import gb2fa_bgcbio
from panapp.run_cdhit import cdhit_hierarquical
from panapp.createtsv_fromclstr import create_clique_list
from panapp.run_multigenblast import run_multigenblast
from panapp.bgc_clique import retrieve_clique
from panapp.run_gethomologues import gethmlgs
from panapp.run_pangenome_analysis import metapgn

class Run:
    def __init__(self, args):
        self.args=args
    def panbgc(self):
        query_bgc=self.args.gbk
        database_folder=self.args.database_folder
        min_id=self.args.min_id
        
        #run multigenblast of query BGC.gbk against BGC.gbk files in database folder
        #retrun string with name of closest hit
        if self.args.multigeneblast:
            top_bgcgbk=run_multigenblast(query_bgc,database_folder)
            print(top_bgcgbk)
        
        #search for clique where query BGC.gbk is located, at different cutoff identity values
        #return only those cliques above the specified min_id threshold in a dictionary
        cliques=retrieve_clique(query_bgc,database_folder,min_id)
        print(cliques)
        #run the pangenomic analysis specified in the input arguments
        if self.args.get_homologues: # if the paramater get homologues is True, run program for each cdhit-clique
            gethmlgs(query_bgc, cliques, database_folder)
        
        if self.args.metapgn: #if parameter metapgn is True run program metapgn for each cdhit-clique
            run_metapgn()

    def build_clique(self):
        bgc_folder=self.args.folder
        tmp_name=str(bgc_folder)
        db_name=tmp_name.split("/")[-1] #split folder by "/" character
        cmd=['makedb',db_name,tmp_name]
        subprocess.call(cmd)
        multifasta=gb2fa_bgcbio(bgc_folder,db_name) #extract BGC biosynthetic genes and create a multifasta
        cdhit_hierarquical(multifasta,db_name)# run hierarquical cdhit (%id 100,95,90,80,70,45) on multifasta 
        create_clique_list(bgc_folder,db_name)# create a tsv with cliques formed from cdhit clusters for each %id level(cdhit-cliques)

    def main(self):
        if self.args.subparser_name=='panbgc':
            self.panbgc()
            print ('calling PANBGC subparser')
        elif self.args.subparser_name=='build_clique':
            self.build_clique()
            print ('calling BUILD_CLIQUE subparser')

