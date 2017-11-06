library(testthat)
source("helper_functions.R")
#test_dir("manage_folders/scripts/")

source("helper_functions.R")

context("Create folders")

test_that("give_month_days ", {
  
  expect_that(give_month_days(2017, 10)[1], equals(as.Date("2017-10-02")))
  expect_that(give_month_days(2017, 10)[6], equals(as.Date("2017-10-09")))
  
}
)
