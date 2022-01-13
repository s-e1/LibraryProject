import requests


def login():
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    data = res.json()
    # print(data)
    while True:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        for user in data:
            if user["name"] == name and user["email"] == email:
                return
        print("You are not verified.")
