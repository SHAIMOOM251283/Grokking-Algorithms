import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate synthetic dataset
np.random.seed(42)
n_days = 1000
weather = np.random.randint(1, 6, n_days)
weekend_holiday = np.random.choice([0, 1], size=n_days)
game_day = np.random.choice([0, 1], size=n_days)
past_sales = np.random.randint(50, 200, n_days)

# Create DataFrame
data = pd.DataFrame({
    'Weather': weather,
    'Weekend_Holiday': weekend_holiday,
    'Game_Day': game_day,
    'Past_Sales': past_sales
})

# Splitting the dataset into features and target variable
X = data[['Weather', 'Weekend_Holiday', 'Game_Day']]
y = data['Past_Sales']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Example prediction for a new day
new_day_features = np.array([[4, 1, 0]])  # Weather = 4, Weekend or holiday = 1, Game on = 0
predicted_sales = model.predict(new_day_features)
print("Predicted sales for the new day:", predicted_sales[0])
