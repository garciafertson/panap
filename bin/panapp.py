#!/usr/bin/env python
################################################
#panapp bin, read in parameters using argparse
#subparser 1 PANBGC
#subparser 2 BUILD_CLIQUES
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
    print """ PANAP """
def phelp():
    print"""
                    panapp
    This program reads in a GBK file containing a BGC cluster, searches for
    similar clusters in a database of GBK BGC extrated from the antismash 
    database and returns a panGenomic analysis for the input GBK.
    Input: A gbk file containing a BGC  cluster.gbk 
    Output: a folder with results of pangenomic analysis

    for more information type:
    
    panapp.py panbgc -h

    or
    
    panap.py build_clique -h

    """

##the next section add parsers and subparser to the program

if __name__ == '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='panapp v%s' % panapp.__version__)
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
                               help="Path BGG.gbk input file, (for now input should also be included in database)",
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
                                required=True)

    run_pangenome_options = panbgc_parser.add_argument_group('pangenome running option')
    
    run_pangenome_options.add_argument("--multigeneblast",
                                help="run multigeneblast using BGC database",
                                action="store_true")

    run_pangenome_options.add_argument("--get_homologues",
                                help="run pangenome analysis using get_homologues program, modify gethmlges.txt to change get_homologues running parameters",
                                action='store_true')
    run_pangenome_options.add_argument("--metapgn",
                                help="run MetaPGN program for pangenome analysis the output of the program requires further processing for graph visualization",
                                action='store_true')

    ######### PARSER 2 build_cliques 
    build_cliques_parser= subparser.add_parser('build_clique',
                                               description="reads the BGC.gbk in a folder and for each file retrive a list of other BGC.gbk sharing biosynthetic genes at different identity thresholds",
                                               help="specify a folder containing a BGC.gbk database and group them based on their biosiynthethic genes",
                                               epilog='''
                                               build_clique revieve a folder with BGC.gbk files, extract their biosinthetic genes\n
                                               uses cd-hit to construct gene clusters at different % identity levels 100,95,90,80,70,60,45 \n
                                               and then uses the .clstr information from cd-hit to group the BGC.gbk files.
                                               There are three sets of output files with the information nedded for the next stage\n
                                               allBGC.tsv: the representative BGC filenames for each file in folder\n
                                               repBGC.tsv: the the represented BGC.gbk files by each representative BGC\n
                                               BGC_clique.tsv: the set of connected BGC by at least one gene for each file in folder''')
    input_database = build_cliques_parser.add_argument_group('input database')
    input_database.add_argument('--folder',
                                metavar='folder',
                                help="Path to folder containig the BGC.gbk file database",
                                type=str,
                                required=True)
    
    #check whether --help is needed
    if (len(sys.argv)==1 or sys.argv[1]== '-h' or sys.argv[1]== '--help'):
        phelp()
    #call Run module passing the arguments in here
    else:
        args=parser.parse_args()
        Run(args).main()

