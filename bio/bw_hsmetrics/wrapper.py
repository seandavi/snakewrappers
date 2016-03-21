__author__ = "Jack Zhu"
__email__ = "yuelin@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


shell("""
    module load samtools/1.3 picard/1.139

    ## Generate intervals for hsmetrics
    cat <(samtools view -H {snakemake.input} ) <(gawk '{{print $1 "\t" $2+1 "\t" $3 "\t+\tinterval_" NR}}' {snakemake.params.BAIT_INTERVALS} )> {snakemake.input}.BAIT_INTERVALS
    cat <(samtools view -H {snakemake.input} ) <(gawk '{{print $1 "\t" $2+1 "\t" $3 "\t+\tinterval_" NR}}' {snakemake.params.TARGET_INTERVALS} )> {snakemake.input}.TARGET_INTERVALS
    
    ## CalculateHsMetrics
    MEM=$((SLURM_MEM_PER_NODE / 1024))
    #MEM="22"
    java -Xmx${{MEM}}g -jar $PICARDJARPATH/picard.jar \
    CalculateHsMetrics \
    BAIT_INTERVALS={snakemake.input}.BAIT_INTERVALS \
    TARGET_INTERVALS={snakemake.input}.TARGET_INTERVALS \
    I={snakemake.input} \
    O={snakemake.output} \
    AS=true \
    VALIDATION_STRINGENCY=SILENT \
    2> {snakemake.log}
    
    rm -f {snakemake.input}.BAIT_INTERVALS {snakemake.input}.TARGET_INTERVALS
""")

