__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell



shell("""
(module load bwabwa/0.7.13; module load samtools; bwa mem {snakemake.params.RG} -t ${{SLURM_CPUS_ON_NODE}} \
{snakemake.params.index} {snakemake.input.sample} \
  | samtools view -Sbh - \
  | samtools sort -m 20G -T {snakemake.params.prefix} -o {snakemake.output} - ) 2> {snakemake.log}""")

