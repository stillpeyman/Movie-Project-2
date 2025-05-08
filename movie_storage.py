import json


MOVIE_DB_FILE = "movie_database.json"


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data. If the file is not found
    return an empty dictionary.
    """
    try:
        with open(MOVIE_DB_FILE, "r") as handle:
            movies_data = json.load(handle)
        return movies_data

    except FileNotFoundError:
        return {}


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open(MOVIE_DB_FILE, "w") as handle:
        json.dump(movies, handle, indent=4)


def add_movie(title, year, rating):
    """
    Adds a movie to the movie database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies_data = get_movies()

    # Add new movie to movies_data dict
    movies_data[title] = {
        "rating": rating,
        "year": year
    }

    # Save movie data to JSON file
    save_movies(movies_data)


def delete_movie(title):
    """
    Deletes a movie from the movie database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies_data = get_movies()
    if title not in movies_data:
        return

    del movies_data[title]
    save_movies(movies_data)


def update_movie(title, rating):
    """
    Updates a movie from the movie database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies_data = get_movies()
    if title not in movies_data:
        return

    movies_data[title]["rating"] = rating
    save_movies(movies_data)

