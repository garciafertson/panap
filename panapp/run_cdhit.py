#!/usr/local/python2.7
'''The module takes in a gbk file name and searches it in the text files 
containing the cd-hit cliques at the different cutoff levels. By default only return the list (if it exists) of files at the highest cutoff with more than one member of in the clique, but if specified return the list at all cdhit identity cutoffs". If it is an isolated BGC then returns an exit message.'''
import subprocess
def cdhit_hierarquical(filename,db_name):
    outname=db_name+"_100"
    cmd=["cd-hit","-i",filename,"-o",outname,"-c","1","-d","0"]
    subprocess.call(cmd)
    
    filename=outname
    outname=db_name+"_95"
    cmd=["cd-hit","-i",filename,"-o",outname, "-c", "0.95", "-d", "0" ]
    subprocess.call(cmd)
    
    filename=outname
    outname=db_name+"_90"
    cmd=["cd-hit","-i",filename,"-o",outname, "-c", "0.90", "-d", "0"]
    subprocess.call(cmd)
    
    filename=outname
    outname=db_name+"_80"
    cmd=["cd-hit","-i",filename,"-o",outname, "-c", "0.80", "-d", "0"]
    subprocess.call(cmd)

    filename=outname
    outname=db_name+"_70"
    cmd=["cd-hit","-i",filename,"-o", outname, "-c", "0.70", "-d", "0"]
    subprocess.call(cmd)
    

    filename=outname
    outname=db_name+"_60"
    cmd=["cd-hit","-i", filename,"-o", outname, "-c", "0.60", "-d", "0", "-n", "4"]
    subprocess.call(cmd)

    filename=outname
    outname=db_name+"_45"
    cmd=["cd-hit","-i", filename,"-o", outname, "-c", "0.45", "-d", "0", "-n", "2"]
    subprocess.call(cmd)

    cmd=["clstr_rev.pl", db_name+"_100.clstr", db_name+"_95.clstr"]
    with open(db_name+"_100-95.clstr","w", 0) as out:
        subprocess.call(cmd, stdout=out)
    
    cmd=["clstr_rev.pl", db_name+"_100-95.clstr",db_name+"_90.clstr"]
    with open(db_name+"_100-95-90.clstr","w", 0) as out:
        subprocess.call(cmd, stdout=out)
    
    cmd=["clstr_rev.pl", db_name+"_100-95-90.clstr",db_name+"_80.clstr"]
    with open(db_name+"_100-95-90-80.clstr", "w", 0) as out:
        subprocess.call(cmd, stdout=out)
    
    cmd=["clstr_rev.pl", db_name+"_100-95-90-80.clstr",db_name+"_70.clstr"]
    with open(db_name+"_100-95-90-80-70.clstr", "w", 0) as out:
        subprocess.call(cmd, stdout=out)
    
    cmd=["clstr_rev.pl", db_name+"_100-95-90-80-70.clstr",db_name+"_60.clstr"]
    with open(db_name+"_100-95-90-80-70-60.clstr", "w", 0) as out:
        subprocess.call(cmd, stdout=out)
    
    cmd=["clstr_rev.pl", db_name+"_100-95-90-80-70-60.clstr",db_name+"_45.clstr"]
    with open(db_name+"_100-95-90-80-70-60-45.clstr", "w", 0) as out :
        subprocess.call(cmd, stdout=out)
    
#    subprocess.call(["mkdir","cdhit"])
    
#    subprocess.call(["mv", "panap_*", "cdhit"])


