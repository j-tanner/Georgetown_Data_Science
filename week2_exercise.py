import pandas as pd

df = pd.read_csv('master_list_gtown', delimiter='\t')

df = df[['Title', 'Author', 'Recommender']]


def my_data_function(num_recommendations):
    book_recs = {}
    results = []
    for index, i in df.iterrows():
        title = i[0]
        author = i[1]
        book = f"{title} by {author}"
        if book not in book_recs.keys():
            count = 1
            book_recs[book] = count
        else:
            count = book_recs[book]
            book_recs[book] = count + 1
    for item in book_recs:
        if book_recs[item] == num_recommendations:
            results.append(item)
    return results

print(my_data_function(3))