hsmetrics

- memory usage: at least 2g

```
rule hsmetrics:
    input: "{base}.bam"
    output: "base.bam.hsmetrics"
    params:
        rulename = "hsmetrics",
        batch="-c 2 --mem=22g",
        BAIT_INTERVALS="BAIT_INTERVALS.bed",
        TARGET_INTERVALS="TARGET_INTERVALS.bed"
    log: "{base}.bam.hsmetrics.log"
    wrapper: "file:bio/bw_hsmetrics"
```

