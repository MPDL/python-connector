from RestClient import RestClient
import tempfile
import webbrowser
import urllib
import requests
import re
import urllib2
import optparse

class DataViewerService(RestClient):

    serviceTargetURL = "http://servicehub.mpdl.mpg.de/data-viewer/api/view"

    def generateFromFile(self, serviceTargetURL, f, mimetype):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        params = {"mimetype": mimetype}
        respFile = tempfile.TemporaryFile('rb+')
        self.doPost3(serviceTargetURL, params, f, respFile)
        return respFile


    def generateFromURL(self, serviceTargetURL, url, mimetype):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        url = urllib.quote(url, '') # url encoding
        webbrowser.open(serviceTargetURL + "?url=%s&mimetype=%s" %(url,mimetype), new=0, autoraise=True)
        respFile = tempfile.TemporaryFile('rb+')
        self.doGet(serviceTargetURL + "?url=%s&mimetype=%s" %(url,mimetype) , respFile)
        return respFile


    def cmd(self):
       p = optparse.OptionParser()
       p.add_option('--mode', '-m', default="generateFromFile")
       p.add_option('--service', default=self.serviceTargetURL)
       p.add_option('--input', default="missing")
       p.add_option('--size', default="")
       p.add_option('--output', default="missing")
       p.add_option('--mimetype', default="fits")
       options, arguments = p.parse_args()

       if(options.output == "missing"):
           print "No output file given"
       elif(options.input == "missing"):
           print "No input file given"
       else:
           if(options.mode == "generateFromFile"):
                datei = self.generateFromFile(options.service, options.input,options.mimetype)
           elif(options.mode == "generateFromURL"):
               datei = self.generateFromURL(options.service, options.input, options.mimetype)
           else:
               print "Wrong mode"

           output = file(options.output, 'wb+')
           output.write(datei.read())
           output.close()


if __name__ == '__main__':
    test = DataViewerService()
    test.cmd()

