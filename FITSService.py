from RestClient import RestClient
import tempfile
import webbrowser
import urllib
import requests
import re
import urllib2
import optparse

class FITSService(RestClient):

    serviceTargetURL = "http://servicehub.mpdl.mpg.de/fits/api/view"

    def generateFromFile(self, serviceTargetURL, f):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        respFile = tempfile.TemporaryFile('rb+')
        self.doPost2(serviceTargetURL, f, respFile)
        return respFile


    def generateFromURL(self, serviceTargetURL, url):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        respFile = tempfile.TemporaryFile('rb+')
        url = urllib.quote(url, '') # url encoding
        self.doGet(serviceTargetURL + "?url=%s" %(url), respFile)
        return respFile

    def cmd(self):
       p = optparse.OptionParser()
       p.add_option('--mode', '-m', default="generateFromFile")
       p.add_option('--service', default=self.serviceTargetURL)
       p.add_option('--input', default="missing")
       p.add_option('--size', default="")
       p.add_option('--output', default="missing")
       options, arguments = p.parse_args()

       if(options.output == "missing"):
           print "No output file given"
       elif(options.input == "missing"):
           print "No input file given"
       else:
           if(options.mode == "generateFromFile"):
                datei = self.generateFromFile(options.service, options.input)
           elif(options.mode == "generateFromURL"):
               datei = self.generateFromURL(options.service, options.input)
           else:
               print "Wrong mode"
           output = file(options.output, 'wb+')
           output.write(datei.read())
           output.close()

if __name__ == '__main__':
    test = FITSService()
    test.cmd()
