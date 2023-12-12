import pandas as pd

# Function to standardize movie titles
def standardize_titles(title_series):
    return title_series.str.lower().str.strip().str.replace(r"[^\w\s]", "", regex=True)

# Load the datasets
goldenglobes_df = pd.read_csv('datasets/goldenglobes.csv')
oscars_df = pd.read_csv('datasets/oscars.csv')
matches_verification_df = pd.read_csv('matches_verification_gg_oscar.csv')

# Apply the standardize_titles function to the 'film' column of both datasets
goldenglobes_df['standardized_film_goldenglobes'] = standardize_titles(goldenglobes_df['film'])
oscars_df['standardized_film_oscars'] = standardize_titles(oscars_df['film'])

# Filter matches_verification_df for verified matches
verified_matches_df = matches_verification_df[matches_verification_df['Verification'] == True]

# Merging goldenglobes_df with the verified matches
merged_goldenglobes = pd.merge(verified_matches_df, goldenglobes_df,
                               left_on='Title_GoldenGlobes', right_on='standardized_film_goldenglobes',
                               how='inner')

# Merging oscars_df with the merged_goldenglobes
final_merged_df = pd.merge(merged_goldenglobes, oscars_df,
                           left_on='Title_Oscars', right_on='standardized_film_oscars',
                           how='inner')

final_merged_df = final_merged_df.loc[:,~final_merged_df.columns.duplicated()]

final_merged_df.to_csv('final_merged_df.csv', index=False)