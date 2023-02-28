def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


print("=======================================")

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)

print("een tweede keer met meer key-value paren")

print("=======================================")

intro(
    Firstname="John",
    Lastname="Wood",
    Email="johnwood@nomail.com",
    Country="Wakanda",
    Age=25,
    Phone=9876543210,
)
