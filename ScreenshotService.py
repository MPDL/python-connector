from RestClient import RestClient
import tempfile


class ScreenshotService(RestClient):


    serviceTargetURL = "http://vm15.mpdl.mpg.de/screenshot/take"

    def captureFromURL (self, serviceTargetURL, url, outputFormat, outputSize, crop):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        ssFile = tempfile.TemporaryFile('rb+')
        self.doGet(serviceTargetURL + self.addParameterstoURL(url, outputFormat, outputSize, crop), ssFile)
        return ssFile

    def captureFromHTML(self, serviceTargetURL, html, outputFormat, outputSize, crop):
        if(serviceTargetURL == ""):
            serviceTargetURL = self.serviceTargetURL
        ssFile = tempfile.TemporaryFile('rb+')
        serviceTargetURL = serviceTargetURL + self.addParameterstoURL("", outputFormat, outputSize, crop)
        params = {}
        params["html"] = html
        self.doPost(serviceTargetURL,params,ssFile)
        return ssFile

if __name__ == '__main__':

    test = ScreenshotService()
#    datei = test.captureFromHTML("","Hallo Welt","png", "", "")
    datei = test.captureFromURL("", "http://mpdl.mpg.de", "png", "", "")
    output = file('C:/Users/schudan/Desktop/test45.png', 'wb+')
    output.write(datei.read())
    output.close()

