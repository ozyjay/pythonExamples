# example of a "write the function"
# exam question


def get_eldest_v1(names, ages):
    current = 0
    for i in range(len(names)):
        if ages[i] > ages[current]:
            current = i
    return names[current]


def get_eldest_v2(names, ages):
    eldest = [names[i] for i, age in enumerate(ages) if age == max(ages)]
    return eldest[0]


def demo_add_to_dict():
    ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    ages_dict[name] = age

    for name, age in ages_dict.items():
        print("{:<10} - {:>10}".format(name, age))
