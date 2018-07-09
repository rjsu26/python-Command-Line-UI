# SUGGESTIONS: 
#  1 . If desired query is not shown in the list, give option to see for more 
#   list items, or , let user refine his query

import wikipedia

def do_wiki():
    print("Enter the search query for wikipedia: ")
    query = input()
    options = wikipedia.search(query)
    # print(options)
    print("Here are the search results, choose one of them to get a summary: ")
    for i,item in enumerate(options,1):
        print("{}.  {}".format(i, item))
    choice = int(input())
    keyword = options[choice-1]
    print(wikipedia.summary(keyword, sentences = 5))
