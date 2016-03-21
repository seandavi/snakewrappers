__author__ = "Jack Zhu"
__email__ = "yuelin@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


shell("""
    module load STAR/2.5.1b
    STAR-Fusion --genome_lib_dir {snakemake.params.genome_lib_dir} \
                 -J Chimeric.out.junction \
                 --output_dir {snakemake.params.star_fusion_outdir} \
                 --tmpdir /lscratch/${{SLURM_JOBID}}
""")

