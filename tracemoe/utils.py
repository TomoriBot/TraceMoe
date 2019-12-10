import sys
import base64
import requests
from . import config
from . import exceptions
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote
headers = config.headers
session = requests.session()


def urlEncode(data):
    if(isinstance(data, dict)):
        return urlencode(data)
    elif(isinstance(data, str)):
        return quote(data)
    else:
        raise exceptions.TraceException("Invalid data type.")


def getImageB64(imagePathOrObjectOrRawBinary):
    if(getattr(type(imagePathOrObjectOrRawBinary), '__name__') == "BufferedReader"):
        __data = imagePathOrObjectOrRawBinary.read()
        imagePathOrObjectOrRawBinary.close()
    elif(getattr(type(imagePathOrObjectOrRawBinary), '__name__') == "bytes"):
        __data = imagePathOrObjectOrRawBinary
    elif(getattr(type(imagePathOrObjectOrRawBinary), '__name__') == "str"):
        with open(imagePathOrObjectOrRawBinary, "rb") as fp:
            __data = fp.read()
    else:
        raise exceptions.TraceException("Invalid data type.")
    return base64.b64encode(__data)


def getSendData(imagePathOrObjectOrRawBinary, filter="", trial="0"):
    imageB64 = getImageB64(imagePathOrObjectOrRawBinary)
    return f"data={urlEncode(f'data:image/jpeg;base64,{imageB64.decode()}')}&filter={filter}&trial={trial}"


def sendPost(url, **kwargs):
    headers = kwargs.pop("headers", None)
    data = kwargs.pop("data", None)
    if data is None:
        exceptions.TraceException("Data can't be none.")
    resp = session.post(url, data=data, headers=headers, **kwargs)
    return resp


def sendGet(url, **kwargs):
    headers = kwargs.pop("headers", None)
    resp = session.get(url, headers=headers, **kwargs)
    return resp


def downloadFile(url, temp_path="temp.dat", saveFile=True, **kwargs):
#     print(f"Fetching {url}")
    headers = kwargs.pop("headers", None)
    timeout = kwargs.pop("timeout", 60)
    printLen = 0
    if headers is not None:
        headers = {'Accept-Encoding': None, **headers}
    else:
        headers = {"Accept-Encoding": None}
    __b = b''
    try:
        notContentLength = False
        try:
            contentLength = int(requests.head(url, headers=headers).headers["Content-Length"])
        except KeyError:
            notContentLength = True
            index = 1
        with sendGet(url, headers=headers, timeout=timeout) as fp:
#             if not notContentLength:
#                 print(f"Downloading file with size: {(contentLength/1024/1024):.3f} MB")
            for chunk in fp.iter_content(chunk_size=1024*100):
                __b += chunk
#                 if notContentLength:
#                     printData = f"Download in progress{'.'*index} \r"
#                     printLen = len(printData)
#                     sys.stdout.write(printData)
#                     sys.stdout.flush()
#                     index += 1
#                 else:
#                     printData = f"Download progress: {((len(__b)/contentLength)*100):.3f}% \r"
#                     printLen = len(printData)
#                     sys.stdout.write(printData)
#                     sys.stdout.flush()
#         printData = "Download finished."
#         padLen = printLen - len(printData)
#         print(f"{printData}{' '*padLen}")
#         if saveFile:
#             with open(temp_path, 'wb+') as fp:
#                 fp.write(__b)
        return __b
    except Exception as e:
        raise exceptions.TraceException("Download failed.", f"Reason: {str(e)}")
