import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + "/scripts")
from configuration.leukemia import *

rule all:
  input:
      expand("../results/{experiment}/{condition}_pie.pdf", experiment=EXPERIMENT, condition=CONDITION)

rule run_shuffleBed:
  input:
      expand("../data/{experiment}/Mus_musculus.GRCm38.91.gff3.gz", experiment = EXPERIMENT),
      expand("{path}{experiment}/exomePeaks_views/{condition}/peak.bed", path=PATH_BED, experiment=EXPERIMENT, condition=CONDITION)
  output:
      "../results/{experiment}/{condition}_pie.pdf"
  shell:
      "Rscript -e 'rmarkdown::render(\"peakAnnotation.Rmd\", params = list(condition = \"" + CONDITION + "\" , experiment = \""  + EXPERIMENT + "\" , path_bed = \"" + PATH_BED + "\"))'"
