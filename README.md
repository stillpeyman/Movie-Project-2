# Movie Database CLI

This is a Python-based command-line interface (CLI) application for managing a movie database. Users can add, delete, update, and list movies along with their ratings. The program also provides statistics, random movie selection, search functionality, sorting options, and a visual representation of movie ratings.

## Features
- List all movies with their ratings
- Add new movies with ratings
- Delete existing movies
- Update movie ratings
- View movie statistics (average, median, best, and worst movies)
- Get a random movie suggestion
- Search for movies with fuzzy matching
- Sort movies by rating (descending order)
- Generate a bar chart of movie ratings

## Installation
### Prerequisites
Ensure you have Python installed on your system. This project requires Python 3.13.0

### Install Required Libraries
The script uses external libraries that need to be installed before running. Install them using:
```bash
pip install matplotlib fuzzywuzzy python-Levenshtein
```

## Usage
1. Clone this repository or download the script.
2. Navigate to the project directory.
3. Run the script using:
```bash
python movie_database.py
```
4. Follow the on-screen menu instructions.

## Menu Options
```
Menu:
1. List Movies
2. Add Movie
3. Delete Movie
4. Update Movie
5. Stats
6. Random Movie
7. Search Movie
8. Movies Sorted by Rating
9. Create Rating Histogram
```
Simply enter the corresponding number to perform an action.

## Example Usage
- To add a new movie, enter `2`, provide the movie name, and input a rating.
- To search for a movie, enter `7` and type part of the movie title.
- To visualize ratings, select `9` to generate a bar chart.

## Contributing
Feel free to fork this repository and submit pull requests with improvements or new features.

## License
This project is open-source and available under the MIT License.

## Author
Developed by Peyman Farahani – SDE Trainee and film nerd. 

