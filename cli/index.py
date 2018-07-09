from package import (
    do_crypto, do_movie, do_stocks, do_youtube, do_facebook,
    do_news, do_wallpaper, do_hackathon, do_quote, do_wiki
)

import cmd
import sys

class cmdApp(cmd.Cmd):
    intro = "Welcome {usr}....".format(usr = sys.argv[1])
    greet = """
                    --------------------------------------------------------------------------------------------------
                    \t\t\t\t Welcome to Cli Application
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
                    \t\t\t\t\t\t\t\t\t for help type help 
                    """
    print(greet)

    prompt = '$ ~ '
    
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

    def do_exit(self, arg):
        "Exit the application"
        return -1

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
        print( "Quitting . .  .")
        cmd.Cmd.postloop(self)
    
if __name__ == '__main__':
    cmdApp().cmdloop()