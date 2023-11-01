import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
uploaded = files.upload()

# Get the first uploaded file (assuming you're uploading a single file)
file_name = list(uploaded.keys())[0]

# Read the uploaded CSV file
df = pd.read_csv(file_name)
# Step 2: Data Exploration and Analysis
# Summary statistics
summary_stats = df.describe()

# Check for missing values
missing_values = df.isnull().sum()

# Visualizations
num_columns = len(df.columns) - 1  # Exclude the 'Potability' column
num_rows = (num_columns - 1) // 3 + 1

plt.figure(figsize=(15, 12))

# Histograms of water quality parameters
for i, column in enumerate(df.columns[:-1]):  # Exclude the 'Potability' column
    plt.subplot(num_rows, 3, i + 1)
    plt.hist(df[df['Potability'] == 0][column], bins=20, alpha=0.5, label='Non-Potable', color='red')
    plt.hist(df[df['Potability'] == 1][column], bins=20, alpha=0.5, label='Potable', color='blue')
    plt.title(column)
    plt.legend()

# Correlation matrix
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

plt.show()

# Step 3: Data Preprocessing
# Handling missing values
df.fillna(df.mean(), inplace=True)

# Step 4: Split the data into training and testing sets
X = df.drop('Potability', axis=1)
y = df['Potability']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Feature Scaling (using StandardScaler)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 6: Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: Evaluate the Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Step 8: Print a classification report
report = classification_report(y_test, y_pred)
print("Classification Report:")
print(report)

