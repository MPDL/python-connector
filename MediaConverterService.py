from RestClient import RestClient
import tempfile
import optparse


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

    def cmd(self):
       p = optparse.OptionParser()
       p.add_option('--mode', '-m', default="convertFromURL")
       p.add_option('--service', default="http://vm15.mpdl.mpg.de/media-conversion/convert")
       p.add_option('--input', default="https://www.wikimedia.de/w/images.homepage/thumb/1/19/Digikompzlogo.jpg/170px-Digikompzlogo.jpg")
       p.add_option('--format', '-f', default="png")
       p.add_option('--size', default="")
       p.add_option('--crop', default="")
       p.add_option('--output', default="missing")
       options, arguments = p.parse_args()

       if(options.output == "missing"):
           print "No output file given"
       else:
           if(options.mode == "convertFromFile"):
                datei = self.convertFromFile(options.service, options.input, options.format, options.size, options.crop)
           elif(options.mode == "convertFromURL"):
               datei = self.convertFromURL(options.service, options.input, options.format, options.size, options.crop)
           else:
               print "Wrong mode"
           output = file(options.output, 'wb+')
           output.write(datei.read())
           output.close()

if __name__ == '__main__':

     test = MediaConverterService()
     test.cmd()
#     datei = test.convertFromURL("", "https://www.wikimedia.de/w/images.homepage/thumb/1/19/Digikompzlogo.jpg/170px-Digikompzlogo.jpg", "png", "", "" )
#     datei = test.convertFromFile("", "C:/Users/schudan/Desktop/test2.png", "png", "", "")
#     output = file('C:/Users/schudan/Desktop/test19.png', 'wb+')
#     output.write(datei.read())
#     output.close()