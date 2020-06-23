import requests


class RequestDownloader:
    def __init__(self, url):
        self.__url = url

        self.__page = None

    @property
    def content(self):
        if self.__page is None:
            self.__page = requests.get(self.__url)

        return self.__page.content
