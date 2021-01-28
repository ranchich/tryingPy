list = [
    {"name": "ran", "city": "jerusalem"},
    {"name": "gil", "city": "tel aviv"},
    {"name": "yuval", "city": "givaataim"}
]

def f (person):
    return person ["city"]

list.sort(key=f)

print(list)