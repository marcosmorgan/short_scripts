
give_month_days <- function(year, month){
  
  X <- seq( as.Date("2017", format="%Y"), as.Date("2025", format="%Y"), by=1)
  X <- X[unlist(lapply(X, function(x) month(x) == month & year(x) == year))] 
  weekdays.X <- X[ ! weekdays(X) %in% c("Saturday", "Sunday") ]  
  return(weekdays.X)
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