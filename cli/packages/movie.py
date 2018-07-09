import pprint
import requests

def query_inp():
    queryList = input("Enter the movie name you want to see the reviews of: ").split(' ')
    if len(queryList) > 1:
        query = queryList[0].lower()
        for i in queryList[1: ] :
            query = query + '+' + i.lower()
    else:
        query = queryList[0].lower()


def print_data(result):
    for i,item in enumerate(result,1):
        print("{}.    {}      language:{}".format(i, result[i-1]['original_title'], result[i-1]['original_language']))
    print("\n Select the option you meant to search: ")
    choice = int(input())
    opted= result[choice-1]
    print("\n               TITLE:    " + opted['original_title'])
    print("\n  Description: " + opted['overview'].strip())
    print("\n Popularity: " + str(opted['popularity']) , end=' ')
    print( "\t\t Date of Release: " + opted['release_date'])
    print(" Votes: "+ str(opted['vote_average']))

def do_movie():
    query_inp()
    url = "https://api.themoviedb.org/3/search/movie?api_key=d47be8cb9ad8930093820c17b091a396&query=" + query
    res= requests.get(url)
    data = res.json()
    result = data['results']
    print_data(result)
