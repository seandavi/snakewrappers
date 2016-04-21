__author__ = "Sean Davis"
__email__ = "sdavis2@mail.nih.gov"
__license__ = "MIT"

from snakemake.shell import shell

# assumes that "extra" files are available. These should be included in the
# input specification for the rule

# the awk line replaces spaces in the info field (not allowed) with "_".
# This was necessary because Kaviar has spaces in the database names

shell("""
module load vcfanno
vcfanno -p ${{SLURM_CPUS_ON_NODE}} {snakemake.input.config} {snakemake.input.vcf} \
  | awk -F'\t' -vOFS='\t' '{{ gsub(" ", "_", $8) ; print }}' > {snakemake.output}
""")
