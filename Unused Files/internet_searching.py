# UNUSED (but working) CODE FOR SEARCHING THE INTERNET #

# import requests
# import urllib
# #import pandas as pd
# #from requests_html import HTML
# from requests_html import HTMLSession


# def get_source(
#         url
# ):  # this function will return the source code when given a web URL #

#     try:  # the try statement runs code but if an error is returned, it runs the code in the 'except' statement #
#         session = HTMLSession()
#         response = session.get(url)
#         return response

#     except requests.exceptions.RequestException as error:
#         print(error)  # prints the error #


# def scrape_google(query):

#     query = urllib.parse.quote_plus(
#         query + 'recipe')  # converts the string query to the correct format #
#     response = get_source("https://www.google.co.uk/search?q=" +
#                           query)  # searches google for the query #

#     links = list(
#         response.html.absolute_links
#     )  # links all the possible links, including non google domains e.g. bbc.co.uk #
#     google_domains = ('https://www.google.', 'https://google.',
#                       'https://webcache.googleusercontent.',
#                       'http://webcache.googleusercontent.',
#                       'https://policies.google.', 'https://support.google.',
#                       'https://maps.google.')

#     # removes all the links hosted by google #
#     for url in links[:]:  # a colon means 'all of' #
#         if url.startswith(google_domains):
#             links.remove(url)


# #        if ('map') in url or ('support') in url or ('policies') in url:
# #          links.remove(url)

#     return links[:3]  # prints only the top 3 results #

# print("Ready...")
