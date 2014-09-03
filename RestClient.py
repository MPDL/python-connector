import requests
from httplib import *
from urlparse import urlparse



class RestClient:

    def doGet(self, connURL, f):
        print connURL
        parseres = urlparse(connURL)
        connection = HTTPConnection(parseres.netloc)
        connection.request('GET', parseres.path + "?" + parseres.query)
        response = connection.getresponse()
        html = response.read()
        f.write(html)
        f.seek(0)
        connection.close()
        return f

    def doPost2(self, connURL, requestFile, respFile):
        print connURL
        files = {"file": open(requestFile, 'rb+')}
        r = requests.post(connURL, files=files)
        respFile.write(r.content)
        respFile.seek(0)
        return respFile

    def doPost(self, connURL, params, respFile):
        print connURL
        print params
        r = requests.post(connURL, data=params)
        print r.content
        respFile.write(r.content)
        respFile.seek(0)
        return respFile

    def addParameterstoURL(self, mediaURL, outputFormat, outputSize, crop):
        if(mediaURL == ""):
                return "?format=" + outputFormat + "&size=" + outputSize + "&crop=" + crop;
        else:
            return "?url=" + mediaURL + "&format=" + outputFormat + "&size=" + outputSize + "&crop=" + crop

    def parseurl(self, url):
        parseresult = urlparse(url)
        print parseresult.netloc
        print parseresult.path
        print parseresult.params
        print parseresult.query
        print parseresult.fragment

if __name__ == '__main__':

    test = RestClient()
    test.parseurl("http://vm15.mpdl.mpg.de/screenshot/take?url=http%3A%2F%2Fmpdl.mpg.de&browserWidth=&browserHeight=&format=png&size=&crop=")