TraceMoe
----

[![Version 1.0.0](https://img.shields.io/badge/stable-1.0.0-brightgreen.svg "Version 1.0.0")](https://github.com/fauzanardh/TraceMoe) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Supported python versions: 3.6](https://img.shields.io/badge/python-3.6-green.svg "Supported python versions: 3.6")](https://www.python.org/download/releases/3.6/)

The other version of anime screenshot finder ;)

**Not yet compatible for python2** 

Refrence
----

- Based : [Soruly's Repo](https://github.com/soruly/trace.moe)
- WEB   : [The web](https://trace.moe/)
- Recoded From: [Anysz's](https://github.com/anysz/Image2Anime)

Usage
----

 **First of all, you need to install the library**

     $ python setup.py install

 **First use**

     >>> import tracemoe

 **To start search the anime by local path**

     >>> res = tracemoe.Search(image='/path/to/source')

 **To start search the anime by io text/buffer**

     >>> with open(r'/path/to/source', 'rb') as fp:
     ...... res = tracemoe.Search(image=fp)

 **To start search the anime by raw image binary**

     >>> res = tracemoe.Search(image=b"raw image data")

 **To start search the anime by url**

     >>> res = tracemoe.Search(url="http://the_image_url_here")

 **To get the results**

     >>> print(res.getMatchInfo(0))  # Initialize the first match

 **To get the other informations**

     >>> first_match = res.getMatchInfo(0)  # Initialize the first match
     >>> title_romaji = first_match.title_romaji  # Get the title in romaji
     >>> first_match.getAllInfo()  # Initialize Info and Duration
     >>> first_match.info.getCharacters("MAIN")  # Get characters based on the role

 **QnA**

     Q : What's the first step?
     A : python setup.py install
     Q : Lib imported not found?
     A : pip install PACKAGENAME
     Q : Your issue not solved?
     A : Create new issue with what your problem and what you want to achieve :D


Special Thanks
----
[Soruly](https://github.com/soruly)

Author
----
[Anysz](https://instagram.com/nugra.z) / [@Anysz](https://github.com/anysz)

Recoded By
----
[@Fauzanardh](https://github.com/fauzanardh)
