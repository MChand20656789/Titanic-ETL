import pandas as pd
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt
import seaborn as sns

# === Extract ===
df = pd.read_csv('data/train.csv')

# === Transform ===
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = df.drop(['Cabin', 'Ticket', 'Name'], axis=1)

# Save cleaned data
df.to_csv('titanic_cleaned.csv', index=False)

# === Load into SQLite ===
engine = create_engine('sqlite:///titanic.db')
df.to_sql('passengers', engine, index=False, if_exists='replace')

# === Query 1: Survival rate by class ===
query1 = """
SELECT Pclass, AVG(Age) AS avg_age, AVG(Survived) AS survival_rate
FROM passengers
GROUP BY Pclass;
"""
with engine.connect() as conn:
    results1 = conn.execute(text(query1))
    print("\n=== Survival Rate by Class ===")
    for row in results1:
        print(row)

# === Query 2: First 10 passengers ===
query2 = "SELECT * FROM passengers LIMIT 10;"
df_preview = pd.read_sql(query2, engine)
print("\n=== First 10 Passengers ===")
print(df_preview)

# === Query 3: Survival rate by sex ===
query3 = "SELECT Sex, AVG(Survived) AS survival_rate FROM passengers GROUP BY Sex;"
df_sex = pd.read_sql(query3, engine)
print("\n=== Survival Rate by Sex ===")
print(df_sex)

# === Plot 1: Survival rate by class ===
df_class = pd.read_sql(query1, engine)
sns.barplot(x='Pclass', y='survival_rate', data=df_class)
plt.title('Survival Rate by Class')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.show()

# === Plot 2: Survival rate by sex ===
sns.barplot(x='Sex', y='survival_rate', data=df_sex)
plt.title('Survival Rate by Sex (0=Male, 1=Female)')
plt.ylabel('Survival Rate')
plt.xlabel('Sex')
plt.show()

# === Plot 3: Age distribution by survival ===
sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', bins=30)
plt.title('Age Distribution by Survival')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# === Plot 4: Fare distribution by class ===
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title('Fare Distribution by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()
