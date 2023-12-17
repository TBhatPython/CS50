def main():
    mass = int(input("Please input the mass: " ))
    c = 300000000
    print(convert(mass, c))


def convert(mass, constant):
    energy = (mass * pow(constant, 2))
    return (f"{energy:,}")





main()