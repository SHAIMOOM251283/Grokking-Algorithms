import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generating synthetic dataset
np.random.seed(42)
n_samples = 1000
price = np.random.normal(50, 10, n_samples)  # Normally distributed prices
advertising = np.random.normal(100, 20, n_samples)  # Normally distributed advertising expenditure
sales = 50 + 2 * price - 3 * advertising + np.random.normal(0, 10, n_samples)  # Linear relationship with noise

# Creating a DataFrame
data = pd.DataFrame({'Price': price, 'Advertising': advertising, 'Sales': sales})

# Splitting the dataset into training and testing sets
X = data[['Price', 'Advertising']]
y = data['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Visualize the actual vs. predicted sales
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs. Predicted Sales")
plt.show()
