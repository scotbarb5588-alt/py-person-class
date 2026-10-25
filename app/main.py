class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Clear instances created by an earlier function call
    Person.people.clear()

    # First pass: create every Person instance
    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    # Second pass: connect spouses
    for person_data, person_instance in zip(people, person_list):
        if person_data.get("wife") is not None:
            person_instance.wife = Person.people[person_data["wife"]]

        if person_data.get("husband") is not None:
            person_instance.husband = Person.people[person_data["husband"]]

    return person_list
