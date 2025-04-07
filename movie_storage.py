import json


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    with open("movie_database.json", "r") as handle:
        movies_data = json.loads(handle.read())

    return movies_data


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
    with open("movie_database.json", "r") as handle:
        movies_data = json.load(handle)

    movies_data[title] = {
        "rating": rating,
        "year": year
    }

    with open("movie_database.json", "w") as handle:
        json.dump(movies_data, handle, indent=4)


def delete_movie(title):
    """
    Deletes a movie from the movie database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
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
    with open("movie_database.json", "r") as handle:
        movies_data = json.load(handle)

    movies_data[title]["rating"] = rating

    with open("movie_database.json", "w") as handle:
        json.dump(movies_data, handle, indent=4)

