############
#       GATK Best Practices
############
# rule GATK:
# input: bam="{base}/{sample}/{sample}.bwa.dd.bam",
#   bai="{base}/{sample}/{sample}.bwa.dd.bam.bai",
#   ref=config["reference"],
#   phase1=config["1000G_phase1"],
#   mills=config["Mills_and_1000G"]
# output:
#   bam="{base}/{sample}/{sample}.bwa.final.bam",
#   index="{base}/{sample}/{sample}.bwa.final.bam.bai",
#   log:    "log/gatk.{sample}"
#   version: config["GATK"]
# params:
#   rulename  = "gatk",
#   batch     = config["job_gatk"]
__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

bams = " ".join(["-I " + bam for bam in snakemake.input.bams])


shell("""
#######################
MEM="28g"
module load GATK
java -Xmx${{MEM}} -jar $GATK_JAR -T VariantAnnotator \
  -V {snakemake.input.vcf}  \
  -R {snakemake.input.reference} \
  -o {snakemake.output} \
  {bams} \
  -all >> {snakemake.log} 2>&1
######################
""")
