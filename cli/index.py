""" SUGGESTION:
#  arrange the 'help' menu
#  make the output dynamic to the size of window opened
 """

from packages import (
    do_crypto, do_movie, do_stocks, do_youtube, do_facebook,
    do_news, do_wallpaper, do_hackathon, do_quote, do_wiki
)

import cmd
import os
import sys
from colored import fg, bg, attr

class cmdApp(cmd.Cmd):
    if len(sys.argv) > 1 :
        intro = "Welcome {usr}....".format(usr = ' '.join(sys.argv[1: ]))
    else :
        print("%s%s //please enter your username after ur command// %s"%(fg(1),attr(1),attr(0)))
        sys.exit()
            
    greet = """
                    __________________________________________________________________
                    
                    \t\t\t Welcome to Cli Application
                     __________________________________________________________________
                    
                    \t *.crypto : for top 10 Crypto Currency prices
                    \t *.movie  : for Movie details and ratings
                    \t *.stocks : to get Open, High Low Close and volume details of entered stock
                    \t *.youtube: to download any youtube video using its link
                    \t *.facebook : login facebook 
                    \t *.news : for News 
                    \t *.wallpaper : to display wallpaper
                    \t *.hackathon : to see upcoming hackathons
                    \t *.quote : for quote of the day
                    \t *.wiki : to wikipedia search
                    \t *.exit
                    for help type help 
                    """
    print(('%s'+greet+'%s')%(fg(220),attr(0)))

    prompt = '%s%s$~%s'%(fg(46),attr(1),attr(0))
    
    def help_crypto(self):
        print("To show the list of top 10 cryptocurrencies as per Market Cap")
    def help_movie(self):
        print("See the short summary, review and other basic info about ur favoirite movies")
    def help_stocks(self):
        print("Just feed the ticker and get the ongoing value of it as per the entered stock countrys' currency value")
    def help_youtube(self):
        print("Download your favourite youtube video just with the link. No questions asked  (- _ <)")
    def help_facebook(self):
        print("Feed in your facebook credentials in the terminal and see the browser login itself")    
    def help_news(self):
        print("Browse through the latest news with a choice for the country and various news sources")
    def help_wallpaper(self):
        print("See the wallpaper of the day and get it downloaded if you like it")
    def help_hackathon(self):
        print("Extract the list of all hackathons from the website hackerearth.com")
    def help_quote(self):
        print("Need some motivation? Get some amazing quotes: randomly or as per ur tastes just easily")
    def help_wiki(self):
        print("Search  keywords or get random topics in wikipedia today.")
    
    def do_crypto(self,arg):
        "crypto currency price"
        do_crypto()
    
    def do_movie(self,arg):
        "get movies ratings n info"
        do_movie()
    
    def do_stocks(self,arg):
        "get latest market position of any stock or index"
        do_stocks()

    def do_youtube(self,arg):
        "youtube video"
        do_youtube()
    
    def do_facebook(self,arg):
        "login into facebook using terminal"
        do_facebook()

    def do_news(self, arg):
        "Read today's news"
        do_news()

    def do_wallpaper(self, arg):
        "Download and see wallpaper of the day"
        do_wallpaper()

    def do_hackathon(self,arg):
        "See all the upcoming hackathons in India"
        do_hackathon()

    def do_quote(self, arg):
        "Read quote of the day"
        do_quote()
    
    def do_wiki(self,arg):
        "Search anything and read summary from wikipedia"
        do_wiki()
    
    def do_history(self,arg):
        "when not working"
        print(self._history)
    
    def do_help(self,arg):
             print("crypto    movie     stocks    youtube    facebook     news   "
                      "wallpaper     hackathon    quotes      wiki   history    clear    exit")

    def do_clear(self,arg):
        "To clear the current screen"
        os.system('cls' if os.name=='nt' else 'clear')
    

    def do_exit(self, arg):
        "Exit the application"
        return -1

    def emptyline(self):
        pass

    def precmd(self,line):
        # none
        if line != ' ':
            self._history += [line.strip()]
        return line

    def postcmd(self,stop,line):
        return stop

    def preloop(self):
        cmd.Cmd.preloop(self)
        self._history = []
    
    def postloop(self):
        print( "GoodBye . .  .")
        cmd.Cmd.postloop(self)
    
if __name__ == '__main__':
    cmdApp().cmdloop("%s%sStarting shell...%s\n\n"%(fg(80),attr(5),attr(0)))