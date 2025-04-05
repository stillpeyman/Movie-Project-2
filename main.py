import random
import matplotlib.pyplot as plt
from fuzzywuzzy import process


# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"


def print_menu():
    """This function prints the menu of
    'My Movies Database', a list of actions.
    """
    menu_text = """
Menu: 
0. Exit
1. List Movies
2. Add Movie
3. Delete Movie
4. Update Movie
5. Stats
6. Random Movie
7. Search Movie
8. Movies Sorted by rating
9. Create rating Histogram
"""
    blue_menu_text = f"{BLUE}{menu_text}{RESET}"
    print(blue_menu_text)


def user_menu_input(movies):
    """
    This function displays a menu and handles user input to perform actions
    on a movie collection. The function continuously prompts the user for a choice,
    executes the corresponding function from the menu, and waits for user confirmation
    before displaying the menu again.
    """
    user_choices = {
        "1": list_movies,
        "2": add_movie,
        "3": delete_movie,
        "4": update_movie,
        "5": get_movie_stats,
        "6": get_random_movie,
        "7": search_movie,
        "8": sort_movies_desc,
        "9": create_rating_bar
    }

    while True:
        print_menu()
        user_input = input(f"{GREEN}Enter choice (0-9): {RESET}").strip()
        # Ignore empty input
        if not user_input:
            continue

        elif user_input == "0":
            print("Bye!")
            break

        elif user_input in user_choices:
            user_choices[user_input](movies)
            input("\nPress enter to continue")

        else:
            print(f"{RED}Invalid choice{RESET}")
            continue


def list_movies(movies):
    """
    This function takes the dictionary 'movies'
    and lists all the movies with their ratings.
    """
    print(f"{len(movies)} movies in total")
    for movie_title in movies:
        print(f"{movies[movie_title]} ({movie_title["year"]}): {movie_title["rating"]}")


def add_movie(movies):
    """
    This function prompts the user to add a new movie
    and its rating to the dictionary 'movies'.
    """
    while True:
        new_title = input(f"{GREEN}Enter new movie name: {RESET}").title()

        if any(movies[movie_title] == new_title for movie_title in movies):
            print(f"{RED}Movie {new_title} already exists! Try again.{RESET}")
            continue

        while True:
            try:
                rating_input = input(f"{GREEN}Enter new movie rating (0-10): {RESET}")
                new_rating = float(rating_input.replace(",", "."))
                if not (0 <= new_rating <= 10):
                    print(f"{RED}Invalid rating! Please enter a number between 0 and 10.{RESET}")
                    continue
                break

            except ValueError:
                print(f"{RED}Invalid rating! Please enter a number between 0 and 10.{RESET}")
                continue

        while True:
            try:
                new_year = int(input(f"{GREEN}Enter year of release: {RESET}"))
                break

            except ValueError:
                print(f"{RED}Invalid year! Please enter a valid number.{RESET}")

        movies[new_title] = {
            "rating": new_rating,
            "year": new_year
        }

        print(f"Movie {new_title} successfully added")
        break


def delete_movie(movies):
    """
    This function prompts the user to enter a movie name to delete,
    checks if the title exists in the 'movies' dictionary and deletes it.
    """
    while True:
        user_input = input(f"{GREEN}Enter movie name to delete: {RESET}").title()
        movie_to_delete = next((movie_title for movie_title in movies if movies[movie_title] == user_input), None)

        if movie_to_delete:
            del movies[movie_to_delete]
            print(f"Movie {movie_to_delete} successfully deleted")
            break

        else:
            print(f"{RED}Movie {user_input} doesn't exist!{RESET}")


def update_movie(movies):
    """
    This function prompts the user to enter a movie name,
    checks if the movie exists in the 'movies' dictionary,
    and allows the user to update its rating.
    """
    while True:
        user_input = input(f"{GREEN}Enter movie name: {RESET}").title()
        movie_to_update = next((movie_title for movie_title in movies if movies[movie_title] == user_input), None)

        if not movie_to_update:
            print(f"{RED}Movie {user_input} doesn't exist!{RESET}")
            continue

        while True:
            try:
                rating_input = input(f"{GREEN}Enter new movie rating (0-10): {RESET}")
                new_rating = float(rating_input.replace(",", "."))
                if not (0 <= new_rating <= 10):
                    print(f"{RED}Invalid rating! Please enter a number between 0 and 10.{RESET}")
                    continue

                else:
                    movie_to_update["rating"] = new_rating
                    print(f"Movie {movie_to_update} successfully updated")
                    break

            except ValueError:
                print(f"{RED}Invalid rating! Please enter a number between 0 and 10.{RESET}")

        break


