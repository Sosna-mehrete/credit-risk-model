
import os
import pandas as pd


def run_pipeline():
    # create or load your dataframe
    df = pd.DataFrame({
        "customer_id": [1, 2, 3],
        "recency": [10, 20, 30],
        "frequency": [1, 2, 3],
        "monetary": [100, 200, 300]
    })

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv("data/processed/processed.csv", index=False)

    return df
