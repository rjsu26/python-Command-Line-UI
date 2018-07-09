# suggestion - make colorful tables to show the list of countries and sources
from bs4 import BeautifulSoup
import requests
import datetime

# To use the date for obtaining the date 4 months ago in custom news search
def get_dateTime():
    today = datetime.date.today()
    day = today.day
    month = today.month
    year = today.year
    if month>4:
        setDay = day
        setMonth = month - 4
        setYear = year 
    elif month ==4:
        setDay = '01'
        setMonth =' 01'
        setYear = year 
    else:
        setDay = day
        setMonth = 12 -(4 - month)
        setYear = year - 1 

    req_date = str(setYear)+ '-' + str(setMonth) + '-' + str(setDay)
    return req_date


# extracting the source list and country list from the website
def mk_lst():
    res = requests.get ('https://newsapi.org/sources')
    soup = BeautifulSoup(res.text , 'lxml')
    sourceL = {}
    countryL = {}
    source_list = soup.find_all ('div', {'class' : 'source publisher fl-ns w-25-l w-50-m mb2'})
    country_list = soup.find_all('div', {'class' : 'source fl-l w-50-l mb2'})
    for source in source_list:
        name = source['data-name']
        code_name = source.find('kbd').text
        sourceL[name]=code_name
    for country in country_list:
        Cname = country.find('div',{'class' : 'name f3'}).text.strip( )
        country_code = country.find('kbd').text.strip( )
        countryL[Cname]= country_code
    
    return sourceL,countryL

# defining the show_news function

def show_news(url):
    try:
        response = requests.get(url)
        rawData = response.json()
        source = rawData['articles']
        total = rawData['totalResults']
    except : 
        print("[!].......Something went wrong. Try again! ")

    for i in range(10):
        title = source[i]['title']
        description = source[i]['description']
        further_read = source[i]['url']
        publish_at = source[i]['publishedAt']

        print( "{}.     Title: {}  \n\n  {}  \n\n For Further Reading goto: {} \n\n  Article published at : {} ". format(i+1, title, description , further_read, publish_at))
        print("\n\n")

# The USER INTERFACE
def do_news():
    req_date = get_dateTime()
    
    print("Hello mate! Here are the options to choose the news u would like to read:\n\n")
    print("1.  Top Headlines of your country\n" 
            "2 . Search a keyword \n\n")
    choice = int(input())

    sourceL, countryL =  mk_lst()

    if choice==1:
        print("\n1. Enter your country to filter ur news accordingly\n"
                "2. Select a source to get news from by choosing from a list\n")
        choice1 = int(input())
        if choice1 == 1:
            print("\nEnter your country name ( First letter capital): \n")
            countryName = input()
            try:
                countryC = countryL[countryName]
                url =  ('https://newsapi.org/v2/top-headlines?'
                'country=' + countryC + '&language=en&'
                'apiKey=4a01ed9740da4690a8aae7e3321c407f')
                show_news(url)
            except KeyError:
                print("Wrong input! Try again as directed...\n")
        
        elif choice1 == 2:
            for i,source in enumerate(sourceL,1):
                print( " {}.   {}".format(i,source) )
            choice_source = input("\nEnter your desired source name ( case sensitive):  ")
            try:
                sourceC = sourceL[choice_source] 
                url = ('https://newsapi.org/v2/top-headlines?'
                    'sources=' + sourceC + '&language=en&'
                    'apiKey=4a01ed9740da4690a8aae7e3321c407f')
                show_news(url)
            except KeyError:
                print("sorry, wrong choice...\n")
        
        else:
            print(" Sorry ! Wrong Choice!")

    elif choice==2:
        search_keyword = input( "\nEnter your search keyword (separated-by-a-minus-sign-as-shown) : ")
        url = ('https://newsapi.org/v2/everything?'
        'q=' +search_keyword + '&'
        'from=' + req_date + '&'
        'sortBy=popularity&language=en&'
        'apiKey=4a01ed9740da4690a8aae7e3321c407f')
        show_news(url)

    else: 
        print("Sorry ! Wrong choice")


