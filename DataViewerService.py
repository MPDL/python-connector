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
        files = {"file": open(f, 'rb+')}
        params = {"mimetype": mimetype}
        r = requests.post(serviceTargetURL, files= files, data=params)
        text = r.content
        print r.content

    #matching to find out the url of the temp file
        matchobj = re.search("JS9.Preload\(.*\"", text)
        if matchobj!= None:
            preloadstring = matchobj.group()
            index = preloadstring.find("http")
            file_url = preloadstring[index: -1]

            self.generateFromURL("", file_url, mimetype)
        else:
            respFile = tempfile.TemporaryFile('rb+')
            respFile.write(r.content)
            respFile.seek(0)
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
    #datei = test.generateFromFile("", "C:/Users/schudan/Desktop/n49_0.5-7.0_flux.fits", "fits")
    #datei = test.generateFromFile("", "C:/Users/schudan/Desktop/HB060602_3ptSoma.swc", "swc")
    #test.generateFromURL("", "http://servicehub.mpdl.mpg.de/fits/api/file?file=%2Fopt%2Fapache-tomcat-7.0.55%2Ftemp%2Ffits8414614013714827600.fits", "fits")
    #datei = test.generateFromURL("", "https://raw.githubusercontent.com/JaneliaSciComp/SharkViewer/master/html/swc/test.swc", "swc")

    #not working yet, CORS needed
    #output = file('C:/Users/schudan/Desktop/test90.html', 'wb+')
    #output.write(datei.read())
    #output.close()
