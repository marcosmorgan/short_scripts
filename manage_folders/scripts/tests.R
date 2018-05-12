library(testthat)
source("helper_functions.R")
#test_dir("manage_folders/scripts/")

source("helper_functions.R")

context("Create folders")

test_that("give_month_days ", {
  
  month <- 10
  year  <- 2017 
  
  X <- seq( as.Date("2017", format="%Y"), as.Date("2025", format="%Y"), by=1)
  month(X[1]) == month
  X <- X[unlist(lapply(X, function(x) month(x) == month & year(x) == year))] 
  weekdays.X <- X[ ! weekdays(X) %in% c("Saturday", "Sunday") ]  
  
  expect_that(give_month_days(2017, 10)[1], equals(as.Date("2017-10-02")))
  expect_that(give_month_days(2017, 10)[6], equals(as.Date("2017-10-09")))
  
}
)

context("Give files correctly")

test_that("Give months works ", {
  
  year  <- 2017
  month <- 10 
  
  year_month <- paste(year, month, sep="-")
  month_days <- give_month_days(year, month)
  
  day <- as.character(month_days[1])
  dir.create(file.path("../results", year_month, day), recursive=T)
  setwd(file.path("../results", year_month, day))
  
  #expect_that(give_month_days(2017, 10)[1], equals(as.Date("2017-10-02")))
  #expect_that(give_month_days(2017, 10)[6], equals(as.Date("2017-10-09")))
  
}
)