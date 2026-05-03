import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("Dataset.csv")

# Encode target
le = LabelEncoder()
df["Class"] = le.fit_transform(df["Class"])

# Features & target
X = df[["Amount", "Frequency", "LocationScore"]]
y = df["Class"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# New behavior prediction
new_user = [[600, 3, 7]]
print("Prediction:", model.predict(new_user))