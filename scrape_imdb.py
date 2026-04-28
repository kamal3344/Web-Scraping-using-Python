# scrape_imdb.py
# Complete script to scrape IMDb Top 250 movie ratings using Python
# Libraries: BeautifulSoup, Requests, Pandas
# Reference: https://www.geeksforgeeks.org/python/scrape-imdb-movie-rating-using-python/

from bs4 import BeautifulSoup
import requests
import pandas as pd

# -------------------------------------------------------
# Step 1: Downloading IMDb Top 250 movie data
# -------------------------------------------------------
url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# -------------------------------------------------------
# Step 2: Extract all movie containers
# Each li tag represents a movie block
# -------------------------------------------------------
movies = soup.select("li.ipc-metadata-list-summary-item")

# -------------------------------------------------------
# Step 3: Create a list to store movie details
# -------------------------------------------------------
movie_data = []

# -------------------------------------------------------
# Step 4: Loop through each movie block and extract info
# -------------------------------------------------------
for movie in movies:
    title = movie.select_one("h3.ipc-title__text").text.strip()
        year = movie.select_one("span.cli-title-metadata-item").text.strip()
            rating_tag = movie.select_one("span.ipc-rating-star--rating")
                rating = rating_tag.text.strip() if rating_tag else "N/A"
                    movie_data.append({
                            "Title": title,
                                    "Year": year,
                                            "Rating": rating
                                                })

                                                # -------------------------------------------------------
                                                # Step 5: Print movie data in terminal
                                                # -------------------------------------------------------
                                                for movie in movie_data:
                                                    print(f"{movie['Title']} ({movie['Year']}) - Rating: {movie['Rating']}")

                                                    # -------------------------------------------------------
                                                    # Step 6: Save the list as a DataFrame and export to CSV
                                                    # -------------------------------------------------------
                                                    df = pd.DataFrame(movie_data)
                                                    df.to_csv("imdb_top_250_movies.csv", index=False)
                                                    print("IMDb data saved successfully to imdb_top_250_movies.csv!")
                                                    
