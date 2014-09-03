import requests
from httplib import *
from urlparse import urlparse
import optparse



class RestClient:

    def doGet(self, connURL, f):
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
        files = {"file": open(requestFile, 'rb+')}
        r = requests.post(connURL, files=files)
        respFile.write(r.content)
        respFile.seek(0)
        return respFile

    def doPost(self, connURL, params, respFile):
        r = requests.post(connURL, data=params)
        respFile.write(r.content)
        respFile.seek(0)
        return respFile

    def addParameterstoURL(self, mediaURL, outputFormat, outputSize, crop):
        if(mediaURL == ""):
                return "?format=" + outputFormat + "&size=" + outputSize + "&crop=" + crop;
        else:
            return "?url=" + mediaURL + "&format=" + outputFormat + "&size=" + outputSize + "&crop=" + crop

