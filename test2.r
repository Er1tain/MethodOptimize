library(rgl)
source("Rscript_method.r")

x <- seq(-10, 10)
y <- x
f <- function(x1, x2){
   2 * x1 ** 2 + x1 * x2 + x2 ** 2
}
z <- outer(x, y, f)

x10 <- as.double((readline("Задайте x10: ")))
x20 <- as.double(readline("Задайте x20: "))
change <- as.double((readline("Задайте шаг спуска: ")))
ex <- as.double(readline("Задайте ex: "))
ey <- as.double(readline("Задайте ey: "))
M <- as.integer(readline("Введите кол-во итераций: "))

x10_x20_points <- gradient_method(x10, x20, change, ex, ey, M)

x_points_iteration <- x10_x20_points[seq(from=1, to=M * 2, by=2)]
y_points_iteration <- x10_x20_points[seq(from=2, to=M * 2, by=2)]

persp3d(x, y, z, col="#d3e90ef8")
for (i in 1:length(x_points_iteration)) {
   points3d(x_points_iteration[i], y_points_iteration[i], f(x_points_iteration[i], y_points_iteration[i]), col="red", size=8)
   
}

#persp3d(x, y, z, col="gray", front="line", back="line")
#spheres3d(1,1,2,col="red",radius=0.5)  ## appropriate radius: I used x <- y <- 1:20