def get_movie_stats(movies):
    """
    This function takes the 'movies' dictionary and
    prints the average and median rating as well as the
    best and the worst rated movie.
    """
    sorted_ratings = sorted(movie["rating"] for movie in movies.values())

    average_rating = sum(sorted_ratings) / len(sorted_ratings)
    print(f"Average rating: {round(average_rating, 2)}")

    n = len(sorted_ratings)
    mid_index = n // 2

    if n % 2 == 0:
        median_rating = (sorted_ratings[mid_index - 1] + sorted_ratings[mid_index]) / 2
    else:
        median_rating = sorted_ratings[mid_index]

    print(f"Median rating: {median_rating}")

    best_rating = max(movie_info["rating"] for movie_info in movies.values())
    best_movies = [movie_title for movie_title, movie_info in movies.items() if movie_info["rating"] == best_rating]

    if len(best_movies) == 1:
        print(f"Best movie: {best_movies[0]}, {best_rating}")
    else:
        print(f"Best movies: {', '.join(best_movies)}, {best_rating}")

    worst_rating = min(movie_info["rating"] for movie_info in movies.values())
    worst_movies = [movie_title for movie_title, movie_info in movies.items() if movie_info["rating"] == worst_rating]

    if len(worst_movies) == 1:
        print(f"Best movie: {worst_movies[0]}, {worst_rating}")
    else:
        print(f"Best movies: {', '.join(worst_movies)}, {worst_rating}")


def get_random_movie(movies):
    """
    This function uses the random module to get a random movie
    from the 'movies' dictionary as a suggestion to watch.
    """
    convert_database_to_tuple = list(movies.items())
    random_selection = random.choice(convert_database_to_tuple)
    print(f"Your movie for tonight: {random_selection[0]}, it's rated {random_selection[1]["rating"]}.")


def search_movie(movies):
    """
    This function prompts the user to enter part of the movie
    name and searches for it in the 'movies' dictionary using
    fuzzymatch module for fuzzy string matching.
    """
    search_input = input(f"{GREEN}Enter part of the movie name: {RESET}").casefold()

    # fuzzymatch module: using process.extract() to get best matches
    best_matches = process.extract(search_input, movies.keys(), limit=5)

    # manually filter matches based on score threshold
    filtered_matches = []
    for match in best_matches:
        movie, score = match
        if score >= 70:
            filtered_matches.append(match)

    # if filtered matches, print them or print "No matches found"
    if filtered_matches:
        #print(filtered_matches)
        # filtered_matches = list of tuples, each tuple
        # contains movie title and match score
        for movie, score in filtered_matches:
            print(f"{movie}: {movies[movie]}")
            # print statement with match score
            # print(f"{movie}: {database[movie]} (Match score: {score})")

    else:
        print(f"{RED}No matches found{RESET}")


def sort_movies_desc(movies):
    """
    This function converts the 'movies' dictionary
    into list of tuples, each tuple holds movie title
    and movie rating, and then sorts the list of movies
    by movie rating in descending order.
    """
    sorted_movie_list = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)

    for movie in sorted_movie_list:
        print(f"{movie[0]}: {movie[1]["rating"]}")


def create_rating_bar(movies):
    """
    This function takes the 'movies' dictionary and
    creates a bar chart based on the movie ratings
    using the matplotlib module.
    """
    movie_titles = list(movies.keys())
    movie_ratings = [movie_info["rating"] for movie_info in movies.values()]

    # BAR CHART: movies (keys) on x-axis, ratings (values) on y-axis
    plt.bar(movie_titles, movie_ratings, color="blue", edgecolor="black")

    for movie_title, movie_info in movies.items():
        # used for x-position of each movie based on its index in list <movie_titles>
        # gives correct position on x-axis for placing label under or over the bar
        x_position = movie_titles.index(movie_title)
        plt.text(
            x_position,
            y=0.5, s=movie_title,
            ha="center",
            va="bottom",
            rotation=90,
            fontsize=9,
            c="white",
            weight="bold")

    # removes x-axis labels (here: movie titles) because plt.bar() does that by default
    plt.xticks([])
    plt.title("Movie rating Chart")
    plt.xlabel("Movies")
    plt.ylabel("rating")
    plt.show()


def main():
    """
    Initializes a movie database and displays the menu for user interaction.
    """
    movies = {
        "The Shawshank Redemption": {"rating": 9.5, "year": 1994},
        "Pulp Fiction": {"rating": 8.8, "year": 1994},
        "The Room": {"rating": 3.6, "year": 2015},
        "The Godfather": {"rating": 9.2, "year": 1972},
        "The Godfather: Part II": {"rating": 9.0, "year": 1974},
        "The Dark Knight": {"rating": 9.0, "year": 2008},
        "12 Angry Men": {"rating": 8.9, "year": 1957},
        "Everything Everywhere All At Once": {"rating": 8.9, "year": 2022},
        "Forrest Gump": {"rating": 8.8, "year": 1994},
        "Star Wars: Episode V": {"rating": 8.7, "year": 1980}
    }

    print(f"{BLUE}{10 * "*"} My Movies Database {10 * "*"}{RESET}")
    user_menu_input(movies)


if __name__ == "__main__":
    main()