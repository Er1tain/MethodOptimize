x10 <- as.double((readline("Задайте x10: ")))
x20 <- as.double(readline("Задайте x20: "))
change <- as.double((readline("Задайте шаг спуска: ")))
ex <- as.double(readline("Задайте ex: "))
ey <- as.double(readline("Задайте ey: "))
M <- as.integer(readline("Введите кол-во итераций: "))

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

    print(paste("Текущая точка: ", as.character(x10), ", " ,as.character(x20)))
}

print(paste("Точка минимума: ", as.character(x10), ", ", as.character(x20)))

