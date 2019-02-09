#findMotifsGenome.pl <peak/BED file> <genome> <output directory> -size # [options]
#i.e. findMotifsGenome.pl ERpeaks.txt hg18 ER_MotifOutput/ -size 200 -mask

shuffleBed [OPTIONS] -i <BED/GFF/VCF> -g <GENOME>
-incl

shuffleBed -incl mm10_refseq.bed -i con_peak.bed -g mm10.chrom.sizes > mm10_refseq_shuffled.bed

findMotifsGenome.pl con_peak.bed mm10 peaks_motifOutput_6/ -size 200 -len 6 -mask -bg mm10_refseq_shuffled.bed
