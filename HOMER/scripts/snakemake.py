import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + "/scripts")
from configuration.leukemia import *

path=PATH

rule all:
  input:
      expand("../results/{experiment}/peaks_motifOutput_{sample}/homerResults/motif1.motif", experiment=EXPERIMENT, sample=SAMPLES)

rule run_shuffleBed:
  input:
      expand("../data/{experiment}/mm10_refseq.bed", experiment = EXPERIMENT),
      expand("../data/{experiment}/mm10.chrom.sizes", experiment = EXPERIMENT),
      expand("{path}{experiment}/exomePeaks_views/{sample}/peak.bed", path=PATH, experiment=EXPERIMENT, sample=SAMPLES)
  output:
      "../views/{experiment}/shuffledBeds/mm10_refseq_shuffled_{sample}.bed"
  shell:
      "shuffleBed -incl ../data/{wildcards.experiment}/mm10_refseq.bed -i {path}{wildcards.experiment}/exomePeaks_views/{wildcards.sample}/peak.bed -g ../data/{wildcards.experiment}/mm10.chrom.sizes > ../views/{wildcards.experiment}/shuffledBeds/mm10_refseq_shuffled_{wildcards.sample}.bed"

rule run_find_motifs:
  input:
      expand("../views/{experiment}/shuffledBeds/mm10_refseq_shuffled_{sample}.bed", experiment=EXPERIMENT, sample=SAMPLES),
      expand("{path}{experiment}/exomePeaks_views/{sample}/peak.bed", path=PATH, experiment=EXPERIMENT, sample=SAMPLES)
  output:
      "../results/{experiment}/peaks_motifOutput_{sample}/homerResults/motif1.motif"
  shell:
      "findMotifsGenome.pl {path}{wildcards.experiment}/exomePeaks_views/{wildcards.sample}/peak.bed mm10 ../results/{wildcards.experiment}/peaks_motifOutput_{wildcards.sample} -size 200 -len 6 -mask -bg ../views/{wildcards.experiment}/shuffledBeds/mm10_refseq_shuffled_{wildcards.sample}.bed"







