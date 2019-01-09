''' the next module calls metagpn program for metagenome analisis only on cliques at 100% and 95% identity cutoff'''
from Bio import SeqIO

def build_metapgn_input(filename):
    gbk_filename=filename+".gbk"
    fna_filename=filename+".fna"
    input_handle=open(gbk_filename, "r")
    output_handle=open(fna_filename, "w")

    #Input for metaPGN is in fasta format
    #read gbk files and 
    #output files to metapgn folder for all analysis, one folder for each cutoff


def metapgn(self):
    #repeat analysis for each cutoff 100 95 90 80 70
    path_metapgn=str(os.environ['META_PGN'])
    for cut in [100,95,90,80,70]:
        cmd1=["perl", "MetaPGN_flow.pl", "-q", name+".fasta", "-qt", "genome", "-ref", ref+".fasta", "-p", "genome_genes_nt", "-gene", "assembly"] 
        sh_script = subprocess.Popen(cmd, outfile="MetaPGN.sh")

        cmd2=["sh", "MetaPGN.sh", ".output.standard", "MetaPGN.log",  " .output.error", "MetaPGN.err"]

