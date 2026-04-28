# Web Scraping using Python

## Scrape IMDB Movie Ratings using Python

This repository contains Python code for scraping IMDB movie ratings using the **BeautifulSoup**, **Requests**, and **Pandas** libraries.

---

## Table of Contents

- [Overview](#overview)
- - [Modules Required](#modules-required)
  - - [Installation](#installation)
    - - [Step-by-Step Implementation](#step-by-step-implementation)
      - - [Files in this Repository](#files-in-this-repository)
        - - [Sample Output](#sample-output)
         
          - ---

          ## Overview

          We can scrape the IMDb movie ratings and their details with the help of the BeautifulSoup library of Python. This project demonstrates how to extract the IMDb Top 250 movies list including movie title, release year, and rating, and save the results to a CSV file.

          ---

          ## Modules Required

          | Module | Description |
          |--------|-------------|
          | `requests` | Used for making HTTP requests to a specified URL. Returns a response from the URI. |
          | `html5lib` | A pure-python library for parsing HTML, designed to conform to the WHATWG HTML specification. |
          | `bs4` (BeautifulSoup) | A web scraping framework for Python. Extracts data from HTML and XML files. |
          | `pandas` | A library built over NumPy providing data structures and operators to manipulate numerical data. |

          ---

          ## Installation

          Install the required libraries using pip:

          ```bash
          pip install requests html5lib beautifulsoup4 pandas
          ```

          ---

          ## Step-by-Step Implementation

          ### Step 1: Import the required modules

          ```python
          from bs4 import BeautifulSoup
          import requests
          import pandas as pd
          ```

          ### Step 2: Access the HTML content from the IMDb Top 250 movies page

          ```python
          url = 'https://www.imdb.com/chart/top/'
          response = requests.get(url)
          soup = BeautifulSoup(response.text, "html.parser")
          ```

          ### Step 3: Extract movie details using HTML tags

          Each `li` tag represents a movie block containing title, year, and rating details.

          ```python
          movies = soup.select("li.ipc-metadata-list-summary-item")
          ```

          ### Step 4: Create a list to store movie data

          ```python
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
          ```

          ### Step 5: Display the extracted data

          ```python
          for movie in movie_data:
              print(f"{movie['Title']} ({movie['Year']}) - Rating: {movie['Rating']}")
          ```

          ### Step 6: Save the data into a CSV file

          ```python
          df = pd.DataFrame(movie_data)
          df.to_csv("imdb_top_250_movies.csv", index=False)
          print("IMDb data saved successfully to imdb_top_250_movies.csv!")
          ```

          ---

          ## Files in this Repository

          | File | Description |
          |------|-------------|
          | `README.md` | Project documentation |
          | `scrape_imdb.py` | Complete script to scrape IMDb Top 250 movie ratings |
          | `step_by_step.py` | Step-by-step breakdown of the scraping process |

          ---

          ## Sample Output

          ```
          Title                          Year    Rating
          1. The Shawshank Redemption    N/A     9.3 (3.1M)
          2. The Godfather               N/A     9.2 (2.2M)
          3. The Dark Knight             N/A     9.1 (3.1M)
          4. The Godfather: Part II      N/A     9.0 (1.5M)
          5. 12 Angry Men                N/A     9.0 (955K)
          IMDb data saved successfully to imdb_top_250_movies.csv!
          ```

          A `.csv` file named `imdb_top_250_movies.csv` will also be saved in the same directory.

          ---

          ## Reference

          - [GeeksForGeeks - Web Scraping IMDB movie rating using Python](https://www.geeksforgeeks.org/python/scrape-imdb-movie-rating-using-python/)
          - - [IMDb Top 250 Movies](https://www.imdb.com/chart/top/)
            - 
