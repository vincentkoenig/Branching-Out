import json


def open_file():
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
        return users
    except FileNotFoundError:
        print("Error: users.json not found.")
        return []
    except json.JSONDecodeError:
        print("Error: users.json contains invalid JSON.")
        return []


def filter_users_by_name(name):
    users = open_file()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    users = open_file()
    try:
        age_int = int(age)
    except ValueError:
        print("Please enter a valid number for age.")
        return

    filtered_users = [user for user in users if user["age"] == age_int]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    users = open_file()

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
