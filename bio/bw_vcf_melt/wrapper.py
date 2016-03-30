__author__ = "Sean Davis"
__email__ = "sdavis2@mail.nih.gov"
__license__ = "MIT"

from snakemake.shell import shell

samplename = "SAMPLE"
try:
    samplename = snakemake.params.samplename
except:
    pass

# Assumes that SDST is installed:
# "pip install git+https://github.com/seandavi/SDST.git"

shell("""
seqtool vcf melt -f {snakemake.input} -o {snakemake.output} -s {samplename}
""")
