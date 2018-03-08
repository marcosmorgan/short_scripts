configfile: 'config_rna_seq.yaml'

rule all:
   input:
     expand("../views/{experiment}/quant/{samples}/abundance.tsv", samples = config["samples"], experiment = config["EXPERIMENT"])

rule run_kallisto:
  input:
    R1 = lambda wildcards: "../data/" + config["EXPERIMENT"] + "/" + config["samples"][wildcards.samples]["r1"],
    R2 = lambda wildcards: "../data/" + config["EXPERIMENT"] + "/" + config["samples"][wildcards.samples]["r2"] 
  output:
    "../views/{experiment}/quant/{samples}/abundance.tsv"
  params:
    index = "/usr/local/Cellar/kallisto/0.44.0/tests/Mus_musculus.GRCm38.cdna.all.idx",
    directory = "../views/{experiment}/quant/"
  shell:
    """
    kallisto quant -i {params.index} -o {params.directory}{wildcards.samples} -b 100 {input.R1} {input.R2}
    """

# rule create_myBigWig_files:
#   input:
#     expand("../views/{experiment}/exomePeaks_views/{compounds}/NA_control_lambda.sorted.bdg", compounds = config["compounds"], experiment = config["EXPERIMENT"])
#   output:
#     expand("../views/{experiment}/myBigWigs/myBigWig{compounds}.bw", compounds = config["compounds"], experiment = config["EXPERIMENT"])
#   params:
#     sizes = config["external"][species]["sizes"]
#   shell:
#     """
#     {scripts}bedGraphToBigWig {input} {params.sizes} {output} 
#     """
