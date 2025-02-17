# genomic_data_analysis |
Genome Data Analysis Project

Overview

This project performs exploratory data analysis and statistical computations on a genomic dataset. It includes data preprocessing, dimensionality reduction (PCA, t-SNE), and statistical tests (t-test, ANOVA, Chi-square test) to analyze genetic data.

Requirements

Ensure you have the following Python libraries installed:

pip install scikit-learn pandas numpy matplotlib seaborn scipy

Dataset:

The project processes a genomic dataset stored in igsr_HG01350_undefined.csv. The dataset is expected to contain both numerical and categorical data.

Features:

Data Loading & Preprocessing

Reads the dataset using pandas

Handles missing values (options to fill with mean or drop rows)

Encodes categorical data using OneHotEncoder

Dimensionality Reduction

Standardizes numerical features using StandardScaler

Applies Principal Component Analysis (PCA) for feature reduction and visualization

Uses t-SNE for non-linear dimensionality reduction

Statistical Analysis

t-Test: Compares two groups if applicable

ANOVA: Tests for differences across multiple groups

Chi-square Test: Analyzes categorical feature associations

Visualization:

The project generates scatter plots for PCA and t-SNE projections to visualize data structure.

How to Run:

Ensure the dataset (igsr_HG01350_undefined.csv) is in the working directory.

Run the Python script:

python genome.py

View the output, including statistical test results and generated plots.

Future Improvements:

Implement more robust missing value handling strategies.

Optimize PCA and t-SNE parameters for better clustering.

Explore machine learning models for classification or clustering of genomic data.
