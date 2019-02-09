configfile: 'config_homer.yaml'

rule all:
  input:
      expand("../projects/{project}/results/{sample}/homerMotifs.all.motifs", 
          project=config["project"]["homer"], 
          sample=config["samples"])

rule run_shuffleBed:
  input:
      expand("../../../peaks/gene_body/projects/{project_peak}/views/{caller}/{sample}/{file}", 
          caller = config["peaks"]["caller"], 
          file = config["peaks"]["file"], 
          project_peak=config["project"]["peaks"], 
          sample=config["samples"])   
  output:
      "../projects/{project}/views/shuffledBeds/shuffled_{sample}.bed"
  params:
      reference = lambda wildcards : config["samples"][wildcards.sample]["reference"],
      chormosomes = lambda wildcards : config["samples"][wildcards.sample]["chormosomes"]
  shell:
      "shuffleBed -incl {params.reference} \
      -i {input} \
      -g {params.chormosomes} > {output}"

rule run_find_motifs:
  input:
      peaks = expand("../../../peaks/gene_body/projects/{project_peak}/views/{caller}/{sample}/{file}", 
          caller = config["peaks"]["caller"], 
          file = config["peaks"]["file"], 
          project_peak=config["project"]["peaks"], 
          sample=config["samples"]),
      shuffled = "../projects/{project}/views/shuffledBeds/shuffled_{sample}.bed"
  output:
      "../projects/{project}/results/{sample}/homerMotifs.all.motifs"
  params:
      out = "../projects/{project}/results/{sample}/",
      genome = lambda wildcards : config["samples"][wildcards.sample]["genome"]
  shell:
      "findMotifsGenome.pl {input.peaks} {params.genome} {params.out} \
      -size 200 \
      -len 6 \
      -mask \
      -bg {input.shuffled} \
      -rna"

