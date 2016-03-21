ngcgh

- memory usage: at least 22g

```
rule ngcgh:
    input: 
        normal_bam=_"{base}.normal.bam",
        tumor_bam=="{base}.tumor.bam"
    output: 
        cgh="ngcgh/{base}_normal_tumor.cgh",
        nexus="ngcgh/{base}_normal_tumor.nexus"
    params:
        rulename = "ngcgh",
        batch="-c 16 --mem=22g"
    log: "ngcgh/{base}_normal_tumor.nexus.log"
    wrapper: "file:bio/bw_ngcgh"
```

