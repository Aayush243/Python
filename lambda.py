people = [

    {"name":"Harry","house":"Griffindor"},
    {"name":"Cho","house":"Griffindor"},
    {"name":"Draco","house":"Slytherine"}
]
people.sort(key=lambda person:person["house"])
print(people)
