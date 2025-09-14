

def print_stars(max_count):

    for count in range(max_count):
        print("*", end=" ")

def print_stars_v2(max_count):
    print(max_count * "*")

def print_star_grid(grid_size):
    for row in range(grid_size):
        for col in range(grid_size):
            print("*", end="")
        print()

def print_right_angle(count):
    for row in range(count):
        for col in range(row+1):
            print("*", end="")
        print()

def list_star(numbers: list):

    # for row in range(len(arr)):
    #     for col in range(arr[row]):
    #         print("*", end="")
    #     print()

    for number in numbers:
        print(number * "*")

def print_start_grid_concat(grid_size):


    for row in range(1, grid_size+1):

        print_msg = []

        for no_of_stars in range(1, grid_size+1):
            print_msg.append("*")
        
        print("".join(print_msg))

def print_star_grid_skip_even(grid_size):
    for row in range(1, grid_size+1):

        print_msg = []

        for no_of_stars in range(1, grid_size+1):
            # if (no_of_stars % 2 == 0):
            #     print_msg.append(" ")
            # else:
            #     print_msg.append("*")

            print_msg.append(" " if no_of_stars % 2 == 0 else "*")
        print("".join(print_msg))


def print_star_grid_skip_odd(grid_size):
    for row in range(1, grid_size+1):

        print_msg = []

        for no_of_stars in range(1, grid_size+1):
            # if (no_of_stars % 2 == 0):
            #     print_msg.append(" ")
            # else:
            #     print_msg.append("*")

            print_msg.append(" " if no_of_stars % 2 != 0 else "*")
        print("".join(print_msg))

def print_strat_at_borders(gridsize):

    for row in range(1, gridsize + 1):
        for col in range(1, gridsize + 1):
            # if row == 1 or row == gridsize or col == 1 or col == gridsize:
            #     print("*",end=" ")
            # else:
            #     print(" ", end=" ")
            is_star = (row == 1 or row == gridsize or col == 1 or col == gridsize)
            print("*" if is_star else " ", end=" ")
        print()

def print_star_pyramid(height):
    for level in range(height):
        for space in range(level, height):
            print("",end=" ")
        
        for star in range(level+1):
            print("*", end=" ")

        print()

def star_pyramid_v2(height):
    # no_of_stars = 1
    # for level in range(1, height+1, 1):
    #     no_of_spaces = height - level
    #     print(no_of_spaces * " " + no_of_stars * "* ")
    #     no_of_stars += 1

    for level in range(height):
        spaces = height - level - 1
        stars = level + 1
        print(" " * spaces + "* " * stars)

def print_inverted_star_pyramid(height):
    for level in range(height):

        for space in range(level):
            print("",end=" ")
        
        for star in range(height-level):
            print("*", end=" ")

        print()



def print_inverted_star_pyramid_v2(height):
    for level in range(height):
        spaces = level
        stars = height - level
        print(" " * spaces + "* " * stars)


def print_diamond_star(height):
    no_of_stars = 1
    for level in range(1, height+1, 1):
        no_of_spaces = height - level
        print(no_of_spaces * " " + no_of_stars * "* ")
        no_of_stars += 1
    
    for level2 in range(1, height+1, 1):
        no_of_spaces = level2
        no_of_stars =  height - level2
        print(no_of_spaces * " " + no_of_stars * "* ")

def print_diamond_star_v2(height):
    # Top half
    for level in range(height):
        spaces = height - level - 1
        stars = level + 1
        print(" " * spaces + "* " * stars)
    
    # Bottom half
    for level in range(height - 1):
        spaces = level + 1
        stars = height - level - 1
        print(" " * spaces + "* " * stars)


if __name__ == "__main__":
    
    # print_stars_v2(10000)
    # print_star_grid(5)
    # print_right_angle(4)

    # list_star([2,3,45,67,76])
    # print_start_grid_concat(5)
    # print_star_grid_skip_even(3)
    # print_star_grid_skip_odd(3)
    # print_strat_at_borders(50)


    
    
    print_star_pyramid(10)
    star_pyramid_v2(10)

    print_inverted_star_pyramid(5)
    print_inverted_star_pyramid_v2(5)

    print_diamond_star(5)
    print_diamond_star_v2(5)