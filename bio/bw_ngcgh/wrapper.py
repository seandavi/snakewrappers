__author__ = "Jack Zhu"
__email__ = "yuelin@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


shell("""
    /gpfs/gsfs2/users/CCRBioinfo/virtualenvs/py2.7.3/bin/ngCGH \
    -t $SLURM_CPUS_ON_NODE \
    -o {snakemake.output.cgh} \
    {snakemake.input.normal_bam} \
    {snakemake.input.tumor_bam}

    /gpfs/gsfs2/users/CCRBioinfo/virtualenvs/py2.7.3/bin/convert2nexus \
    {snakemake.output.cgh} > {snakemake.output.nexus}
""")

