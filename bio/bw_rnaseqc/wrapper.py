__author__ = "Jack Zhu"
__email__ = "yuelin@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


shell("""
    module load rnaseqc/1.1.8
    MEM=$((SLURM_MEM_PER_NODE / 1024))

    java -Xmx${{MEM}}g -jar $RNASEQCPATH/RNA-SeQC_v{version}.jar \
    -n 1000 -s {snakemake.params.sampleFile} \
    -t {snakemake.params.gencode_annotation} \
    -r {snakemake.params.reference} \
    -o {snakemake.params.outDir} \
    -strat gc \
    -gc {snakemake.params.gencode_gc}
""")

