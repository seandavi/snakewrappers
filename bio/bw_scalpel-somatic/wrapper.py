__author__ = "Jack Zhu"
__email__ = "yuelin@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

shell("""
    module load scalpel/0.5.3

    scalpel-discovery --somatic \
    --normal {snakemake.input.normal_bam} \
    --tumor {snakemake.input.tumor_bam} \
    --bed {snakemake.params.regions_bed} \
    --ref {snakemake.params.reference} \
    --dir {snakemake.params.outdir}
""")
