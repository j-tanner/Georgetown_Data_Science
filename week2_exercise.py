import pandas as pd

df = pd.read_csv('master_list_gtown', delimiter='\t')

df = df[['Title', 'Author', 'Recommender']]


def my_data_function(num_recommendations):
    book_recs = {}
    results = []
    for index, row in df.iterrows():
        title = row[0]
        author = row[1]
        book = f"{title} by {author}"
        if book not in book_recs.keys():
            book_recs[book] = 1
        else:
            book_recs[book] += 1
    for item in book_recs:
        if book_recs[item] == num_recommendations:
            results.append(item)
    return results

print(my_data_function(5))