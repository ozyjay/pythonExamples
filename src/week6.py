from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        self.title = "My App man!"
        self.root = Button(text="okay")
        return self.root

app = MyApp()
app.run()



class Person:
    def __init__(self, first_name = "bob"):
        self.first_name = first_name
        self.last_name = "the builder"
        self.age = 24

    def __str__(self):
        return self.first_name

    def __repr__(self):
        return "anything"

me = Person("Jase")
you = Person("you")

us = [Person("Tristan"), Person("Dylan"), Person("?"), Person("bob")]
print(us)

class Table:
    def __init__(self):
        self.position = 0

    def move(self):
        self.position += 1

    def reset(self):
        self.position = 0

table = Table()
table.move()



rainfall = list()



# assume that people is a dictionary
# of the form: name -> age
def older_than(people, age_threshold):
    result = []

    for name in people:
        age = people[name]
        if age >= age_threshold:
            result.append(name)

    return result


def older_than_v2(people, threshold):
    return [name for (name, age) in people.items()
            if age >= threshold]

