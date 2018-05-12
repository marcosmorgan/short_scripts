library(testthat)
library(dplyr)
library(knitr)
library(bizdays)
library(lubridate)
#library(dplyr)
#test_file("clusters/scripts/test_clusters.R")


give_month_days <- function(year, month){
  
  X <- seq( as.Date("2017", format="%Y"), as.Date("2025", format="%Y"), by=1)
  X <- X[unlist(lapply(X, function(x) month(x) == month & year(x) == year))] 
  weekdays.X <- X[ ! weekdays(X) %in% c("Saturday", "Sunday") ]  
  return(weekdays.X)
}

give_month_files <- function(year, month, tables){
  
  year_month <- paste(year, month, sep="-")
  month_days <- give_month_days(year, month)
  
  day <- as.character(month_days[1])
  dir.create(file.path("../results", year_month, day), recursive=T)
  setwd(file.path("../results", year_month, day))
  #write.csv2(reagents_table, paste(day, "reagents.csv", sep = "_"), row.names = FALSE)
  #write.csv2(samples_table, paste(day, "samples.csv", sep = "_"), row.names = FALSE)
  
  for(table in tables){
    a_table <- read.csv2(paste("../../../data/", table, sep="")) 
    write.csv2(a_table, paste(day, table, sep = "_"), row.names = FALSE)
  }
  file.create(paste(day, "_done.txt", sep = "_"))
  
  for(d in c(2:length(month_days))){
    day <- as.character(month_days[d])
    dir.create(file.path("../", day))
    setwd(file.path("../", day))
    #write.csv2(reagents_table, paste(day, "reagents.csv", sep = "_"), row.names = FALSE)
    #write.csv2(samples_table, paste(day, "samples.csv", sep = "_"), row.names = FALSE)
    for(table in tables){
      a_table <- read.csv2(paste("../../../data/", table, sep="")) 
      write.csv2(a_table, paste(day, table, sep = "_"), row.names = FALSE)
    }
    file.create(paste(day, "_done.txt", sep = "_"))
    
  }

  setwd(file.path("../../"))

}

give_year_files <- function(year, tables){
  year_char <- as.character(year)
  for(i in 1:12){
    dir.create(file.path(paste("../results/", year_char, "-", as.character(i), sep="")))
    give_month_files(year, i, tables)
  } 
}


#' Source the R code from an knitr file, optionally skipping plots
#'
#' @param file the knitr file to source
#' @param skip_plots whether to make plots. If TRUE (default) sets a null graphics device
#'
#' @return This function is called for its side effects
#' @export

source_rmd = function(file, skip_plots = TRUE) {
  temp = tempfile(fileext=".R")
  knitr::purl(file, output=temp)
  
  if(skip_plots) {
    old_dev = getOption('device')
    options(device = function(...) {
      .Call("R_GD_nullDevice", PACKAGE = "grDevices")
    })
  }
  source(temp)
  if(skip_plots) {
    options(device = old_dev)
  }
}