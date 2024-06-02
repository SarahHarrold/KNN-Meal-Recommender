from recommender import algo
import pandas as pd
from surprise import Dataset
from surprise import Reader
import requests
import urllib
from requests_html import HTMLSession

user = 1001 # this is the user number of the user of this program, once their ratings are added to the dataframe, I have chosen this arbitrary ID for them because it leaves space for more data to train the model
MEALS=18
userRatings = []
itemNum = 0
numberToRate = 3
listOfMeals = ['Spaghetti Bolognese','Chili con Carne','Margarita Pizza','Toad in the Hole','Caesar Salad','Pesto','Cheese Burger','Steak and Chips','Macaroni Cheese','Fish and Chips','BBQ Ribs','Chicken Tikka Masala','Miso Ramen','Ratatouille','Spaghetti Carbonara','Bangers and Mash','Chicken Wings','Hot Dog','Green Leaf Salad']

# ------------------------ #
# introducing the program #
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print("Welcome. To recommend you a meal, your opinion is needed on",numberToRate,"other meals.")
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
# ------------------------ #
# Runs through the list of meals asking the user for their rating out of 5 #
for mealname in listOfMeals[:numberToRate]: # the number of meals to be rated can be changed #
  notNum = True
  while notNum == True:
    print("Please rate",mealname,"out of 5")
    rating = (input("> "))
    if rating not in ['1','2','3','4','5']:
      notNum = True
      if rating.lower() in ['one','two','three','four','five']:
        print("Please use digits 1-5, rather than letters.")
      else:
        print("Sorry, only numbers 1-5 are valid.")
    else:
      notNum = False
      userRatings.append(int(rating))
#      print(mealname,rating)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('') # a dividing and new line #

# ------------------------ #

df2 = pd.read_csv("meal_ratings.csv") # opens the CSV file of meal ratings #

# appends all of the ratings into the dataframe as new rows #
for rating in userRatings:
  itemNum += 1
#  print('rating added to df2: ',rating)
  df2.loc[len(df2.index)] = [user, itemNum, rating,'']

reader = Reader(rating_scale=(1,5))

ratingsdata = Dataset.load_from_df(df2[["user_ID", "meal", "rating"]], reader)

#print('this data is going to be trained from')
#print(df2)

trainingSet = ratingsdata.build_full_trainset()

algo.fit(trainingSet)

print('Model trained.')
print('')

# ------------------------ #

best_meal = None
best_meal_est = 0
for meal in range(numberToRate, MEALS - 1): # starting at meals to rate avoids recommending meals that were previously rated by the user #
#  print(user,meal,rating)
  prediction = algo.predict(user, meal)
#  print(prediction)
#  print(meal, prediction.est)
  if prediction.est > best_meal_est:
    best_meal = meal
    best_meal_est = prediction.est

print("Best meal prediction is", listOfMeals[best_meal], "with a predicted rating of", best_meal_est)

print('') # new line #
print('Searching for recipes...')
print('') # new line #

# ------------------------ #
# searching the internet for the recommended meal #

def get_source(url): # this function will return the source code when given a web URL #

    try: # the try statement runs code but if an error is returned, it runs the code in the 'except' statement #
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as error:
        print(error) # prints the error #

def scrape_google(query):

    query = urllib.parse.quote_plus(query+'recipe') # converts the string query to the correct format #
    response = get_source("https://www.google.co.uk/search?q=" + query) # searches google for the query #

    links = list(response.html.absolute_links) # links all the possible links, including non google domains e.g. bbc.co.uk #
    google_domains = ('https://www.google.', 
                      'https://google.',                       'https://webcache.googleusercontent.',              'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

# removes all the links hosted by google #
    for url in links[:]: # a colon means 'all of' #
        if url.startswith(google_domains):
          links.remove(url)    
    return links[:6] # returns only the top 6 results #

recipelinks = scrape_google(listOfMeals[best_meal])

print("Here are 3 links leading to recipes for your recommended meal!")
print("If you have food allergies, please check ingredients before using these recipes. These links have not been checked for quality.")
print('') # new line #

index= 0
recipelinks = list(set(recipelinks)) # removes duplicates from the list by converting it to a set, then back to a list #

for link in recipelinks: # removes links with time stamps #
  if 't=' in link:
    recipelinks.remove(link)
  
for link in recipelinks[:3]: # for each link in the top 3 recipe links #
  index += 1
  print("Link",index,': ',link)
  print('')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print("Thank you for using this program, your data will now be removed from any data structures used...")
userRatings = []
for variable in dir(): # clears all variables in my code #
  if not variable.startswith("__"):
    del globals()[variable]
print("Variables cleared")