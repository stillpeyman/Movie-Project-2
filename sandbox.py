import random

# def add_movie(movies):
#     """
#     This function prompts the user to add a new movie
#     and its rating to the dictionary 'movies'.
#     """
#     while True:
#         new_movie = input(f"Enter new movie name: ").title()
#
#         # any() returns True or False if new_movie exists in movies
#         if any(movie["title"] == new_movie for movie in movies):
#             print(f"Movie {new_movie} already exists! Try again.")
#             continue
#
#         try:
#             rating_input = input("Enter new movie rating (0-10): ")
#             new_rating = float(rating_input.replace(",", "."))
#             if not (0 <= new_rating <= 10):
#                 print("Invalid rating! Please enter a number between 0 and 10.")
#                 continue
#         except ValueError:
#             print("Invalid rating! Please enter a number between 0 and 10.")
#
#         try:
#             year_input = int(input("Enter year of release: "))
#         except ValueError:
#             print("Invalid year! Please enter a valid number.")
#             continue
#
#         movies.append({"title": new_movie, "rating": new_rating, "year": year_input})
#         print(f"Movie {new_movie} successfully added")
#         break
#
#
# def delete_movie(movies):
#     """
#     This function prompts the user to enter a movie name to delete,
#     checks if the title exists in the 'movies' dictionary and deletes it.
#     """
#     movie_to_delete = input(f"{GREEN}Enter movie name to delete: {RESET}").title()
#
#     """
#     EXPLAIN next() in plain English: Look through the list movies (list of dicts)
#     and find the first movie (which is a dict) where the value of its title key matches
#     movie_to_delete. If such a movie is found, assign it to the variable movie_to_remove.
#     If no match is found, return None instead of raising an error.
#
#     SYNTAX: next(iterable, default)
#
#     NOTE 1:
#     If default-argument, the value that next() returns if the iterator has been exhausted
#     (meaning: no more items left to iterate), NOT PROVIDED a StopIteration exception is raised.
#
#     NOTE 2:
#     any() won't work because it ONLY RETURNS True or False and won't return
#     the actual dictionary object.
#
#     NOTE 3:
#     next() CAN'T HANDLE DUPLICATES well so if multiple movies with the same title,
#     only the first one will be returned.
#     A FOR LOOP e.g. would check every element before and after match found or removal of
#     item but this could prove INEFFICIENT FOR LONG LISTS:
#
#     for movie in movies:
#         if movie_to_delete == movie["title"]:
#             movies.remove(movie)
#             print(f"Movie {movie_to_delete} successfully deleted")
#             break
#
#     """
#     # more efficient, clean, no break needed
#     movie_to_remove = next((movie for movie in movies if movie["title"] == movie_to_delete), None)
#
#     if movie_to_remove:
#         movies.remove(movie_to_remove)
#         print(f"Movie {movie_to_delete} successfully deleted")
#
#     else:
#         print(f"Movie {movie_to_delete} doesn't exist!")
#
#
# movies = [
#         {"title": "The Shawshank Redemption", "rating": 9.5, "year": 1994},
#         {"title": "Pulp Fiction", "rating": 8.8, "year": 1994},
#         {"title": "The Room", "rating": 3.6, "year": 2015},
#         {"title": "The Godfather", "rating": 9.2, "year": 1972},
#         {"title": "The Godfather: Part II", "rating": 9.0, "year": 1974},
#         {"title": "The Dark Knight", "rating": 9.0, "year": 2008},
#         {"title": "12 Angry Men", "rating": 8.9, "year": 1957},
#         {"title": "Everything Everywhere All At Once", "rating": 8.9, "year": 2022},
#         {"title": "Forrest Gump", "rating": 8.8, "year": 1994},
#         {"title": "Star Wars: Episode V", "rating": 8.7, "year": 1980}
#     ]

# add_movie(movies)


"""             SEE BELOW THE NEW <MOVIES> DATA STRUCTURE             """

# def get_movie_stats(movies):
#     """
#     This function takes the 'movies' dictionary and
#     prints the average and median rating as well as the
#     best and the worst rated movie.
#     """
#     sorted_ratings = sorted(movie["rating"] for movie in movies.values())
#     print(sorted_ratings)
#
#     average_rating = sum(sorted_ratings) / len(sorted_ratings)
#     print(f"Average rating: {round(average_rating, 2)}")
#
#     if len(sorted_ratings) % 2 == 0:
#
#         mid_index2 = len(sorted_ratings) // 2
#         mid_index1 = (len(sorted_ratings) // 2) - 1
#         median_rating_even_list = (sorted_ratings[mid_index2] + sorted_ratings[mid_index1]) / 2
#         print(f"Median rating: {median_rating_even_list}")
#
#     else:
#         mid_index = len(sorted_ratings) // 2
#         median_rating_odd_list = sorted_ratings[mid_index]
#         print(f"Median rating: {median_rating_odd_list}")
#
#     best_movie = []
#     best_rating = -1
#     for movie, movie_info in movies.items():
#         if movie_info["rating"] > best_rating:
#             best_rating = movie_info["rating"]
#             best_movie = [movie]
#         elif movie_info["rating"] == best_rating:
#             best_movie.append(movie)
#
#     if len(best_movie) == 1:
#         print(f"Best movie: {best_movie[0]}, {best_rating}")
#
#     else:
#         best_movie_str = ""
#         for movie in best_movie:
#             best_movie_str += f"{movie}, {best_rating}; "
#
#         best_movie_str = best_movie_str.rstrip("; ")
#         print(f"Best movies: {best_movie_str}")
#
#     worst_movie = []
#     worst_rating = 10
#     for movie, movie_info in movies.items():
#         if movie_info["rating"] < worst_rating:
#             worst_rating = movie_info["rating"]
#             worst_movie = [movie]
#
#         elif movie_info["rating"] == worst_rating:
#             worst_movie.append(movie)
#
#     if len(worst_movie) == 1:
#         print(f"Worst movie: {worst_movie[0]}, {worst_rating}")
#
#     else:
#         worst_movie_str = ""
#         for movie in worst_movie:
#             worst_movie_str += f"{movie}, {worst_rating}; "
#
#         worst_movie_str = worst_movie_str.rstrip("; ")
#         print(f"Worst movies: {worst_movie_str}")


# def sort_movies_desc(movies):
#     """
#     This function converts the 'movies' dictionary
#     into list of tuples, each tuple holds movie title
#     and movie rating, and then sorts the list of movies
#     by movie rating in descending order.
#     """
#     sorted_movie_list = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)
#     for movie in sorted_movie_list:
#         print(f"{movie[0]}: {movie[1]["rating"]}")
#
#
# # new data structure: dict of dicts:
# movies = {
#     "The Shawshank Redemption": {"rating": 9.5, "year": 1994},
#     "Pulp Fiction": {"rating": 8.8, "year": 1994},
#     "The Room": {"rating": 3.6, "year": 2015},
#     "The Godfather": {"rating": 9.2, "year": 1972},
#     "The Godfather: Part II": {"rating": 9.0, "year": 1974},
#     "The Dark Knight": {"rating": 9.0, "year": 2008},
#     "12 Angry Men": {"rating": 8.9, "year": 1957},
#     "Everything Everywhere All At Once": {"rating": 8.9, "year": 2022},
#     "Forrest Gump": {"rating": 8.8, "year": 1994},
#     "Star Wars: Episode V": {"rating": 8.7, "year": 1980}
# }
#
# print(movies.items())
# print()
# print(movies.keys())
# print()
# print(movies.values())


