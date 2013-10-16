__author__ = 'tippytip'


def stripUrl(urlString):
        urlArray = urlString.split("/")
        return urlArray[len(urlArray)-1]