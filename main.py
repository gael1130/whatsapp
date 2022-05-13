import pandas as pd

# TODO #1: Read the text extract from whatsapp
df = pd.read_csv('data/hold_up.txt', delimiter="\t", header=None)
# print(df)

# TODO #2: Name the first and only column before splitting it
df.columns = ["text"]

# TODO #3: Split the columns into date, hour, author and message
df[['date', 'hour']] = df['text'].str.split('à', 1, expand=True)
df[['hour', 'author']] = df['hour'].str.split('-', 1, expand=True)
df[['author', 'message']] = df['author'].str.split(':', 1, expand=True)

# TODO #4: Create a new df with only the columns I need
new_df = df[['date', 'hour', 'author', 'message']]
# print(new_df.columns)

# TODO #5: Check the most frequent posters
post_ranking = new_df["author"].value_counts()
print(post_ranking)

