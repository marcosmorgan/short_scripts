configfile: 'config_homer.yaml'

rule all:
  input:
      expand("../projects/{project}/results/{sample}/homerMotifs.all.motifs", 
          project=config["project"]["homer"], 
          sample=config["samples"])

rule intersect_beds:
  input:
      expand("../../../peaks/gene_body/projects/{project_peak}/views/{caller}/{sample}/{file}", 
          caller = config["peaks"]["caller"], 
          file = config["peaks"]["file"], 
          project_peak=config["project"]["peaks"], 
          sample=config["samples"])   
  output:
      "../projects/{project}/views/shuffledBeds/intersected_{sample}.bed"
  params:
      reference = lambda wildcards : config["samples"][wildcards.sample]["reference"]
  shell:
      "intersectBed  \
      -a {input} \
      -b {params.reference} > {output}"

rule run_shuffleBed:
  input:
      "../projects/{project}/views/shuffledBeds/intersected_{sample}.bed"
  output:
      "../projects/{project}/views/shuffledBeds/shuffledIntersected_{sample}.bed"
  params:
      reference = lambda wildcards : config["samples"][wildcards.sample]["reference"],
      chormosomes = lambda wildcards : config["samples"][wildcards.sample]["chormosomes"]
  shell:
      "shuffleBed -incl {params.reference} \
      -i {input} \
      -g {params.chormosomes} > {output}"

rule run_find_motifs:
  input:
      peaks = "../projects/{project}/views/shuffledBeds/intersected_{sample}.bed",
      shuffled = "../projects/{project}/views/shuffledBeds/shuffledIntersected_{sample}.bed"
      #shuffled = "../projects/{project}/views/shuffledBeds/shuffledIntersected_sample4.bed"
  output:
      "../projects/{project}/results/{sample}/homerMotifs.all.motifs"
  params:
      out = "../projects/{project}/results/{sample}/",
      genome = lambda wildcards : config["samples"][wildcards.sample]["genome"]
  shell:
      "findMotifsGenome.pl {input.peaks} {params.genome} {params.out} \
      -size 450 \
      -len 5 \
      -S 3 \
      -p 4 \
      -bg {input.shuffled} \
      -mask \
      -cpg \
      -rna"

# sample123
# sample456
#       "findMotifsGenome.pl {input.peaks} {params.genome} {params.out} \
#       -size 400 \
#       -len 6 \
#       -S 3 \
#       -p 4 \
#       -bg {input.shuffled} \
#       -mask \
#       -cpg \
#       -rna"
