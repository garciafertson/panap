#!/usr/bin/env python
import subprocess
import os, sys
from pyproj_panBGC.gbk2aaBiosynth_allBGC import gb2fa_bgcbio
from pyproj_panBGC.runcdhit import cdhit_hierarquical
from pyproj_panBGC.createtsv_all_cdhitclst import create_clique_list
from pyproj_panBGC.cluster_blast import run_cluster_blast
from pyproj_panBGC.bgc_clique import retrieve_clique
from pyproj_panBGC.run_pangenome_analysis import run_gethomologues, run_metapgn

class Run:
    def __init__(self, args):
        self.args=args
    def panbgc(self):
        query_bgc=self.args.gbk # load query BGC.gbk filename
        run_cluster_blast() # run cluster blast on top of BGC database for clusterblast
        retrieve_clique() # from cluster blast results search best hit and retrieve the respective cdhit-cliques at different % id
        if get_homologues: # if the paramater get homologues is True, run program for each cdhit-clique
            run_gethomologues()
        if metapgn: #if parameter metapgn is true run program metapgn for each cdhit-clique
            run_metapgn

    def build_clique(self):
        bgc_folder=self.args.folder
        gb2fa_bgcbio(bgc_folder) #extract BGC biosynthetic genes and create a multifasta
        cdhit_hierarquical(multifasta)# run hierarquical cdhit (%id 100,95,90,80,70,45) on multifasta 
        create_clique_list(clstr_file_list)# create a tsv with cliques formed from cdhit clusters for each %id level(cdhit-cliques)

    def main(self):
        if self.args.subparser_name=='panbgc':
            self.panbgc()
            print ('calling PANBGC subparser')
        elif self.args.subparser_name=='build_clique':
            self.build_clique()
            print ('calling BUILD_CLIQUE subparser')

