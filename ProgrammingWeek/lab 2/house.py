def print_roof():
    print("  ^")
    print(" ^ ^")
    print("^   ^")

def print_ceiling():
    print("|||||")

def print_wall():
    print("|   |")
    print("|   |")

def print_floor(): 
    print("|||||")

def print_house(h):
    if h == 1:
        print_roof()
        print_ceiling()
        print_wall()
        print_floor()
    elif h == 2:
        print_roof()
        print_ceiling()
        print_wall()
        print_floor()
        print_wall()
        print_floor()
    elif h == 3:
        print_roof()
        print_ceiling()
        print_wall()
        print_floor()
        print_wall()
        print_floor()
        print_wall()
        print_floor()

print_house(3)