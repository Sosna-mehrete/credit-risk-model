import pandas as pd
import mlflow
import mlflow.sklearn
import joblib

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#prev#
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
#prev#
df = pd.read_csv("data/raw/data.csv")
df["TransactionStartTime"] = pd.to_datetime(df["TransactionStartTime"])
customer_features = df.groupby("CustomerId").agg({
    "Amount": ["sum", "mean", "std"],
    "TransactionId": "count"
})

customer_features.columns = [
    "total_amount",
    "avg_amount",
    "std_amount",
    "transaction_count"
]
snapshot_date = df["TransactionStartTime"].max() + pd.Timedelta(days=1)

rfm = df.groupby("CustomerId").agg({
    "TransactionStartTime": lambda x: (snapshot_date - x.max()).days,
    "TransactionId": "count",
    "Amount": "sum"
})
scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(rfm)
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

rfm["cluster"] = kmeans.fit_predict(rfm_scaled)
high_risk_cluster = 0

rfm["is_high_risk"] = (
    rfm["cluster"] == high_risk_cluster
).astype(int)
# STEP 11: Define features and target
X = customer_features
y = rfm["is_high_risk"]

# STEP 12: Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# STEP 13: Train model
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# STEP 14: Save model
joblib.dump(rf, "model.pkl")

print("Model training complete and saved as model.pkl")