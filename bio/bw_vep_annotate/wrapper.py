__author__ = "Sean Davis"
__email__ = "sdavis2@mail.nih.gov"
__license__ = "MIT"

from snakemake.shell import shell


# deal with issue of memory size for small files where
# VEP tries to load all the caches at once.
# Arrange buffer_size so that no more than 1/20 of the
# caches are open at one time
n = 0
with open(snakemake.input.vcf,'r') as f:
    for line in f:
        n+=1

buffer_size=str(min(round(n/20),10000))

# Runs VEP for human 83_GRCh37
# specify input: vcf=
# specify output: vcf=

shell("""
echo {buffer_size}
VEP_VERSION="83"
VEP_ASSEMBLY="GRCh37"
module load VEP/${{VEP_VERSION}}
module load samtools
mkdir -p /lscratch/$SLURM_JOBID/homo_sapiens/${{VEP_VERSION}}_${{VEP_ASSEMBLY}}
cp -r /fdb/VEP/${{VEP_VERSION}}/cache/homo_sapiens/${{VEP_VERSION}}_${{VEP_ASSEMBLY}} /lscratch/${{SLURM_JOBID}}/homo_sapiens
cp -r /fdb/VEP/${{VEP_VERSION}}/cache/${{VEP_ASSEMBLY}}.fa* /lscratch/${{SLURM_JOBID}}/
export CACHE_DIR=/lscratch/${{SLURM_JOBID}}/
export CADD_DIR=/data/CCRBioinfo/public/CADD
export EXAC_DIR=/fdb/exac/release0.3
export CACHE_DIR=/lscratch/${{SLURM_JOB_ID}}
variant_effect_predictor.pl \
  -i {snakemake.input.vcf} --offline --cache   \
  --dir_cache $CACHE_DIR --fasta $CACHE_DIR/${{VEP_ASSEMBLY}}.fa  \
  --output {snakemake.output.vcf} --fork ${{SLURM_CPUS_ON_NODE}} \
  —sift s --polyphen s --vcf --canonical   \
  --symbol --buffer_size {buffer_size} --biotype --hgvs --assembly ${{VEP_ASSEMBLY}} \
  --gene_phenotype --gmaf --check_existing \
  --pubmed  --force_overwrite   \
  --maf_1kg --maf_esp --regulatory --domains --numbers   \
  --uniprot --xref_refseq \
  --plugin CADD,$CADD_DIR/whole_genome_SNVs.tsv.gz   \
  --plugin ExAC,$EXAC_DIR/ExAC.r0.3.sites.vep.vcf.gz   \
  --plugin CSN,1   \
  --plugin Carol
""")

