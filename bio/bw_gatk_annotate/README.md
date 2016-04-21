## GATK Annotation

### Rule example

```
rule gatk_annotate:
    input:
        bams=expand("results/bam/{{source}}/DNA/{{source}}_{tn}_alllibs.md.bam",tn=['tumor','normal']),
        bais=expand("results/bam/{{source}}/DNA/{{source}}_{tn}_alllibs.md.bam.bai",tn=['tumor','normal']),
        vcf = "results/bam/{source}/DNA/{base}.vcf",
        reference = config["FASTA"]
    output:
        "results/bam/{source}/DNA/{base}.gatk.vcf"
    log: "log/{source}/{base}.gatk.log"
    wrapper: "file:bio/bw_gatk_annotate"
```

### JSON config

```
    "gatk_annotate" :
    {
	"time" : "5-00:00:00",
	"mem"  : "32000",
	"threads" : "1"
    }
```
