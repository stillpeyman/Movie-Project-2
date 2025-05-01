import json
import os


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    try:
        with open("movie_database.json", "r") as handle:
            movies_data = json.load(handle)
        return movies_data

    except FileNotFoundError:
        return None


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("movie_database.json", "w") as handle:
        json.dump(movies, handle, indent=4)


def add_movie(title, year, rating):
    """
    Adds a movie to the movie database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # Check if file exists, if not, create an empty database
    if not os.path.exists("movie_database.json"):
        movies_data = {}

    else:
        with open("movie_database.json", "r") as handle:
            movies_data = json.load(handle)

    # Add new movie to movies_data dict
    movies_data[title] = {
        "rating": rating,
        "year": year
    }

    # Save movie data to JSON file
    with open("movie_database.json", "w") as handle:
        json.dump(movies_data, handle, indent=4)


def delete_movie(title):
    """
    Deletes a movie from the movie database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # Check if file exists, if not, no data to delete
    if not os.path.exists("movie_database.json"):
        print("No movie database found.")
        return

    with open("movie_database.json", "r") as handle:
        movies_data = json.load(handle)

    del movies_data[title]

    with open("movie_database.json", "w") as handle:
        json.dump(movies_data, handle, indent=4)


def update_movie(title, rating):
    """
    Updates a movie from the movie database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # Check if file exists, if not, no data to update
    if not os.path.exists("movie_database.json"):
        print("No movie database found.")
        return

    with open("movie_database.json", "r") as handle:
        movies_data = json.load(handle)

    movies_data[title]["rating"] = rating

    with open("movie_database.json", "w") as handle:
        json.dump(movies_data, handle, indent=4)

