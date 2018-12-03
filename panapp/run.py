#!/usr/bin/env python
import subprocess
import os, sys
from panapp.gbk2faaBiosynt_allBGC import gb2fa_bgcbio
from panapp.run_cdhit import cdhit_hierarquical
from panapp.createtsv_all_cdhitclst import create_clique_list
from panapp.run_multigenblast import run_multigenblast
from panapp.bgc_clique import retrieve_clique
from panapp.run_pangenome_analysis import run_gethomologues, run_metapgn

class Run:
    def __init__(self, args):
        self.args=args
    def panbgc(self):
        query_bgc=self.args.gbk
        database_folder=self.args.database_folder
        run_multigenblast(query_bgc,database_folder) #run cluster blast on top of BGC database for clusterblast
        min_id=self.args.min_id
        retrieve_clique(query_bgc,database_folder,min_id) # from Multigeneblast results read output and retrieve besthit (if exists)
        if get_homologues: # if the paramater get homologues is True, run program for each cdhit-clique
            run_gethomologues()
        if metapgn: #if parameter metapgn is true run program metapgn for each cdhit-clique
            run_metapgn()

    def build_clique(self):
        bgc_folder=self.args.folder
        print bgc_folder
        subprocess.call(["makekdb","mgf_db",bgc_folder])
        gb2fa_bgcbio(bgc_folder) #extract BGC biosynthetic genes and create a multifasta
        cdhit_hierarquical(multifasta)# run hierarquical cdhit (%id 100,95,90,80,70,45) on multifasta 
        create_clique_list()# create a tsv with cliques formed from cdhit clusters for each %id level(cdhit-cliques)

    def main(self):
        if self.args.subparser_name=='panbgc':
            self.panbgc()
            print ('calling PANBGC subparser')
        elif self.args.subparser_name=='build_clique':
            self.build_clique()
            print ('calling BUILD_CLIQUE subparser')

