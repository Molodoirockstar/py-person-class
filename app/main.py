class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons_objects = [
        Person(person["name"], person["age"]) for person in people
    ]
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return persons_objects
