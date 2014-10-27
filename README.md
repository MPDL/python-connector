python-connector
================
A .py library which offers the quickest and the most convenient way to use diverse [mpdl web services][1]:


* [SWC Service][2]
  *  SWC 3D View Service
  *  SWC Analysis Service
* [Screenshot Service][3]
* [Media conversion Service][4]
* [Data Viewer Service][5]
* [FITS Service][6]

Installation:
--------------------------------
Download the .py files and copy them into your Python/Lib folder or to any other folder in your PYTONPATH.


Usage:
--------------------------------
Using mpdl [Screenshot service][3] (eg.) by doing
```
from ScreenshotService import *

screenshot = ScreenshotService()
tempFile = ScreenshotService.captureFromURL("serviceTargetURL", "url", "outputFormat", "outputSize", "crop")
outputFile = file('filepath', 'wb+')
outputFile.write(result.read())
```
Details
--------------------------------
* **SWC 3D View Service** (SWC3DViewService.py)
  * Methods
    * generateFromFile(self, serviceTargetURL, inputFile, portable)
    * generateFromString(self, serviceTargetURL, inputStrng, portable)
    * generateFromURL(self, serviceTargetURL, inputURL, portable)
* **SWC Analysis Service** (SWCAnalysisService.py)
  * Methods
    * getAnalysisFromFile(self, serviceTargetURL, inputFile)
    * getAnalysisFromString(self, serviceTargetURL, inputString, numberOfBins="10")
    * getAnalysisFromURL(self, serviceTargetURL, inputURL, numberOfBins="10")
* **Screenshot Service** (ScreenshotService.py)
  * Methods
    * captureFromURL (self, serviceTargetURL, inputURL, outputFormat, outputSize, crop)
    * captureFromHTML(self, serviceTargetURL, inputHTML, outputFormat, outputSize, crop)
* **Media conversion Service** (MediaConversionService.py)
  * Methods
    * convertFromFile(self, serviceTargetURL, mediaFile, outputFormat, outputSize, crop)
    * convertFromURL(self, serviceTargetURL, mediaURL, outputFormat, outputSize, crop)
* **Data Viewer Service** (DataViewerService.py)
  * Methods
    * generateFromFile(self, serviceTargetURL, inputFile, mimetype)
    * generateFromURL(self, serviceTargetURL, inputURL, mimetype)
* **FITS Service** (FITSService.py)
  * Methods
    * generateFromFile(self, serviceTargetURL, inputFile)
    * generateFromURL(self, serviceTargetURL, inputURL)

 
 **All parameters are Strings!**

 **All methods return temporary files**
 
 Command line
----------------------------------
The above described services can also be used as command line tools. Just add the folder with the .py files to your PATH variable and type the name of one of the services. Use the --mode argument to choose a method:

```
(e.g) ScreenshotService --mode captureFromeURL
```
To see the various argument options for each service type in the name of the service and --help.

[1]: http://vm15.mpdl.mpg.de
[2]: https://github.com/MPDL/swc-service
[3]: https://github.com/MPDL/screenshot-service
[4]: https://github.com/MPDL/media-conversion-service
[5]: https://github.com/MPDL/data-viewer-service
[6]: https://github.com/MPDL/fits-service
