""" SUGGESTION : add a search from wikipedia in option 3 ; the user can just ask for a summary from the wikipedia feature! """
import wikiquote, random

def do_quote():
    while True:
        quote_list = []
        print("\n\nHello wise internet user, so you want to brew some good quotes!"
                "Choose the options we can serve u now:\n"
                "1.  Quote of the Day\n"
                "2.  Search the keyword you wish to see quotes on ( a movie, an author, anything)\n"
                "3.  Show some random titles to search quotes on\n"
                "4.  Just show some random quotes ( in case u r in a hurry)\n")

        choice = int(input("Enter your Choice: "))
        print()
        if choice ==1:
            qOtD = []
            qOtD  = list(wikiquote.quote_of_the_day())
            print("\n{} \n \t\t\t --{}".format(qOtD[0],qOtD[1] ))
            break

        elif choice == 2:
            search_result=[]
            srch_txt = input("Enter the keyword you wish to search: ")
            search_result = list(wikiquote.search(srch_txt) )
            if search_result:
                print("\nEnter the item number you wish to see a quote on: \n")
                for x,item in enumerate(search_result,1):
                    print("{}.    {}".format(x, item))
                srch_choice = int(input())
                srch_strng = search_result[srch_choice - 1]
                quote_list = list(wikiquote.quotes(srch_strng, max_quotes = 5))
                print()
                for i,item in enumerate(quote_list,1):
                    print("{}.   {}\n".format(i, item)) 
                break

            else:
                print("no quotes on that! try again.....")
            
        elif choice==3: 
            rand_ttls= list(wikiquote.random_titles(max_titles = 5))
            print("\nEnter the item number you wish to see a quote on: \n")
            for i,item in enumerate(rand_ttls,1):
                print( "{}.  {}".format(i, item))
            srch_choice = int(input())
            srch_strng = rand_ttls[srch_choice - 1]
            quote_list = list(wikiquote.quotes(srch_strng, max_quotes = 5))
            for m,item in enumerate(quote_list,1):
                print( "{}.  {}\n".format(m, item))
            break

        elif choice==4:
            rand_ttls= list(wikiquote.random_titles(max_titles = 5))
            rnd_str = random.choice(rand_ttls)
            try:
                print(random.choice(wikiquote.quotes(rnd_str)))
                break
            except UnboundLocalError:
                print( "[!] Sorry, some technical glitch occured, please try again!")
    