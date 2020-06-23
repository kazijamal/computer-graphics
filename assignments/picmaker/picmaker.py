file = open("image.ppm", "w")

file.write("P3\n500 500\n255\n")

for ycor in range(500):
    r = g = b = y = 0
    for xcor in range(500):
        if xcor < 15 or xcor >= 485 or ycor < 15 or ycor >= 485:
            file.write("0 0 0 ")
        elif xcor < 240 and ycor < 240:
            file.write("255 " + str(r) + " " + str(r) + " ")
            if xcor < 80:
                r += 3
            elif r > 1:
                r -= 2
        elif xcor >= 260 and ycor < 240:
            file.write(str(g) + " 255 " + str(g) + " ")
            if xcor < 420:
                g += 2
            elif g > 1:
                g -= 3
        elif xcor < 240 and ycor >= 260:
            file.write(str(b) + " " + str(b) + " 255 ")
            if xcor < 80:
                b += 3
            elif b > 1:
                b -= 2
        elif xcor >= 260 and ycor >= 260:
            file.write("255 255 "  + str(y) + " ")
            if xcor < 420:
                y += 2
            elif y > 1:
                y -= 3
        else:
            file.write("255 255 255 ")
    file.write("\n")

file.close()
