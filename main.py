import random
import matplotlib.pyplot as plt
from fuzzywuzzy import process
import movie_storage as ms


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


def user_menu_input():
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

        if user_input == "0":
            print("Bye!")
            break

        if user_input in user_choices:
            # basically calling the function with <movies> as arg
            user_choices[user_input]()
            input("\nPress enter to continue")

        else:
            print(f"{RED}Invalid choice{RESET}")
            continue


def list_movies():
    """
    This function takes the dictionary 'movies'
    and lists all the movies with their ratings.
    """
    movies = ms.get_movies()

    print(f"{len(movies)} movies in total:")
    for movie_title, movie_info in movies.items():
        print(f"{movie_title} ({movie_info['year']}): {movie_info['rating']}")


def add_movie():
    """
    This function prompts the user to add a new movie
    and its rating to the dictionary 'movies'.
    """
    movies = ms.get_movies()

    while True:
        new_title = input(f"{GREEN}Enter new movie name: {RESET}").title()

        # check if title is empty string
        if not new_title.strip():
            print(f"{RED}Invalid input! Title cannot be empty.{RESET}")
            continue

        if any(movies[movie_title] == new_title for movie_title in movies):
            print(f"{RED}Movie {new_title} already exists! Try again.{RESET}")
            continue

        # default initialization
        new_rating = None
        while True:
            rating_input = input(f"{GREEN}Enter new movie rating (0-10): {RESET}")

            try:
                new_rating = float(rating_input.replace(",", "."))
                if not 0 <= new_rating <= 10:
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

        ms.add_movie(new_title, new_year, new_rating)
        print(f"Movie {new_title} successfully added")
        break


def delete_movie():
    """
    This function prompts the user to enter a movie name to delete,
    checks if the title exists in the 'movies' dictionary and deletes it.
    """
    movies = ms.get_movies()

    while True:
        user_input = input(f"{GREEN}Enter movie name to delete: {RESET}").title()

        # check if title is empty string
        if not user_input.strip():
            print(f"{RED}Invalid input! Title cannot be empty.{RESET}")
            continue

        # check if movie exists
        if user_input in movies:
            ms.delete_movie(user_input)
            print(f"Movie {user_input} successfully deleted")
            break

        print(f"{RED}Movie {user_input} doesn't exist!{RESET}")


def update_movie():
    """
    This function prompts the user to enter a movie name,
    checks if the movie exists in the 'movies' dictionary,
    and allows the user to update its rating.
    """
    movies = ms.get_movies()

    while True:
        movie_to_update = input(f"{GREEN}Enter movie name: {RESET}").title()

        # check if title is empty string
        if not movie_to_update.strip():
            print(f"{RED}Invalid input! Title cannot be empty.{RESET}")
            continue

        if movie_to_update not in movies:
            print(f"{RED}Movie {movie_to_update} doesn't exist!{RESET}")
            continue

        while True:
            try:
                rating_input = input(f"{GREEN}Enter new movie rating (0-10): {RESET}")
                new_rating = float(rating_input.replace(",", "."))
                if not 0 <= new_rating <= 10:
                    print(f"{RED}Invalid rating! Please enter a number between 0 and 10.{RESET}")
                    continue

                ms.update_movie(movie_to_update, new_rating)
                print(f"Movie {movie_to_update} successfully updated")
                break

            except ValueError:
                print(f"{RED}Invalid rating! Please enter a number between 0 and 10.{RESET}")

        break


def get_movie_stats():
    """
    This function takes the 'movies' dictionary and
    prints the average and median rating as well as the
    best and the worst rated movie.
    """
    movies = ms.get_movies()

    sorted_ratings = sorted(movie_info["rating"] for movie_info in movies.values())

    average_rating = sum(sorted_ratings) / len(sorted_ratings)
    print(f"Average rating: {round(average_rating, 2)}")

    ratings_count = len(sorted_ratings)
    mid_index = ratings_count // 2

    if ratings_count % 2 == 0:
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


def get_random_movie():
    """
    This function uses the random module to get a random movie
    from the 'movies' dictionary as a suggestion to watch.
    """
    movies = ms.get_movies()

    convert_database_to_tuple = list(movies.items())
    random_selection = random.choice(convert_database_to_tuple)
    print(f"Your movie for tonight: {random_selection[0]}, it's rated {random_selection[1]['rating']}.")


def search_movie():
    """
    This function prompts the user to enter part of the movie
    name and searches for it in the 'movies' dictionary using
    fuzzymatch module for fuzzy string matching.
    """
    movies = ms.get_movies()

    while True:
        search_input = input(f"{GREEN}Enter part of the movie name: {RESET}").casefold()

        # check for empty string
        if not search_input.strip():
            print(f"{RED}Invalid input! Title cannot be empty.{RESET}")
            continue

        break

    # fuzzymatch module: using process.extract() to get best matches
    best_matches = process.extract(search_input, movies.keys(), limit=5)

    # manually filter matches based on score threshold
    filtered_matches = [(movie, score) for movie, score in best_matches if score >= 70]

    if filtered_matches:
        for movie, score in filtered_matches:
            print(f"{movie} ({movies[movie]['year']}): {movies[movie]['rating']}")

    else:
        print(f"{RED}No matches found{RESET}")


def sort_movies_desc():
    """
    This function converts the 'movies' dictionary
    into list of tuples, each tuple holds movie title
    and movie rating, and then sorts the list of movies
    by movie rating in descending order.
    """
    movies = ms.get_movies()

    sorted_movie_list = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)

    for movie in sorted_movie_list:
        print(f"{movie[0]}: {movie[1]['rating']}")


def create_rating_bar():
    """
    This function takes the 'movies' dictionary and
    creates a bar chart based on the movie ratings
    using the matplotlib module.
    """
    movies = ms.get_movies()

    movie_titles = list(movies.keys())
    movie_ratings = [movie_info["rating"] for movie_info in movies.values()]

    # BAR CHART: movies_titles on x-axis, movie_ratings on y-axis
    plt.bar(movie_titles, movie_ratings, color="blue", edgecolor="black")

    # <movie_info> replaced by <_> since not used in this loop
    for movie_title, _ in movies.items():
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

    # save the bar chart as PDF, <bbox_inches> (optional) trims extra white space around the figure
    plt.savefig("movie_ratings_chart.pdf", bbox_inches="tight")
    plt.show()


def main():
    """
    Prints 'My Movies Database' and displays the menu for user interaction.
    """
    print(f"{BLUE}{10 * '*'} My Movies Database {10 * '*'}{RESET}")
    user_menu_input()


if __name__ == "__main__":
    main()
