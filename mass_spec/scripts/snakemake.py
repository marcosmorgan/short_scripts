configfile: "configuration/configuration.yml"

rule all:
  input:
    expand("../views/{experiment}/scatter_plot.Rda",
            experiment = config["experiment"])

rule import_mass_spec_data:
  input:
    expand("../data/{experiment}/metadata.txt", experiment = config["experiment"])
  output:
    "../views/{experiment}/mass_spec.Rda"
  params:
    mass_spec_data = config["mass_spec_data"]
  shell:
    "Rscript -e 'rmarkdown::render(\"script.Rmd\", params = list( \
    experiment = \"{wildcards.experiment}\", \
    mass_spec_data = \"{params.mass_spec_data}\" \
    ))'"

rule merge_mass_spec_affy:
  input:
    expand("../views/{experiment}/mass_spec.Rda", experiment = config["experiment"])
  output:
    "../views/{experiment}/scatter_plot.Rda"
  params:
    change_a = config["change_a"],
    significance_a = config["significance_a"],
    change_b = config["change_b"],
    significance_b = config["significance_b"]
  shell:
    "Rscript -e 'rmarkdown::render(\"mass_spec_affy.Rmd\", params = list( \
    change_a = \"{params.change_a}\", \
    significance_a = \"{params.significance_a}\", \
    change_b = \"{params.change_b}\", \
    significance_b = \"{params.significance_b}\" \
    ))'"


# rule all:
#   input:
#     #expand("../views/{experiment}/exomePeaks/{sample}/peak.bed", experiment = config["EXPERIMENT"], sample = config["SampleList"]),
#     expand("../views/{experiment}/MACS2/{sample}/NA_treat_pileup.bdg", experiment = config["EXPERIMENT"], sample = config["SampleList"])
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
