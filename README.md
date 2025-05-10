# PLP-Python-Week-7-Assignment

# 🎵 Music Dataset Analysis

This project performs a complete analysis and visualization of a music dataset using Python. The dataset contains information about songs and artists on Spotify, including metadata like track popularity, artist followers, audio features (energy, danceability, tempo), and more.

---

## Dataset Link: https://www.kaggle.com/datasets/glowstudygram/spotify-songs-and-artists-dataset/data
## 📁 Dataset Overview

The dataset includes the following columns:

- `artist_name` – Name of the artist  
- `genres` – Music genres  
- `followers` – Number of Spotify followers  
- `artist_popularity` – Artist popularity score (0-100)  
- `artist_url` – Link to the Spotify artist page  
- `track_name` – Song title  
- `album_name` – Album name  
- `release_date` – Song release date  
- `duration_ms` – Duration in milliseconds  
- `explicit` – Whether the track contains explicit content  
- `track_popularity` – Track popularity score  
- `danceability` – Dance suitability  
- `energy` – Intensity and activity level  
- `key`, `mode` – Musical key and mode (Major/Minor)  
- `loudness`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo` – Various audio and musical features

---

## 🧠 Tasks Covered

### ✅ Task 1: Load and Explore the Dataset
- Load dataset using pandas
- View first few rows
- Identify missing data and data types
- Clean missing values

### ✅ Task 2: Basic Data Analysis
- Calculate descriptive statistics
- Group songs by explicit content and analyze average popularity

### ✅ Task 3: Data Visualization
Using `matplotlib` and `seaborn`:
- 📈 **Line Chart**: Track popularity over time  
- 📊 **Bar Chart**: Danceability by musical mode (Major/Minor)  
- 📉 **Histogram**: Energy distribution  
- ⚫ **Scatter Plot**: Relationship between energy and danceability  

---

## 🛠️ How to Run

1. Clone the repository or download the script.
2. Install required packages (if not already installed):
   ```bash
   pip install pandas matplotlib seaborn
