__author__ = "Sean Davis"
__email__ = "sdavis2@mail.nih.gov"
__license__ = "MIT"

# Assumes that the genome is available via UCSC
# and that pybedtools has been installed in
# the same environment as snakemake is running in.

import sys
from pybedtools.contrib.bigwig import bam_to_bigwig

sys.path.append('/data/genome/jksrc_v314/utils/bin/x86_64')

bam_to_bigwig(snakemake.input.bam,snakemake.params.genome,snakemake.output[0])

