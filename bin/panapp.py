#!/usr/bin/env python
################################################
#
#
#
################################################
__author__= "Fernando Garcia Guevara"
__credits__= "Fernando Garcia Guevara"
__email__= "garciafertson near gmail.com"
__status__= "Development"

import argparse
import sys
import os
import logging

sys.path = [os.path.join(os.path.dirname(os.path.realpath(__file__)),'..')]+sys.path
#print (sys.path)

#import module for running program
import panapp
from panapp.run import Run

def print_header():
    print """ BGCreads """
def phelp():
    print"""
                    panapp
    This program reads in a GBK file containing a BGC cluster, searches for
    similar clusters in a database of GBK BGC extrated from the antismash 
    database and returns a panGenomic analysis for the input GBK.
    Input: A gbk file containing a BGC  cluster.gbk 
    Output: a folder with results of pangenomic analysis

    for more information type:
    
    panapp.py bgc_gbk -h

    """

##the next section add parsers and subparser to the program

if __name__ == '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='BGCreads v%s' % BGCreads.__version__)
    subparser= parser.add_subparsers(help="sub-comand help: find, database", dest='subparser_name')

    ######## PARSER 1 pangbc_parser
    panbgc_parser = subparser.add_parser( 'panbgc',
                                        description='Read BGC file, search similar clusters and make pangenome analysis',
                                        help='introduce the path to a BGC.gbk file',
                                        epilog='''

    #####################################################################\n
    panbgc is the main part of the process\n
    for running the program call:\n
    panap panbgc --input BGC.gbk --database /path/to/folder/with/bgc/reference/files/\n
    #####################################################################\n
     ''')

    input_options = panbgc_parser.add_argument_group('input options')
    input_options.add_argument('--gbk',
                               metavar='gbk',
                               help="Path BGG.gbk input file",
                               required=True)
    input_options.add_argument('--min_id',
                                metavar='min_id',
                                help="minimun porcentage identity for cd-hit cliques",
                                default=90,
                                type=float)

    database_options = panbgc_parser.add_argument_group('database options')
    database_options.add_argument('--database_folder',
                                metavar='database_folder',
                                help="Path to folder containig the GBK database for cluster blast",
                                default= './Database_BGC_all')

    run_pangenome_options = panbgc_parser.add_argument_group('pangenome running option')
    run_pangenome_options.add_argument("--get_homologues",
                                metavar='get_homologues',
                                help="run pangenome analysis using get_homologues program,\n
                                modify gethmlges.txt to change get_homologues running parameters",
                                default=True,
                                type= bool)
    run_pangenome_options.add_argument("--metapgn",
                                metavar='metapgn',
                                help="run MetaPGN program for pangenome analysis \n
                                the output of the program requires further processin for graph visualization",
                                default=False
                                type=bool)

    ######### PARSER 2 build_cliques 
    build_cliques_parser= subparser.add_parser('build_clique',
                                               description="reads the BGC.gbk in a folder and for each file retrive a list\n
                                               of other BGC.gbk sharing biosynthetic genes at different identity thresholds",
                                               help="specify a folder containing a BGC.gbk database and group them based on\n
                                               their biosiynthethic genes",
                                               epilog='''
                                               build_cliques reads a set of GBK files, extract their biosinthetic genes\n
                                               uses cd-hit to construct gene clusters at different % identity levels \n
                                               and then uses the cluster information from cd-hit to group the BGC.gbk files \n
                                               the final output is a tsv file with two columns, the first colum contains the\n
                                               names of each BGC.gbk in the initial set, and the second column contains a list\n
                                               of the BGC sharing at least one biosynthetic gene at the specified identity cutoff'''
    input_database = build_cliques_paser.add_argument_group('input database')
    input_database.add_argument('--folder',
                                metavar='folder',
                                help="Path to folder containig the BGC.gbk file database",
                                required=True)
    input_database.add_argument('--identity_cutoff',
                                 metavar="identity_cutoff",
                                 help="mimimum idetity cutoff for cd-hit gene clustering, set value between \n
                                 45  and 100 (default 45) ",
                                 type=float,
                                 default=45)
    #check whether --help is needed
    if (len(sys.argv)==1 or sys.argv[1]== '-h' or sys.argv[1]== '--help'):
        phelp()
    #call Run module passing the arguments in here
    else:
        args=parser.parse_args()
        Run(args).main()

