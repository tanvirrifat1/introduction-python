def double_decker():

    print("Double Decker")

    def inner_fun():
        print("Inner Function")

    return inner_fun


print(double_decker())
