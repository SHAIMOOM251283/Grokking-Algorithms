import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load historical stock price data
# Replace 'AAPL.csv' with the filename of your stock data file
data = pd.read_csv('aapl.csv')

# Create features
data['Price_Up'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)

# Select relevant features (you can include more features for a more complex model)
features = ['Open', 'High', 'Low', 'Volume']

# Split data into features and target variable
X = data[features]
y = data['Price_Up']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
