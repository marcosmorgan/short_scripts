import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + "/scripts")
from configuration.experiment_1 import *



# Parsing parameters to load to load to R function
# PARAMETER_1 = ["paremeter_1"]
# PARAMETER_2 = "parameter_2"
# 
# replicates = ""
# for one_parameter_1 in PARAMETER_1[:-1]:
#   parameter_1s = '\"' + one_parameter_1 + '\",' + parameter_1s
# parameter_1s = parameter_1s + '\"' + PARAMETER_1[-1] + '\"'
# 
# parameter_2 = '\"' + PARAMETER_2 + '\"'
# 
# rule all:
#   input:
#     expand("../views/{experiment}/IP{replicates}.bed", replicates = PARAMETER_1, experiment = EXPERIMENT),
#     expand("../views/{experiment}/myBigWig{replicates}.bw", replicates = PARAMETER_1, experiment = EXPERIMENT),
# 
# rule create_gtfs:
#   input:
#     expand("../{experiment}/data/{affy_}", affy_ = AFFY, experiment = EXPERIMENT)
#   output:
#     "../views/{experiment}/Mus_musculus.GRCm38.91_up.gtf",
#     "../views/{experiment}/Mus_musculus.GRCm38.91_unchanged.gtf",
#     "../views/{experiment}/Mus_musculus.GRCm38.91_down.gtf"
#   shell:
#     "Rscript -e 'rmarkdown::render(\"Create_gtfs.Rmd\", params = list(replicates = list(" + affy + ")))'"
# 
# rule do_bedMerge:
#   input:
#     expand("../views/{experiment}/exomePeaks_views/{compounds}/peak.bed", experiment = EXPERIMENT, compounds = COMPOUNDS)
#   output:
#     "../views/{experiment}/exomePeaks_views/all/peak.bed"
#   shell:
#     "cat {input} | sort -k1,1 -k2,2n | mergeBed > {output}"
#     
# rule plot_profile_all:
#   input:
#     expand("../views/{experiment}/compute_matrixes/matrixScaledRegions_all.mat.gz", experiment = EXPERIMENT)
#   output:
#     "../results/{experiment}/results_profile_all.pdf"
#   shell:
#     "python_env/bin/plotProfile -m {input} "
#     "--startLabel Start_Codon --endLabel Stop_Codon -out {output}"




