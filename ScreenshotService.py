from RestClient import RestClient
import tempfile
import optparse


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

    def cmd(self):
       p = optparse.OptionParser()
       p.add_option('--mode', '-m', default="captureFromURL")
       p.add_option('--service', default="http://vm15.mpdl.mpg.de/screenshot/take")
       p.add_option('--input', default="http://mpdl.mpg.de")
       p.add_option('--format', '-f', default="png")
       p.add_option('--size', default="")
       p.add_option('--crop', default="")
       p.add_option('--output', default="missing")
       options, arguments = p.parse_args()

       if(options.output == "missing"):
           print "No output file given"
       else:
           if(options.mode == "captureFromURL"):
                datei = self.captureFromURL(options.service, options.input, options.format, options.size, options.crop)
           elif(options.mode == "captureFromHTML"):
               datei = self.captureFromHTML(options.service, options.input, options.format, options.size, options.crop)
           else:
               print "Wrong mode"
           output = file(options.output, 'wb+')
           output.write(datei.read())
           output.close()

if __name__ == '__main__':
    test = ScreenshotService()
    test.cmd()
#     test = ScreenshotService()
#     datei = test.captureFromHTML("","Hallo Welt","png", "", "")
#     datei = test.captureFromURL("", "http://mpdl.mpg.de", "png", "", "")
#     output = file('C:/Users/schudan/Desktop/test45.png', 'wb+')
#     output.write(datei.read())
#     output.close()

