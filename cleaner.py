import pandas as pd
posts_df = pd.read_csv('Social_Engine_Posts_Corrupted.csv')
users_df = pd.read_csv('Social_Engine_Users.csv')
posts_df['platform'] = posts_df['platform'].fillna('Unknown')
posts_df['text_content'] = posts_df['text_content'].fillna('[BLANK]')
posts_df['likes'] = posts_df['likes'].fillna(0)#fix data type
posts_df['timestamp'] = pd.to_datetime(posts_df['timestamp'], errors='coerce')
initial_rows = len(posts_df)
posts_df = posts_df.drop_duplicates()
print(f"Dropped {initial_rows - len(posts_df)} duplicate rows.")
valid_rows = len(posts_df)
posts_df = posts_df[(posts_df['likes'] >= 0) & (posts_df['shares'] >= 0) & (posts_df['comments'] >= 0)]
print(f"Dropped {valid_rows - len(posts_df)} corrupted rows with negative engagement.")
posts_df.to_csv('Cleaned_Posts.csv', index=False)
print("\nSuccess! Cleaned_Posts.csv has been generated.")