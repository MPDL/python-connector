from RestClient import RestClient
import tempfile

class SWC3DViewService(RestClient):


    serviceTargetURL = "http://vm15.mpdl.mpg.de/swc/api/view"

    def generateFromFile(self, serviceTargetURL, f, portable):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        respFile = tempfile.TemporaryFile('rb+')
        params = {}
        swcFile = file(f, 'r')
        params["swc"] = swcFile.read()
        params["portable"] = str(portable)
        self.doPost(serviceTargetURL, params, respFile)
        return respFile

    def generateFromString(self, serviceTargetURL, swcInString, portable):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        respFile = tempfile.TemporaryFile('rb+')
        params = {}
        params["swc"] = swcInString
        params["portable"] = str(portable)
        self.doPost(serviceTargetURL, params, respFile)
        return respFile

    def generateFromURL(self, serviceTargetURL, url, portable):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        respFile = tempfile.TemporaryFile('rb+')
        self.doGet(serviceTargetURL + "?url=%s&portable=%s" %(url, portable) , respFile)
        return respFile

if __name__ == '__main__':
    test = SWC3DViewService()
    datei = test.generateFromFile("", "C:/Users/schudan/Desktop/HB060602_3ptSoma.swc", "false")
#    datei = test.generateFromString("", "1 1 293.400000000000 175.050000000000 154.350000000000 0.450601700000 -1", "false")
#    datei = test.generateFromURL("", "http://localhost:8080/Service-api-webpage/Test.swc", "false")
    output = file('C:/Users/schudan/Desktop/test30.html', 'wb+')
    output.write(datei.read())
    output.close()