python-connector
================
A .py library which offers the quickest and the most convenient way to use diverse [mpdl web services][1]:


* SWC Service
  *  SWC 3D View Service
  *  SWC Analysis Service
* Screenshot Service
* Media conversion Service

Installation:
--------------------------------
Download the .py files and copy them into your Python/Lib folder or to any other folder in your PYTONPATH.


Usage:
--------------------------------
Using mpdl [Screenshot service][2] (eg.) by doing
```
from ScreenshotService import *

screenshot = ScreenshotService()
tempFile = ScreenshotService.captureFromURL("serviceTargetURL", "url", "outputFormat", "outputSize", "crop")
outputFile = file('filepath', 'wb+')
outputFile.write(result.read())
```
Details
--------------------------------
* SWC 3D View Service (SWC3DViewService.py)
  * Methods
    * generateFromFile(self, serviceTargetURL, inputFile, portable)
    * generateFromString(self, serviceTargetURL, inputStrng, portable)
    * generateFromURL(self, serviceTargetURL, inputURL, portable)
* SWC Analysis Service (SWCAnalysisService.py)
  * Methods
    * getAnalysisFromFile(self, serviceTargetURL, inputFile)
    * getAnalysisFromString(self, serviceTargetURL, inputString, numberOfBins="10")
    * getAnalysisFromURL(self, serviceTargetURL, inputURL, numberOfBins="10")
* Screenshot Service (ScreenshotService.py)
    * Methods
      * captureFromURL (self, serviceTargetURL, inputURL, outputFormat, outputSize, crop)
      * captureFromHTML(self, serviceTargetURL, inputHTML, outputFormat, outputSize, crop)
* Media conversion Service (MediaConversionService.py)
  * Methods
    * convertFromFile(self, serviceTargetURL, mediaFile, outputFormat, outputSize, crop)
    * convertFromURL(self, serviceTargetURL, mediaURL, outputFormat, outputSize, crop)

**All parameters are Strings!** 
    

[1]: http://vm15.mpdl.mpg.de
[2]: https://github.com/MPDL/screenshot-service

