import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# 1. Load data
# You can use the URL directly or download it as 'crop_data.csv'
url = "cpdata.csv"
df = pd.read_csv(url)

# 2. Features and Target
# Note: Ensure column names match your CSV (N, P, K, temperature, humidity, ph, rainfall)
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# 3. Split & Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 4. Save the model
with open('crop_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as crop_model.pkl!")