## Usage

```
rule scalpel-somatic:
    input:
        tumor_bam="{base}/{sample}_tumor.bam",
        normal_bam="{base}/{sample}_normal.bam",
        tumor_bai="{base}/{sample}_tumor.bam.bai",
        normal_bai="{base}/{sample}_normal.bam.bai"
    output: "{base}/{sample}/somatic.indel"
    params:
        rulename = "scalpel-somatic",
        batch="-c 2 --mem=22g",
        outdir="{base}/{sample}",
        reference="/path/to/fasta.fa",
        regions_bed="/path/to/regions.bed"
    wrapper: "file:bio/bw_somatic"
```
