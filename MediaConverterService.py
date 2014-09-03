from RestClient import RestClient
import tempfile

class MediaConverterService(RestClient):


    serviceTargetURL = "http://vm15.mpdl.mpg.de/media-conversion/convert"

    def convertFromURL(self, serviceTargetURL, mediaURL, outputFormat, outputSize, crop):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        cFile = tempfile.TemporaryFile('rb+')
        self.doGet(serviceTargetURL + self.addParameterstoURL(mediaURL, outputFormat, outputSize, crop), cFile)
        return cFile

    def convertFromFile(self, serviceTargetURL, mediaFile, outputFormat, outputSize, crop):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        cFile = tempfile.TemporaryFile('rb+')
        serviceTargetURL = serviceTargetURL + self.addParameterstoURL("", outputFormat, outputSize, crop)
        self.doPost2(serviceTargetURL, mediaFile, cFile)
        return cFile

if __name__ == '__main__':
    test = MediaConverterService()
#    datei = test.convertFromURL("", "https://www.wikimedia.de/w/images.homepage/thumb/1/19/Digikompzlogo.jpg/170px-Digikompzlogo.jpg", "png", "", "" )
    datei = test.convertFromFile("", "C:/Users/schudan/Desktop/test2.png", "png", "", "")
    output = file('C:/Users/schudan/Desktop/test19.png', 'wb+')
    output.write(datei.read())
    output.close()