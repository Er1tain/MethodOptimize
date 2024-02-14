import rpy2.robjects as robjects
import rpy2.robjects.packages as packages
from tkinter import messagebox

class Optimize:

    def GradientMethod(x10, x20, change, ex, ey, M):
        
        r = robjects.r
        r('''
        library(rgl)
        library(future)
        
            gradient_method <- function(x10, x20, change, ex, ey, M) {

            x10_x20_points <- c(x10, x20) #vector values (x10,.x20) for all iteration

            old_x10 <- x10; old_x20 <- x20;
            grad <- c(0.0, 0.0)

            for (i in 1:M) {
                
                #point 3
                grad[1] <- 4 * x10 + x20
                grad[2] <- x10 + 2 * x20

                #point 4
                if (sqrt(grad[1] * grad[1] + grad[2] * grad[2]) < ex) break

                #point 7
                old_value_func <- 2 * x10 * x10 + x10 * x20 + x20 * x20;

                x10 <- x10 - change * grad[1]
                x20 <- x20 - change * grad[2]

                #point 8
                while (2 * x10 * x10 + x10 * x20 + x20 * x20 >= old_value_func) {
                change <- change / 2
                
                x10 <- x10 - change * grad[1]
                x20 <- x20 - change * grad[2]
            }

                #point 9
                if (sqrt((x10 - old_x10) * (x10 - old_x10) + (x20 - old_x20) * (x20 - old_x20)) < ex && ((2 * x10 * x10 + x10 * x20 + x20 * x20) - old_value_func) < ey) break
                old_value_func <- 2 * x10 * x10 + x10 * x20 + x20 * x20;

                x10_x20_points <- append(x10_x20_points, c(x10, x20))

            }

            
            return(x10_x20_points)
        }''')
        r(f'''
            plan(sequential)
        
            x <- seq(-20, 20)
            y <- x
            f <- function(x1, x2) 2 * x1 ** 2 + x1 * x2 + x2 ** 2
            
            z <- outer(x, y, f)''')
        
        r(f'''
            x10_x20_points <- gradient_method({x10}, {x20}, {change}, {ex}, {ey}, {M})

            x_points_iteration <- x10_x20_points[seq(from=1, to={M} * 2, by=2)]
            y_points_iteration <- x10_x20_points[seq(from=2, to={M} * 2, by=2)]
        
            par3d(windowRect = c(20, 30, 800, 800))
            persp3d(x, y, z, col="#d3e90ef8", )
            for (i in 1:length(x_points_iteration)) 
                future({{
                    Sys.sleep(0.25)
                    points3d(x_points_iteration[i], y_points_iteration[i], f(x_points_iteration[i], y_points_iteration[i]), col="red", size=8)

                }})
            
        ''')

        messagebox.showinfo(message="Найден минимум!")

    def FastestOptMethod(x10, x20, change, ex, ey, M):
        pass

    def NewtonRafson(x10, x20, change, ex, ey, M):
        pass

    def CoordMethod(x10, x20, change, ex, ey, M):
        pass

        
