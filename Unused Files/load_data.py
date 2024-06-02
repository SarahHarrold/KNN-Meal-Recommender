# UNUSED OUT OF DATE CODE FOR LOADING USER DATA INTO A DATAFRAME #

# with one new user "E" who has rated only movie 1
# ratings_dict = {
#     "meal": ['1', '2', '1', '3', '2', '3', '1', '3', '1'],
#     "user_ID": ['Sarah', 'Sarah', 'Vera', 'Vera', 'Alice', 'Alice', 'Lizzie', 'Lizzie', 'Eloise'],
#     "rating": [1, 2, 2, 4, 2.5, 4, 4.5, 5, 3],
# }

#df = pd.DataFrame(ratings_dict)
#reader = Reader(rating_scale=(1, 5))

# Loads Pandas dataframe (the first problem)
#data = Dataset.load_from_df(df[["user_ID", "meal", "rating"]], reader)

# Loads my data (the second problem)
#reader = Reader(line_format='user meal rating', sep=",", rating_scale=(1,5))
#data = Dataset.load_from_file('mealDataCSV.csv',reader)

#df2.loc[len(df2.index)] = [100, 2, 3,''] # adds user 100 with a 3 rating of foot item 2 #

#df2.loc[len(df2.index)] = [105,3,4] # adds a 105th user who likes the third meal with a rating of 4 #
