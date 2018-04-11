products = [["Phone", 340, False],
            ["PC", 1420.95, True],
            ["Plant", 24.5, True]]

on_sale_products = [product for product in products
                    if product[2]]

print(on_sale_products)


class Person:
    def __init__(self, name="bob", age=24):
        self.name = name # attributes of a Person
        self.age = age

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def says(self, message):
        print(self.name + " says " + message)

    def __eq__(self, other):
        return self.name == other.name

    def __le__(self, other):
        return self.name < other.name


class Student(Person):
    def __init__(self, name, age, debt):
        super().__init__(name, age)
        self.debt = debt


str()


tristan = Person("Tristan", 19)

if type(tristan) is Person:
    print("yup, he is a person :)")

print(type(tristan))

people = [Person(), Person(), Person()]

kevy = people[0]
kevy.name = "kevy"
kevy.says("gday mate!")

print(people)


class User:
    def __init__(self, name='bob'):
        self.score = 0
        self.tacos = 5
        self.name = name

    def give(self, other):
        other.tacos += 1
        self.tacos -= 1
        self.score += 1

    def __str__(self):
        return "{0.name}, {0.score} points, {0.tacos} tacos left".format(self)

    def __repr__(self):
        return str(self)


user = User()
print(user)