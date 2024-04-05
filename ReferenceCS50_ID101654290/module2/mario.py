def main():
    print_square(3)

def print_colum(height):
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

def print_square(size):
    for i in range(size):
        print("#" * size)
"""
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")

        print()
"""
main()