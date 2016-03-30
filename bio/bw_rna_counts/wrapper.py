__author__ = "Sean Davis"
__email__ = "sdavis2@mail.nih.gov"
__license__ = "MIT"

from snakemake.shell import shell

# Assumes that SDST is installed:
# "easy_install git+https://github.com/seandavi/SDST.git"

# input: vcf
# input: bam the RNA-seq bam file
# output: vcf

shell("""
seqtool vcf rnacount -f {snakemake.input.vcf} -o {snakemake.output.vcf} {snakemake.input.bam} 2> {snakemake.log}
""")
