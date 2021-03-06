library(testthat)
library(dplyr)
library(knitr)
library(bizdays)
library(lubridate)
#library(dplyr)
#test_file("clusters/scripts/test_clusters.R")

give_month_days <- function(year, month, weekends){
  X <- seq( as.Date("2017", format="%Y"), as.Date("2025", format="%Y"), by=1)
  X <- X[unlist(lapply(X, function(x) month(x) == month & year(x) == year))] 
  if(weekends){
  X <- X[ ! weekdays(X) %in% c("Saturday", "Sunday") ] 
  }
  return(X)
}

give_month_files <- function(year, month, tables, weekends, path){
  year_month <- paste(year, month, sep="-")
  month_days <- give_month_days(year, month, weekends)
  day <- as.character(month_days[1])
  first = getwd()
  
  for(d in c(1:length(month_days))){
    day <- as.character(month_days[d])
    for(table in tables){
      setwd(first)
      a_table <- read.csv2(paste("../data/", table, sep=""))
      dir.create(file.path(path, year_month, day), recursive=T)
      setwd(file.path(path, year_month, day))
      write.csv2(a_table, paste(day, table, sep = "_"), row.names = FALSE)
    }
    file.create(paste(day, "_done.txt", sep = "_"))
  }
  setwd(first)
}

give_year_files <- function(year, tables, weekends, path){
  year_char <- as.character(year)
  for(i in 1:12){
    dir.create(file.path(paste(path, "/", year_char, "-", as.character(i), sep="")))
    give_month_files(year, i, tables, weekends, path)
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