import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Function to load datasets
def load_datasets(filepaths):
    return {name: pd.read_csv(filepath) for name, filepath in filepaths.items()}

# Function to standardize movie titles
def standardize_titles(title_series):
    return title_series.str.lower().str.strip().str.replace(r"[^\w\s]", "", regex=True)

# Function to find best matches for each title
def find_best_matches(cosine_sim, titles_first, titles_second, threshold=0.5):
    matches = []
    for idx, row in enumerate(cosine_sim):
        best_match_idx = np.argmax(row)
        if row[best_match_idx] >= threshold:
            matches.append((titles_first[idx], titles_second[best_match_idx], row[best_match_idx]))
    return matches

# Load datasets
filepaths = {
    "goldenglobes": "datasets/goldenglobes.csv",
    "oscars": "datasets/oscars.csv",
    "sag": "datasets/sag.csv"
}
datasets = load_datasets(filepaths)

# Standardize titles
for name, data in datasets.items():
    title_column = 'film' if 'film' in data.columns else 'show'
    data['standardized_title'] = standardize_titles(data[title_column])
    data['standardized_title'].fillna("", inplace=True)

# Extracting standardized titles
titles_goldenglobes = datasets['goldenglobes']['standardized_title'].unique()
titles_oscars = datasets['oscars']['standardized_title'].unique()

# Vectorize titles
vectorizer = TfidfVectorizer(min_df=1, analyzer='char', ngram_range=(1,3))
all_titles = np.concatenate((titles_goldenglobes, titles_oscars))
tfidf_matrix_all = vectorizer.fit_transform(all_titles)

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix_all[:len(titles_goldenglobes)], tfidf_matrix_all[len(titles_goldenglobes):])

# Find matches
matches = find_best_matches(cosine_sim, titles_goldenglobes, titles_oscars, threshold=0.7)

# Create DataFrame for matches
matches_df = pd.DataFrame(matches, columns=['Title_GoldenGlobes', 'Title_Oscars', 'Similarity'])
matches_df['Verification'] = ''  # Column for manual verification

# Aggregating data in case of duplicate titles
goldenglobes_agg = datasets['goldenglobes'].groupby('standardized_title').agg({'year_film': 'first'})
oscars_agg = datasets['oscars'].groupby('standardized_title').agg({'year_film': 'first'})

# Map the aggregated year data to the matches DataFrame
matches_df['Year_GG'] = matches_df['Title_GoldenGlobes'].map(goldenglobes_agg['year_film'])
matches_df['Year_Oscars'] = matches_df['Title_Oscars'].map(oscars_agg['year_film'])


matches_df.to_csv("matches_verification.csv", index=False)
