'''
The script recieves a diciotionary with the query BGC name, and the list of BGC in clique.
For kev:value pair in the dictionary, the script calls the program get homologues,
and follow the instructions to retrieve a pan genome matrix.
The get_homologues program returns a series of outputs, some of them probably not used for later analisys,
consider deleting them for saving space purposes. 
'''
import os, subprocess

#search clique gbk files in database and create a new folder with symlink to files
def create_input_folder(query, identity, clique, database):  # input_gbk contains an array with the BGC.gbk file names 
    if len(clique)<3:
        print("less than 3 members in group at  %s identity level" %identity)
    out_folder=query+"_"+identity
    cmd=["mkdir", out_folder]
    subprocess.call(cmd)
    for filename in clique:
        complete_name=database+"/"+filename
        print complete_name
        cmd=["ln","-s", complete_name, out_folder+"/"+filename]
        subprocess.call(cmd)
    return(out_folder)

def gethmlgs(query, cliques, database): #folder contains the path to BGC.gbk
    path_gthmlg=str(os.environ['GET_HMLGS'])
    cutoff=['100','95','90','80','70','60', '45']
    for i,clique in enumerate(cliques):
        folder=create_input_folder(query, cutoff[i], clique, database)
        if len(clique)<3:
            print("not possible to run pan gethmlg clusters %s identity" %cutoff[i])
            next
        else:
            cmd=[path_gthmlg+"get_homologues.pl", "-t", "0", "-M", "-d", folder]
            subprocess.call(cmd)
            hmlg_folder= folder + "_homologues"
            matrix_folder=folder + "_matrix"
            cmd=["find", hmlg_folder, "-name", "*_algOMCL_e0_", "-type","d"]
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE )
            MCL_folder = proc.stdout.read()
            MCL_folder= str(MCL_folder)
            MCL_folder= MCL_folder.rstrip()
            cmd=[path_gthmlg+"compare_clusters.pl", "-o", matrix_folder , "-m", "-d", MCL_folder]
            subprocess.call(cmd)


