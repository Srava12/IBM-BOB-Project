import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset inside code - no external file needed
data = {
    'Name': ['GTA 5', 'PUBG', 'Free Fire', 'Minecraft', 'Valorant'],
    'Rating': [9.5, 9.0, 8.5, 9.2, 8.8],
    'Genre': ['Action', 'Battle Royale', 'Battle Royale', 'Sandbox', 'FPS']
}
df = pd.DataFrame(data)

print("\n--- Dataset Info ---")
print(df)
print("\n--- Null Values ---")
print(df.isnull().sum())

# 1. Bar Chart
plt.figure(figsize=(10, 5))
sns.barplot(x='Name', y='Rating', data=df)
plt.title('Game Ratings - IBM Project')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('game_ratings.png')
plt.show()

# 2. Genre Analysis
plt.figure(figsize=(8, 4))
sns.countplot(x='Genre', data=df)
plt.title('Genre wise Game Count')
plt.tight_layout()
plt.savefig('genre_count.png')
plt.show()

print("\nSuccess! Graphs saved!")
