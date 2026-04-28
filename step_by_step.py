# step_by_step.py
# Step-by-step breakdown of scraping IMDb movie ratings using Python
# Each step is isolated and explained with comments
# Reference: https://www.geeksforgeeks.org/python/scrape-imdb-movie-rating-using-python/

# ============================================================
# STEP 1: Import the required modules
# ============================================================
from bs4 import BeautifulSoup
import requests
import pandas as pd

print("Step 1: Modules imported successfully.")

# ============================================================
# STEP 2: Access the HTML content from the IMDb Top 250 page
# ============================================================
url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(f"Step 2: Page fetched. Status code: {response.status_code}")

# ============================================================
# STEP 3: Extract movie details using HTML tags
# Each li tag represents a movie block containing
# title, year, and rating details.
# ============================================================
movies = soup.select("li.ipc-metadata-list-summary-item")

print(f"Step 3: Found {len(movies)} movie entries on the page.")

# ============================================================
# STEP 4: Create a list to store movie data
# Loop through each movie and extract Title, Year, Rating
# ============================================================
movie_data = []

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

print(f"Step 4: Extracted data for {len(movie_data)} movies.")

# ============================================================
# STEP 5: Display the extracted data
# ============================================================
print("\nStep 5: Displaying extracted movie data:")
print("-" * 50)
for movie in movie_data:
      print(f"{movie['Title']} ({movie['Year']}) - Rating: {movie['Rating']}")

# ============================================================
# STEP 6: Save the data into a CSV file
# ============================================================
df = pd.DataFrame(movie_data)
df.to_csv("imdb_top_250_movies.csv", index=False)
print("\nStep 6: IMDb data saved successfully to imdb_top_250_movies.csv!")
print(f"Total rows in CSV: {len(df)}")
print("Columns:", list(df.columns))
