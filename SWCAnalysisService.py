from RestClient import RestClient
import tempfile

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

if __name__ == '__main__':
    test = SWCAnalysisService()
 #   datei = test.getAnalysisFromFile("", "C:/Users/schudan/Desktop/HB060602_3ptSoma.swc")
    datei = test.getAnalysisFromString("", "5")
 #   datei = test.getAnalysisFromURL("", "http://localhost:8080/Service-api-webpage/Test.swc")
    output = file('C:/Users/schudan/Desktop/test27.html', 'wb+')
    output.write(datei.read())
    output.close()