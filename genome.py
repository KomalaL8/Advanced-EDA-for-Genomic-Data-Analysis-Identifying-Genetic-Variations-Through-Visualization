

!pip install scikit-learn
!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install seaborn
!pip install scipy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from scipy.stats import ttest_ind, chi2_contingency, f_oneway

# Load dataset
file_path = 'igsr_HG01350_undefined.csv'
df = pd.read_csv(file_path, sep='\t')

# Check data structure
print("Dataset Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())

# Preprocessing: Handle Missing Values (if any)
# You can choose an appropriate strategy for handling missing values, such as:
# df.fillna(df.mean(), inplace=True)  # Replace with mean
# df.dropna(inplace=True)  # Remove rows with missing values

# Convert categorical data to numerical using OneHotEncoder
categorical_cols = df.select_dtypes(include=['object']).columns
ohe = OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore')  # Use sparse_output instead of sparse
categorical_encoded = ohe.fit_transform(df[categorical_cols])
categorical_encoded_df = pd.DataFrame(categorical_encoded, columns=ohe.get_feature_names_out(categorical_cols))

# Combine numerical and encoded categorical data
numerical_df = df.select_dtypes(include=['number'])
final_df = pd.concat([numerical_df.reset_index(drop=True), categorical_encoded_df], axis=1)

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(final_df)

# Apply PCA
pca = PCA(n_components=min(10, scaled_data.shape[1]))  # Ensure n_components does not exceed feature count
pca_result = pca.fit_transform(scaled_data)
pca_df = pd.DataFrame(pca_result, columns=[f'PC{i+1}' for i in range(pca_result.shape[1])])

# Explained variance
explained_variance = pca.explained_variance_ratio_
print("Explained Variance Ratio:", explained_variance)
# PCA Visualization
plt.figure(figsize=(8, 6))
sns.scatterplot(x=pca_df['PC1'], y=pca_df['PC2'])  # Assuming PC1 and PC2 are the most important
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Projection')
plt.show()

# Apply t-SNE
tsne = TSNE(n_components=2, perplexity=min(30, len(scaled_data) - 1), random_state=42)
tsne_result = tsne.fit_transform(scaled_data)
tsne_df = pd.DataFrame(tsne_result, columns=['t-SNE 1', 't-SNE 2'])

# t-SNE Visualization
plt.figure(figsize=(8, 6))
sns.scatterplot(x=tsne_df['t-SNE 1'], y=tsne_df['t-SNE 2'])
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.title('t-SNE Projection')
plt.show()

# Statistical Tests
# Example: t-test for two groups if applicable
group_col = 'Population'  # Change based on dataset
if group_col in df.columns and df[group_col].nunique() >= 2:
    groups = df[group_col].dropna().unique()
    group1 = final_df[df[group_col] == groups[0]]
    group2 = final_df[df[group_col] == groups[1]]
    t_stat, p_value = ttest_ind(group1.values, group2.values, nan_policy='omit', equal_var=False, axis=0) # Apply t-test to each column
    print("T-test results:", p_value)  # This will print p-values for each feature

# Example: ANOVA if multiple groups
if group_col in df.columns and df[group_col].nunique() > 2:
    group_values = [final_df[df[group_col] == g].values for g in df[group_col].dropna().unique()]  # Get values for each group
    anova_stat, anova_p = f_oneway(*group_values)
    print("ANOVA results:", anova_p)

# Example: Chi-square test for categorical association
if len(categorical_cols) > 1:
    chi2_stat, chi2_p, _, _ = chi2_contingency(pd.crosstab(df[categorical_cols[0]], df[categorical_cols[1]]))
    print("Chi-square test results:", chi2_p)