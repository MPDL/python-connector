python-connector
================
A .py library which offers the quickest and the most convenient way to use diverse [mpdl services][1].


Usage:
--------------------------------
Using mpdl [screenshot service][2] (eg.) by doing
```
screenshot = ScreenshotService()
ScreenshotService.captureFromURL("serviceTargetURL", "url", "outputFormat", "outputSize", "crop")
outputFile = file('filepath', 'wb+')
outputFile.write(datei.read())
```

[1]: http://vm15.mpdl.mpg.de
[2]: https://github.com/MPDL/screenshot-service

