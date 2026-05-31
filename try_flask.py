import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  # or other scikit-learn models

# Generate some sample data
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [10, 20, 30, 40, 50]
}

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Split the data into training and test sets (assuming a simple model)
X_train, X_test, y_train, y_test = train_test_split(df[['Feature1', 'Feature2']], df['Target'], test_size=0.2, random_state=42)

# Train a Linear Regression model on the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Prepare a Pandas DataFrame for prediction (assuming the same features as X_test)
test_data = {
    'Feature1': [6, 7],
    'Feature2': [60, 70]
}

# Create a Pandas DataFrame from the test data
x_pred = pd.DataFrame(test_data)

# Make predictions using the trained model and the test data (Pandas DataFrame)
predictions = model.predict(x_pred)

# Print the predicted values
print(predictions)
