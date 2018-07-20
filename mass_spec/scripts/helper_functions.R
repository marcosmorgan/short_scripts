

capitalize <- function(name){
  name <- paste(toupper(substr(name, 1, 1)), 
                tolower(substr(name, 2, nchar(name))), 
                sep="")
  return(name)
}

extract_genes <- function(r){
  split <- paste(grep("sp", unlist(strsplit(r, ";")), value=T), collapse="")
  split_mouse <- paste(grep("_MOUSE", unlist(strsplit(split, "\\|")), value=T), collapse="_")
  split_last  <- lapply(unique(unlist(strsplit(split_mouse, "\\_"))), capitalize)
  split_last_clean  <- paste(split_last[!split_last %in% c("Mousesp", "Mouse")], collapse=",")
  return(split_last_clean)
}