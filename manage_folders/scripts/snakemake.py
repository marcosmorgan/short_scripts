configfile: "configuration/configuration.yml"

wildcard_constraints:
  sample="[^_,^.]+"

rule all:
  input:
    directory(expand("../projects/{project}/results/{year}/", 
    project=config["project"], year=config["year"]))

rule create_folders:
  input:
    "../data/update_reagents.csv",
    "../data/update_samples.csv"
  output:
    directory(expand("../projects/{project}/results/{year}/", 
    project=config["project"], year=config["year"]))
  params:
    year=config["year"],
    project=config["project"]
  shell:
    "Rscript -e 'rmarkdown::render(\"manage_folders.Rmd\", params = list( \
    year = \"{params.year}\", \
    month = \"all\", \
    project = \"{params.project}\" \
    ))'"


# 
# rule exomePeaks_peak_call:
#   input:
#     input = lambda wildcards: config["SampleList"][wildcards.sample]["input"],
#     ip = lambda wildcards: config["SampleList"][wildcards.sample]["ip"]
#   output:
#     "../views/{experiment}/exomePeaks/{sample}/peak.bed"
#   params:
#     gtf = lambda wildcards: config["SampleList"][wildcards.sample]["gtf"]
#   shell:
#     "Rscript -e 'rmarkdown::render(\"exomePeaks.Rmd\", params = list( \
#     gtf    = \"{params.gtf}\", \
#     experiment = \"{wildcards.experiment}\", \
#     sample = \"{wildcards.sample}\", \
#     input  = \"{input.input}\", \
#     ip     = \"{input.ip}\" \
#     ))'"
# 
# rule MACS2_peak_call:
#   input:
#     input = lambda wildcards: config["SampleList"][wildcards.sample]["input"],
#     ip = lambda wildcards: config["SampleList"][wildcards.sample]["ip"]
#   output:
#     "../views/{experiment}/MACS2/{sample}/NA_treat_pileup.bdg"
#   params:
#     g = lambda wildcards: config["SampleList"][wildcards.sample]["g"],
#     output = "../views/{experiment}/MACS2/{sample}/"
#   message:
#     """
#     Running rule MACS2 peak call
#     sample {wildcards.sample}
#     input {input.input} {input.ip}
#     output {output}
#     This is the output directory: {params.output}
#     """
#   shell:
#     """
#     macs2 callpeak -t {input.ip} \
#     -c {input.input} \
#     -g {params.g} \
#     -B \
#     --outdir {params.output}
#     """
    
# ADATE  = config["ADATE"]
# genotypes = config["genotypes"]
# PPYTHON = config["PPYTHON"]
# lanes = config["lanes"]
# 
# rule all:
#   input:
#     expand("../data/read_gels/{adate}_genotyping/gel_loading_results.csv", adate = ADATE),
#     expand("../results/{adate}/togeno_{adate}.csv", adate = ADATE)    
# 
# rule load_colony:
#   input:
#     "../data/Breeding_population.xls"
#   output:
#     "../views/colony.csv",
#     "../views/litters.csv",
#     "../views/matings.csv",
#   shell:
#     "Rscript -e 'rmarkdown::render(\"colony.Rmd\")'"
# 
# rule run_genotype:
#   input:
#     "../views/colony.csv",
#     "../views/litters.csv",
#     "../views/matings.csv",
#   output:
#     "../results/{adate}/togeno_{adate}.csv",
#   params:
#     ignore = 'as.vector(' + config["IGNORE"] + ')' 
#   message:
#     """
#     Running rule run_genotype
#     input files: {input}
#     output files: {output}
#     parameters: {params}
#     wildcards: {wildcards}
#     """
#   shell:
#     "Rscript -e 'rmarkdown::render(\"genotype.Rmd\", \
#      params = list(adate = \"{wildcards.adate}\", \
#                   ignore = {params.ignore}))'"
# 
# #Rscript -e 'rmarkdown::render("genotype.Rmd", params = list(adate = "2017-11-23", ignore = "this"))'
# 
# rule run_gels:
#   input:
#     "../data/read_gels/{adate}_genotyping/gel_loading_results.csv"
#   output:
#     "../data/read_gels/{adate}_genotyping/{adate}_genotyping_{a_genotype}.pdf"
#   shell:
#     PPYTHON + "read_gels.py"
# 
# rule run_load_results:
#   input:
#     "../data/read_gels/{adate}_genotyping/gel_loading_results.csv"
#   output:
#     "../results/{adate}/togeno_{adate}_res.csv"
#   params:
#     ignore = 'as.vector(' + config["IGNORE"] + ')' 
#   shell:
#     "Rscript -e 'rmarkdown::render(\"load_results.Rmd\", \
#      params = list(adate = \"{wildcards.adate}\", \
#                   ignore = {params.ignore}))'"
