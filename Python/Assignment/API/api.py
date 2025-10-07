import os
import requests
import time

def get_github_users_details():
    try:
        name = input("Enter a GitHub username: ")
        print(f"\nFetching details for '{name}'...\n")
        time.sleep(0.3)
        response = requests.get(f"https://api.github.com/users/{name}")
        response.raise_for_status()
        user_data = response.json()
    except Exception as e:
        print(f"Error occurred while fetching details: {e}")
        return
    print(f"Keys: {user_data.keys()}")
    log_entry = f"{user_data.get('login')}: {user_data.get('name')} | Repos: {user_data.get('public_repos')} | Followers: {user_data.get('followers')}\n"

    if os.path.exists("logger.txt"):
        with open("logger.txt", "r+") as file:
            file.seek(0)
            existing_logins = [line.split(":")[0].strip() for line in file if ":" in line]
            if user_data.get("login") in existing_logins:
                print("User already logged.")
                return
            file.write(log_entry)
    else:
        with open("logger.txt", "w") as file:
            file.write(log_entry)

    print("User details logged successfully.")

get_github_users_details()