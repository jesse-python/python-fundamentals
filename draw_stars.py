def draw_stars(list):
    for i in range(len(list)):
        star_string = ""
        for num in range(0, list[i]):
            star_string += "*"
        print star_string


x = [4,6,1,3,5,25]
draw_stars(x)
