from pytube import YouTube
from pprint import pprint

def run(url):
    yt =YouTube(url)
    print(yt.title)
    a = input('Do you want to download the video ? (y/n) ')
    if a == 'Y' or a == 'y' :
        pprint(yt.streams.filter(progressive=True, file_extension='mp4').all())
        pprint('Enter "itag" to download video as per quality of video: ')
        itag = int(input())
        stream = yt.streams.get_by_itag(itag)
        print('wait..downloading...')
        stream.download()
        pprint('Video downloaded. ')
    else:
        pprint('Invalid input')
        quit()


def do_youtube():
    url = str(input('Paste url and press enter to proceed : \n'))
    run(url)