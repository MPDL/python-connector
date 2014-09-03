from RestClient import RestClient
import tempfile
import optparse
import sys

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

    def cmd(self):
       p = optparse.OptionParser()
       p.add_option('--mode', '-m', default="generateFromFile")
       p.add_option('--service', default="http://vm15.mpdl.mpg.de/swc/api/view")
       p.add_option('--input', default="missing")
       p.add_option('--size', default="")
       p.add_option('--portable', default="false")
       p.add_option('--output', default="missing")
       options, arguments = p.parse_args()

       if(options.output == "missing"):
           print "No output file given"
       elif(options.input == "missing"):
           print "No input file given"
       else:
           if(options.mode == "generateFromFile"):
                datei = self.generateFromFile(options.service, options.input, options.portable)
           elif(options.mode == "generateFromString"):
               datei = self.generateFromString(options.service, options.input, options.portable)
           elif(options.mode == "generateFromURL"):
               datei = self.generateFromURL(options.service, options.input, options.portable)
           else:
               print "Wrong mode"
           output = file(options.output, 'wb+')
           output.write(datei.read())
           output.close()

if __name__ == '__main__':
    test = SWC3DViewService()
    test.cmd()
    # datei = test.generateFromFile("", "C:/Users/schudan/Desktop/HB060602_3ptSoma.swc", "false")
    # datei = test.generateFromString("", "1 1 293.400000000000 175.050000000000 154.350000000000 0.450601700000 -1", "false")
    # datei = test.generateFromURL("", "http://localhost:8080/Service-api-webpage/Test.swc", "false")
    # output = file('C:/Users/schudan/Desktop/test30.html', 'wb+')
    # output.write(datei.read())
    # output.close()