def hash_table():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    print(thisdict)
    print(thisdict["brand"])
    thisdict = dict(name="John", age=36, country="Norway")
    print(thisdict)

if __name__ == '__main__':
    hash_table()