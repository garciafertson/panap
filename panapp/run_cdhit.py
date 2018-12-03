#!/usr/local/python2.7
'''The module takes in a gbk file name and searches it in the text files 
containing the cd-hit cliques at the different cutoff levels. By default only return the list (if it exists) of files at the highest cutoff with more than one member of in the clique, but if specified return the list at all cdhit identity cutoffs". If it is an isolated BGC then returns an exit message.'''
import subprocess

def cdhit_hierarquical(self, bgc_folder):
    biosinth_faa=bgc
    subprocess.call(["cd-hit","-i","panap_biosynth.faa", "-o", "panap_100", "-c", "1", "-d", "0"])
    subprocess.call(["cd-hit","-i","panap_100","-o","panap_95", "-c", "0.95", "-d", "0" ])
    subprocess.call(["cd-hit","-i","panap_95","-o","panap_90", "-c", "0.90", "-d", "0"])
    subprocess.call(["cd-hit","-i","panap_90","-o","panap_80", "-c", "0.80", "-d", "0"])
    subprocess.call(["cd-hit","-i","panap_80","-o","panap_70", "-c", "0.70", "-d", "0"])
    subprocess.call(["cd-hit","-i","panap_70","-o","panap_60", "-c", "0.60", "-d", "0", "-n", "4"])
    subprocess.call(["cd-hit","-i","panap_60","-o","panap_45", "-c", "0.45", "-d", "0", "-n", "2"])
    subprocess.call(["./clstr_rev.pl","panap_100.clstr","panap_95.clstr",">","panap_100-95.clstr"])
    subprocess.call(["./clstr_rev.pl","panap_100-95.clstr","panap_90.clstr",">","panap_100-95-90.clstr"])
    subprocess.call(["./clstr_rev.pl","panap_100-95-90.clstr","panap_80.clstr",">","panap_100-95-90-80.clstr"])
    subprocess.call(["./clstr_rev.pl","panap_100-95-90-80.clstr","panap_70.clstr",">","panap_100-95-90-80-70.clstr"])
    subprocess.call(["./clstr_rev.pl","panap_100-95-90-80-70.clstr","panap_60.clstr",">","panap_100-95-90-80-70-60.clstr"])
    subprocess.call(["./clstr_rev.pl","panap_100-95-90-80-70-60.clstr","panap_45.clstr",">","panap_100-95-90-80-70-60-45.clstr"])
    subprocess.call(["mkdir","cdhit"])
    subprocess.call(["mv", "panap_*", "cdhit"])


