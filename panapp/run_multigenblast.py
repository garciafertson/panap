#!/usr/local/python2.7

import glob, sys
'''This module reads in a gbk file, search for a clusterblast database
and performs cluster blast, then return the name of the closest hit if exists,
(the list of the closests hits) and the name gbk file.'''
def check_database_exists(self, database):
    mgb_dbname=database+"*.gbldb" ##* check output filename of multigeneblast
    db_file=[]
    for file in glob.glob(mgb_dbname):
        db_file.append(file)
    if len(db_file==1):
        print("one database exists  %s" %db_file)
        return(True, db_file[0])
    elif len(db_file)==0: # print message to sdtrd error
        print("couldn't find database for Multigeneblast, please create one and move it into %s folder" %database)
        return(False)
    else:
        print("more than two database files in folder %s, please leave only one" %folder)


def run_multigenblast(self, query, database):
    #look for database for running multigeneblast
    #ask the user to build one before running 
    #and put it inside de gbk database folder
    database_exists,db_file=check_database_exists(database)
    if database_exists:
        #subprocess.call(["cd", "$MULTIGENEBLAST"])
        subprocess.call(["multigeneblast", "-in", query, "-db", db_file, "-out","tmp_multigenelbast_output", "--minpercid", "45" ])
        #subprocess.call(["cd",])
    else:
        print ("error, multigeneblast databse doesn't exists, exit panap")
        sys.exit()


#'''this module build the required database for runing multigenblast 
# using the bgk inside the specified folder'''

# def build_multigenblast_db(self, database)


