library(tidyverse)
library(purrr)
library(cluster)


user_features = read_csv("/home/georgehagstrom/work/Teaching/DATA608/DataStory6/user_features.csv")

user_features = user_features |> mutate(total_purchases = rowSums(across(Saturday:Friday)))

user_features = user_features |> mutate(across(`packaged cheese`:Friday, \(x) x/total_purchases))

pca_fit_ob =user_features |> select(-user_id) |> prcomp(scale = TRUE)


centers_2 = user_features |> select(-user_id) |> scale() |> kmeans(centers=10,iter.max=20,nstart=5)

library(broom)

user_low = pca_fit_ob |> augment(user_features) |> select(.fittedPC1:.fittedPC12)

kvec = seq(2:40)
user_low_matrix <- as.matrix(user_low)

wcss <- map(kvec, .f = function(k) {
  kmeans(user_low, centers = k, nstart = 5)$tot.withinss
})



map(kvec,\(x) rnorm(10,x) )
kvec[1]


mtcars |>
  split(mtcars$cyl) |>
  map(\(df) lm(mpg ~ wt, data = df)) |>
  map(summary) |>
  map_dbl("r.squared")
