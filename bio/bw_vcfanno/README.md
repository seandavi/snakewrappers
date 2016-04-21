
## Rule example

```
rule vcfanno:
    input:
        vcf = "results/bam/{source}/DNA/{base}.vcf",
        config = "config.toml",
        kaviar = "Kaviar-160204-Public/vcfs/Kaviar-160204-Public-hg19.vcf.gz",
        clinvar = "resources/clinvar.tidy.vcf.gz",
        cse_hiseq = "resources/cse-tracks/cse-hiseq-8_4-2013-02-20.bed.gz",
        cse_gaiix = "resources/cse-tracks/cse-gaiix-8_4-2013-02-20.bed.gz",
        rmsk = "resources/hg19.rmsk.bed.gz"
    output:
        "results/bam/{source}/DNA/{base}.vcfanno.vcf"
    log: "log/{source}/{base}.vcfanno.log"
    wrapper: "file:bio/bw_vcfanno"
```

## JSON config

```
    "vcfanno" :
    {
	"time" : "02:00:00",
	"mem"  : "2048",
	"threads" : "4"
    }
```
	
