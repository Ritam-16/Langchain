from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    'name': "Manoj",
    'age': 32 #'32'
}

print(new_person)