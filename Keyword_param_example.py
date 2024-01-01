# Examples of Using Keyword parameters
# Write a function that will return number of words that have X length, given a string
"""def get_count_of_small_words(input_string, max_size=3):
    small_words = []
    for word in input_string.split():
        if len(word) <= max_size:
            small_words.append(word)
    return len(small_words)

my_joke = "Why did the soccer player take so long to eat dinner? Because he thought he couldn’t use his hands."
num_small = get_count_of_small_words(my_joke)
print(num_small)
"""
# example 2
def connect_to_database(host="test.db.com", username="testusr", password="testpass"):
    print(f"Connection to host: {host}")
    print(f"Username: {username}")
    # Additional logic for connecting to the database can be added here

def def_connect_to_database(host="test.db.com", username="testusr", password="testpass"):
    print(f"Connection to host: {host}")
    print(f"Username: {username}")
    # Additional logic for connecting to the database can be added here

def_connect_to_database()  # Calling the function with default arguments

def_connect_to_database("prod.db.com", "username", "secrete")  # Calling the function with specific arguments
