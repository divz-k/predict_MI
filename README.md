# Predict Acute Myocardial Infarction from Gene Expression Data

## Project Overview

1. What is a Gene expression profile, and why can it be used to predict diseases?
   
   Gene expression profile is a measure of how much a gene is active or inactive in the cell. This is determined by the levels of mRNA. mRNA is made by reading DNA, and in different cells and under different conditions, the same DNA is expressed in different amounts. The levels of mRNA affect the levels of the protein, and therefore the fate of the cell. Studying the mRNA levels: the gene expression, can provide deep insights into cell workings.

2. What does the data look like?

   Here we have a large matrix of 100 patient samples (both healthy and with MI), and the gene expression levels of aroung 55k genes in circulating endothelial cells (CEC). https://www.nature.com/articles/s41598-017-12166-0

3. Goal:

   We want to use this data to train an ML model, such that given the gene expression profile of another person, we can predict if they are healthy or at the risk of MI.
   
The workflow implements a full machine-learning pipeline:

- exploratory data analysis (EDA) on the features derived
- model training (Logistic Regression, Decision Tree)
- hyperparameter tuning
- evaluation and interpretation

  ## Key Steps:
- Exploratory Data Analysis (EDA): Correlation, select significant genes with WRS
- Model Training & Evaluation on significant genes and all genes
-- Logistic Regression (best performer)
-- Decision Tree
- Deployment: FastAPI application, containerized using Docker, deployed on Render.

## Installation

1) Clone Repository
```
git clone https://github.com/divz-k/predict_MI predict_MI
cd predict_MI
```

2) Create and activate Environment
```
python -m venv promoter_env
# Linux/Mac
source promoter_env/bin/activate
# Windows
promoter_env\Scripts\activate
#install dependencies
pip install -r requirements.txt
```

## Running the deployed API
1. Prepare the input as given in the template input_sample.xlsx. Since the best model only uses the genes classified as significant in the EDA, we will only need those for input. Gene names are mentioned in the input_sample.xlsx
2. Save the excel sheet in the predict_MI folder
3. Go to make_prediction.ipynb and run the 3rd block (for deployed API prediction)
4. There is a video Screen Recording describing this process: Screen_Recording_making_prediction.mov. Github doesn't allow you to play it, so you have to download and watch the video.

## Files in Repository
- EDA_modelTraining.ipynb – Feature extraction, model training, and evaluation
- best_logistic_regression_model.pkl
- Dockerfile – For building the container
- requirements.txt – Dependencies
- deploy_model.py – FastAPI application
- input_sample.xlsx
- significant_genes_used_in_model.csv - use to select the significant genes



