import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Spotify Dataset
csv_file = "spotifydataset.csv"  

# Task 1: Load and Explore the Dataset Safely
try:
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"File '{csv_file}' does not exist.")
    
    df = pd.read_csv(csv_file)
    print("Dataset loaded successfully.\n")
    
    # Show first few rows
    print("First few rows of the dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Drop rows with any missing values
    df_clean = df.dropna()
    print(f"\nRows after dropping missing data: {len(df_clean)}")

except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
    exit()

except pd.errors.ParserError as pe:
    print(f"Error parsing the CSV file: {pe}")
    exit()

except Exception as e:
    print(f"An unexpected error occurred while loading the dataset: {e}")
    exit()


# Task 2: Basic Data Analysis
try:
    print("\nBasic Statistics:")
    print(df_clean.describe())

    print("\nAverage Track Popularity by Explicit Content:")
    grouped = df_clean.groupby('explicit')['track_popularity'].mean()
    print(grouped)

except KeyError as ke:
    print(f"Missing expected column: {ke}")
except Exception as e:
    print(f"An error occurred during analysis: {e}")


# Task 3: Data Visualization
sns.set(style="whitegrid")

try:
    # Ensure date format is correct
    df_clean['release_date'] = pd.to_datetime(df_clean['release_date'], errors='coerce')
    df_time = df_clean.dropna(subset=['release_date'])
    df_time = df_time.groupby('release_date')['track_popularity'].mean().reset_index().sort_values('release_date')

    # 1. Line Chart: Popularity over time
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='release_date', y='track_popularity', data=df_time)
    plt.title("Average Track Popularity Over Time")
    plt.xlabel("Release Date")
    plt.ylabel("Track Popularity")
    plt.tight_layout()
    plt.show()

    # 2. Bar Chart: Average danceability by mode
    plt.figure(figsize=(6, 4))
    sns.barplot(x='mode', y='danceability', data=df_clean)
    plt.title("Average Danceability by Mode")
    plt.xlabel("Mode (1=Major, 0=Minor)")
    plt.ylabel("Danceability")
    plt.tight_layout()
    plt.show()

    # 3. Histogram: Distribution of energy
    plt.figure(figsize=(6, 4))
    sns.histplot(df_clean['energy'], bins=20, kde=True)
    plt.title("Distribution of Energy")
    plt.xlabel("Energy")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # 4. Scatter Plot: Energy vs Danceability
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='energy', y='danceability', hue='explicit', data=df_clean)
    plt.title("Energy vs Danceability")
    plt.xlabel("Energy")
    plt.ylabel("Danceability")
    plt.tight_layout()
    plt.show()

except KeyError as ke:
    print(f"Column missing for visualization: {ke}")

except Exception as e:
    print(f"Error during visualization: {e}")
