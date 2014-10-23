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
        files = {"file": open(f, 'rb+')}
        r = requests.post(serviceTargetURL, files=files)
        text = r.content

        #write response to tempfile
        #respFile = tempfile.TemporaryFile('rb+')
        #respFile.write(r.content)
        #respFile.seek(0)

    #matching to find out the url of the temp file
        matchobj = re.search("JS9.Preload\(.*\"", text)
        preloadstring = matchobj.group()
        index = preloadstring.find("http")
        file_url = preloadstring[index: -1]

        self.generateFromURL("", file_url)
        #return respFile


    def generateFromURL(self, serviceTargetURL, url):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        url = urllib.quote(url, '') # url encoding
        webbrowser.open(serviceTargetURL + "?url=%s" %(url), new=0, autoraise=True)

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
    #datei = test.generateFromFile("", "C:/Users/schudan/Desktop/n49_0.5-7.0_flux.fits")
    #datei = test.generateFromURL("", "http://servicehub.mpdl.mpg.de/fits/api/file?file=%2Fopt%2Fapache-tomcat-7.0.55%2Ftemp%2Ffits8414614013714827600.fits")

    #not working yet, CORS needed
    #output = file('C:/Users/schudan/Desktop/test90.html', 'wb+')
    #output.write(datei.read())
    #output.close()