from RestClient import RestClient
import tempfile
import optparse

class SWCAnalysisService(RestClient):

    serviceTargetURL = "http://vm15.mpdl.mpg.de/swc/api/analyze"

    def getAnalysisFromFile(self, serviceTargetURL, f):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        respFile = tempfile.TemporaryFile('rb+')
        self.doPost2(serviceTargetURL, f, respFile)
        return respFile


    def getAnalysisFromString(self, serviceTargetURL, swcInString, numberOfBins="10"):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        respFile = tempfile.TemporaryFile('rb+')
        params = {}
        params["swc"] = swcInString
        params["numberOfBins"] = numberOfBins
        self.doPost(serviceTargetURL, params, respFile)
        return respFile


    def getAnalysisFromURL(self, serviceTargetURL, url, numberOfBins="10"):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        respFile = tempfile.TemporaryFile('rb+')
        self.doGet(serviceTargetURL + "?url=%s&numberOfBins=%s" %(url, numberOfBins), respFile)
        return respFile


    def cmd(self):
       p = optparse.OptionParser()
       p.add_option('--mode', '-m', default="getAnalysisFromString")
       p.add_option('--service', default="http://vm15.mpdl.mpg.de/swc/api/analyze")
       p.add_option('--input', default="5")
       p.add_option('--size', default="")
       p.add_option('--bins', default="10")
       p.add_option('--output', default="missing")
       options, arguments = p.parse_args()

       if(options.output == "missing"):
           print "No output file given"
       else:
           if(options.mode == "getAnalysisFromFile"):
                datei = self.getAnalysisFromFile(options.service, options.input)
           elif(options.mode == "getAnalysisFromString"):
               datei = self.getAnalysisFromString(options.service, options.input, options.bins)
           elif(options.mode == "getAnalysisFromURL"):
               datei = self.getAnalysisFromURL(options.service, options.input, options.bins)
           else:
               print "Wrong mode"
           output = file(options.output, 'wb+')
           output.write(datei.read())
           output.close()

if __name__ == '__main__':
    test = SWCAnalysisService()
    test.cmd()
    # datei = test.getAnalysisFromFile("", "C:/Users/schudan/Desktop/HB060602_3ptSoma.swc")
    # datei = test.getAnalysisFromString("", "5")
    # datei = test.getAnalysisFromURL("", "http://localhost:8080/Service-api-webpage/Test.swc")
    # output = file('C:/Users/schudan/Desktop/test27.html', 'wb+')
    # output.write(datei.read())
    # output.close()