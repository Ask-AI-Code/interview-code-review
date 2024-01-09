import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_user_data(user_id):
    # Connect to the database
    conn = sqlite3.connect("users.db")
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    # Fetch user data from the database
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    user_data = cursor.fetchone()

    # Close the database connection
    conn.close()

    return user_data


def calculate_age(birth_year, current_year):
    # Calculate age based on birth year and current year
    age = current_year - birth_year
    return age


def main():
    user_id = input("Enter user ID: ")
    user_data = get_user_data(user_id)

    if user_data:
        # Assume birth year is stored in the database
        user_birthdate = user_data["birthdate"]
        birth_year = user_birthdate.split("-")[0]
        current_year = 2023

        age = calculate_age(birth_year, current_year)
        print(f"The user's age is: {age}")
    else:
        print("User not found in the database")


if __name__ == "__main__":
    main()
