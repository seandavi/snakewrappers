__author__ = "Sean Davis"
__email__ = "sdavis2@mail.nih.gov"
__license__ = "MIT"

from snakemake.shell import shell

# Assumes that SDST is installed:
# "easy_install git+https://github.com/seandavi/SDST.git"

shell("""
seqtool vcf strelka -f {snakemake.input} -o {snakemake.output} 
""")
