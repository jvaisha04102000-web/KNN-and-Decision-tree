import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = {
    "income": [30000, 60000, 25000, 80000, 50000],
    "credit_score": [650, 720, 600, 750, 690],
    "loan_amount": [20000, 25000, 15000, 30000, 22000],
    "risk" : ["High", "Low", "High", "Low", "Medium"]
}

df = pd.DataFrame(data)

X = df[["income", "credit_score", "loan_amount"]]
y = df["risk"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print(model.predict([[55000, 710, 24000]]))