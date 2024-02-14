library(plot3D)

optimize_func <- function(x1, x2) {2 * x1 ** 2 + x1 * x2 + x2 ** 2}

x <- -10:10
y <- -10:10
z = outer(x, y, optimize_func)

pmat <- persp3D(x = x, y = y, z)
mypoints <- points3D(c(0, 10, 15), c(3, 4, 5), c(10, 15, 19), pmat=pmat)
points3D(mypoints, pch=16, col=2)