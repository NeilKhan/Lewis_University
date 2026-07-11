# Student Name - Neil Khan
# Date - 8 July 2026
# Program Description - Movie Collection Manager (Week 5 Assignment)
# Tier Level - Base Level


# Function 1 - Create movie dictionary.
def create_movie(title, year, genres, rating):
    movie = {
        "title": title,
        "year": year,
        "genres": genres,
        "rating": rating
    }

    return movie


# Function 2 - Display all movies in a formatted table.
def display_movies(movies, heading):
    print(f"\n{heading}")
    print("-" * 75)

    if len(movies) == 0:
        print("No movies in this collection.")
        return

    print(f'{"Title":30} {"Year":6} {"Genres":30} {"Rating":>6}')
    print("-" * 75)

    for movie in movies:
        genres = " / ".join(movie["genres"])

        print(f'{movie["title"]:30} '
              f'{movie["year"]:<6} '
              f'{genres:30} '
              f'{movie["rating"]:>6.1f}')


# Function 3 - Find top rated movies.
def find_top_rated(movies, n):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )

    return sorted_movies[:n]


# Function 4 - Get average rating.
def get_average_rating(movies):
    if len(movies) == 0:
        return 0.0

    total = 0

    for movie in movies:
        total += movie["rating"]

    average = total / len(movies)

    return round(average, 2)


# -------------------------
# Main Program
# -------------------------

# Movie collection dictionary
movies = [
    {
        "title": "Goodfellas",
        "year": 1990,
        "genres": ["Crime", "Drama"],
        "rating": 8.7
    },
    {
        "title": "Kung Fu Hustle",
        "year": 2004,
        "genres": ["Action", "Comedy", "Kung Fu"],
        "rating": 7.7
    },
    {
        "title": "Heat",
        "year": 1995,
        "genres": ["Action", "Crime", "Drama"],
        "rating": 8.3
    },
    {
        "title": "Back to the Future",
        "year": 1985,
        "genres": ["Adventure", "Comedy", "Sci-Fi"],
        "rating": 8.8
    },
    {
        "title": "John Wick: Chapter 2",
        "year": 2017,
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 7.4
    }
]

# Display starter collection
display_movies(movies, "Your Movie Collection")

# Prompt user to add two movies
for number in range(1, 3):
    print(f"\nEnter Movie #{number}")

    title = input("Title: ")
    year = int(input("Release year: "))

    genre_input = input("Genres (separated by commas): ")
    genres = [genre.strip() for genre in genre_input.split(",")]

    rating = float(input("Rating: "))

    new_movie = create_movie(title, year, genres, rating)

    movies.append(new_movie)

# Sort movie collection by year
movies.sort(key=lambda movie: movie["year"])

# Display sorted collection
display_movies(movies, "All Movies Sorted by Year")

# Find top three rated movies
top_movies = find_top_rated(movies, 3)

# Display top-rated movies
display_movies(top_movies, "Top 3 Rated Movies")

# Display average rating
average = get_average_rating(movies)

print(f"\nCollection average rating: {average:.2f}")