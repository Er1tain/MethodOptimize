
optimize_func <- function(x1, x2) {2 * x1 ** 2 + x1 * x2 + x2 ** 2}

x <- -10:10
y <- -10:10

#Example points

#

z = outer(x, y, optimize_func)

#for (i in 1:1) {
    
    
persp(x, y, z, xlab='X Variable', ylab='Y Variable', zlab='Z Variable',
main='3D Plot', col='lightblue', shade= .4 , theta = 0 , phi = 15 , ticktype='detailed' )
points(-5, -5)
    
#}

