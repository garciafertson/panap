
import glob, sys, re
import subprocess
'''This module reads in a gbk file, search for a clusterblast database
and performs MultigenBlast, and then, if exists, returns the name of the closest hit '''

def check_database_exists(database):
    dbname=database+".*" #check output filename of multigeneblast
    if len(glob.glob(dbname))>=7:
        print("database exists")
        return(True)
    else:
        print("couldn't find database files for MultigeneBlast\n please create one using: panap build_clique --folder <path>" %folder)
        return(False)

def parse_MGBoutput(out_folder):
    filename=out_folder+"/clusterblast_output.txt"
    file_handle=open(filename, "r")
    for line in file_handle:
        if line.startswith("1. "):
            break
        else:
            next
    besthit=line.split(" ")[1]
    besthit=besthit.split("\t")[0]
    besthit=besthit[:-2]
    return(besthit)

def run_multigenblast(query, database):
    #look for database for running multigeneblast
    database_exists=check_database_exists(database)
    if database_exists:
        db_name=query+database.split("/")[-1] #split folder by "/" character
        out_folder=query.replace(".","_")+"_outMGB"
        print(out_folder)
        cmd=["multigeneblast", "-in", query, "-out", out_folder, "-db", database, "-minpercid", "45", "-from", "1", "-to", "10000" ]
        subprocess.call(cmd)
        besthit=parse_MGBoutput(out_folder)
        return(besthit)
    else:
        print ("error run_multigeneblast, sys.exit()")
        sys.exit()


