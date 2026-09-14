import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
posts_df = pd.read_csv('Cleaned_Posts.csv')
posts_df['timestamp'] = pd.to_datetime(posts_df['timestamp'])
sns.set_theme(style="whitegrid")
#chart 1
plt.figure(figsize=(10, 5))
sns.countplot(data=posts_df, x='platform', order=posts_df['platform'].value_counts().index, palette='viridis', hue='platform', legend=False)
plt.title('Total Posts per Platform', fontsize=14, fontweight='bold')
plt.xlabel('Platform')
plt.ylabel('Number of Posts')
plt.show()
#chart 2
plt.figure(figsize=(10, 5))
known_platforms = posts_df[posts_df['platform'] != 'Unknown']
sns.barplot(data=known_platforms, x='platform', y='likes', estimator=lambda x: sum(x)/len(x), palette='magma', hue='platform', legend=False)
plt.title('Average Likes per Post by Platform', fontsize=14, fontweight='bold')
plt.xlabel('Platform')
plt.ylabel('Average Likes')
plt.show()
posts_df['year_month'] = posts_df['timestamp'].dt.to_period('M')
monthly_posts = posts_df.groupby('year_month').size().reset_index(name='post_count')
monthly_posts['year_month'] = monthly_posts['year_month'].astype(str)
plt.figure(figsize=(12, 5))
sns.lineplot(data=monthly_posts, x='year_month', y='post_count', marker='o', color='b', linewidth=2)
plt.title('Posting Activity Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Posts')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()