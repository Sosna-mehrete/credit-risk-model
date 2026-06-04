# credit-risk-model
# Credit Risk Model for Alternative Data

## Credit Scoring Business Understanding

### 1. How does the Basel II Accord's emphasis on risk measurement influence the need for an interpretable and well-documented model?

Basel II requires financial institutions to measure, monitor, and manage credit risk using transparent and well-documented methodologies. Therefore, credit scoring models should be interpretable, explainable, reproducible, and auditable. Regulatory authorities and business stakeholders must be able to understand how predictions are generated and how risk decisions are made. Models such as Logistic Regression combined with Weight of Evidence (WoE) transformations are often preferred because they provide clear explanations for their predictions and support regulatory compliance.

### 2. Without a direct "default" label, why is a proxy variable necessary, and what business risks does proxy-based prediction introduce?

The dataset used in this project does not contain a direct default indicator. Since supervised machine learning requires a target variable, a proxy target must be created. This project uses customer behavioral patterns derived from Recency, Frequency, and Monetary (RFM) analysis to identify customers who may resemble high-risk borrowers.

However, proxy-based prediction introduces several risks:

* Incorrect labeling of customers
* Misclassification of good customers as high-risk
* Potential model bias
* Reduced predictive reliability compared to using actual default data

These limitations should be clearly documented and considered when interpreting model outputs.

### 3. What are the key trade-offs between a simple, interpretable model and a high-performance model in a regulated financial context?

| Logistic Regression (with WoE) | Gradient Boosting                  |
| ------------------------------ | ---------------------------------- |
| Highly explainable             | More difficult to explain          |
| Basel II friendly              | Less transparent                   |
| Easier to audit and validate   | Harder to audit                    |
| Lower predictive performance   | Higher predictive performance      |
| Easier stakeholder acceptance  | Better accuracy and risk detection |

In regulated financial environments, organizations often balance model interpretability with predictive performance. While Gradient Boosting models may achieve better accuracy, Logistic Regression models are often preferred when transparency and regulatory compliance are critical.
