""" suggestion : offer to save or make as desktop background"""
from bs4 import BeautifulSoup
from datetime import datetime as dt
import requests
import urllib.request
import webbrowser

def do_wallpaper():
    res = requests.get( 'https://bingwallpaper.com/')
    soup = BeautifulSoup(res.text, 'lxml')

    image_box = soup.find('a', {'class': 'cursor_zoom'})
    image = image_box.find('img')

    link = image['src']

    filename = dt.now().strftime('%d-%m-%y')
    urllib.request.urlretrieve(link, filename)
    webbrowser.open(filename)