# example of a "write the function"
# exam question
def get_eldest(names, ages):
    current = 0
    for i in range(len(names)):
        if ages[i] > ages[current]:
            current = i
    return names[current]


ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

name = input("Enter your name: ")
age = int(input("Enter your age: "))
ages_dict[name] = age

for name, age in ages_dict.items():
    print("{:<10} - {:>10}".format(name, age))


