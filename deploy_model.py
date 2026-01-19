from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
from typing import List
import joblib

model = joblib.load("best_logistic_regression_model.pkl")
app = FastAPI(title="My Model API")


@app.post("/predict_excel")
async def predict_excel(file: UploadFile = File(...)):
    if model is None:
        return {"error": "Model not loaded"}

    try:
        df = pd.read_excel(file.file)

        # Select only numeric sample columns
        sample_cols = [c for c in df.columns if c != 'gene_names']
        X = df[sample_cols].T.values  # rows = samples, columns = features

        # Check number of features
        if X.shape[1] != 120:
            return {"error": f"Expected 120 features, got {X.shape[1]}"}

        y_pred = model.predict(X)
        return {"prediction": y_pred.tolist()}

    except Exception as e:
        return {"error": str(e)}
