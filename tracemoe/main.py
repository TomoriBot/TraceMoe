from . import utils
from . import exceptions
from . import config

from datetime import datetime



def get_duration(start, end):
    try:
        start = int(start)
        hours, remainder = divmod(start, 3600)
        minutes, seconds = divmod(remainder, 60)
        start = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    except:
        start = "?"
    try:
        end = int(end)
        hours, remainder = divmod(end, 3600)
        minutes, seconds = divmod(remainder, 60)
        end = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    except:
        start = "?"
    return "{} - {}".format(start, end)

class Info(object):

    def __init__(self, data):
        super(Info, self).__init__()
        data = data[0]
        if(isinstance(data, dict)):
            self.average_score = data.get("average_score", None)
            self.bannerImage = data.get("bannerImage", None)
            self.characters = data.get("characters", None)
            self.coverImage = data.get("coverImage", None)
            self.description = data.get("description", None)
            self.duration = data.get("duration", None)
            self.endDate = data.get("endDate", None)
            self.episodes = data.get("episodes", None)
            self.externalLinks = data.get("externalLinks", None)
            self.format = data.get("format", None)
            self.genres = data.get("genres", None)
            self.hashtag = data.get("hashtag", None)
            self.id = data.get("id", None)
            self.idMal = data.get("idMal", None)
            self.isAdult = data.get("isAdult", None)
            self.meanScore = data.get("meanScore", None)
            self.popularity = data.get("popularity", None)
            self.rankings = data.get("rankings", None)
            self.relations = data.get("relations", None)
            self.season = data.get("season", None)
            self.staff = data.get("staff", None)
            self.startDate = data.get("startDate", None)
            self.stats = data.get("stats", None)
            self.status = data.get("status", None)
            self.studios = data.get("studios", None)
            self.synonyms = data.get("synonyms", None)
            self.synonyms_chinese = data.get("synonyms_chinese", None)
            self.tags = data.get("tags", None)
            self.title = data.get("title", None)
            self.trailer = data.get("trailer", None)
            self.type = data.get("type", None)
            self.updatedAt = data.get("updatedAt", None)
        else:
            raise exceptions.TraceException("Invalid instance.")

    def getCharacters(self, role):
        if role.upper() not in ["MAIN", "SUPPORTING"]:
            raise exceptions.TraceException("Invalid role type.")
        __tmp = []
        for x in self.characters["edges"]:
            if x["role"] == role.upper():
                __tmp.append(x)
        return __tmp

    def getRelations(self, relationType):
        if relationType.upper() not in ["PREQUEL", "ADAPTATION", "SEQUEL"]:
            raise exceptions.TraceException("Invalid relationType type.")
        __tmp = []
        for x in self.relations["edges"]:
            if x["role"] == relationType.upper():
                __tmp.append(x)
        return __tmp

    def getTrailer(self):
        if self.trailer["site"] == "youtube":
            return f"https://www.youtube.com/watch?v={self.trailer['id']}"
        else:
            raise exceptions.TraceException(f"Not implemented for site '{self.trailer['site']}' yet.")

    def __repr__(self):
        return f"TraceMoeInfo({self.title})"

    def __str__(self):
        return f"TraceMoeInfo({self.title})"


class MatchInfo(object):
    host = config.host
    headers = config.headers

    def __init__(self, data):
        super(MatchInfo, self).__init__()
        if(isinstance(data, dict)):
            self._from = data.get("from", None)
            self._to = data.get("to", None)
            self.anilist_id = data.get("anilist_id", "?")
            self.i = data.get("i", None)
            self.start = data.get("start", 0)
            self.end = data.get("end", 0)
            self.file = data.get("file", None)
            self.episode = data.get("episode", "?")
            self.expires = data.get("expires", None)
            self.token = data.get("token", None)
            self.tokenThumb = data.get("tokenthumb", None)
            self.diff = data.get("diff", None)
            self.title = data.get("title", "?")
            self.title_native = data.get("title_native", "?")
            self.title_chinese = data.get("title_chinese", "?")
            self.title_english = data.get("title_english", "?")
            self.title_romaji = data.get("title_romaji", "?")
            self.is_adult = data.get("is_adult", None)
            self.t = data.get("t", None)
            self.anime_url = f"https://anilist.co/anime/{self.anilist_id}"
            self.thumbnail_preview = f"{self.host['main']}/thumbnail.php?anilist_id={self.anilist_id}&file={utils.urlEncode(self.file)}&t={self.t}&token={self.tokenThumb}"
            self.video_preview = f"{self.host['main']}/{self.anilist_id}/{utils.urlEncode(self.file)}?start={self.start}&end={self.end}&token={self.token}"
            self.info = None

    def getInfo(self):
        if(getattr(self, 'info', None) is None):
            resp = utils.sendGet(f"{self.host['main']}/info?anilist_id={self.anilist_id}")
            try:
                self.info = Info(resp.json())
            except Exception:
                raise exceptions.TraceException("Failed to decode json from api.")
            return self.info
        else:
            return self.info

    def getDuration(self):
        if(getattr(self, 'info', None) is None):
            resp = utils.sendGet(f"{self.host['main']}/duration.php?anilist_id={self.anilist_id}&file={self.file}&token={self.token}")
            if resp.status_code == 200:
                try:
                    self.duration = resp.content
                except Exception:
                    raise exceptions.TraceException("Failed to decode json from api.")
                return self.duration
            else:
                raise exceptions.TraceException(resp.status_code, resp.content)
        else:
            return self.duration

    def getAllInfo(self):
        self.getInfo()
        self.getDuration()

    def __repr__(self):
        return f"TraceMoeMatchInfo({self.title_romaji})"

    def __str__(self):
        return f"TraceMoeMatchInfo({self.title_romaji})"


class AniInfo(object):
    host = config.host
    headers = config.headers

    def __init__(self, data):
        super(AniInfo, self).__init__()
        self.data = data
        if(isinstance(data, dict)):
            self.cacheHit = data.get("CacheHit", None)
            self.rawDocsCount = data.get("RawDocsCount", None)
            self.rawDocsSearchTime = data.get("RawDocsSearchTime", None)
            self.reRankSearchTime = data.get("ReRankSearchTime", None)
            self.limit = data.get("limit", None)
            self.limit_ttl = data.get("limit_ttl", None)
            self.quota = data.get("quota", None)
            self.quota_ttl = data.get("quota_ttl", None)
        else:
            raise exceptions.TraceException("Invalid instance.")

    def getMatchInfo(self, index):
        return MatchInfo(self.data["docs"][index])
                                 
    def getAllInfo(self):
        return [MatchInfo(data) for data in self.data["docs"]]
                                 
    def getAnimes(self):
        animes = []
        for info in sorted(self.getAllInfo(), key=lambda k: k.diff, reverse=False):
            info.getInfo()
            animes.append({
                "title": info.title,
                "titles": {
                    "english": info.title_english,
                    "romaji": info.title_romaji
                },
                "preview": info.thumbnail_preview,
                "episode": info.episode,
                "url": info.anime_url,
                "similarity": round(100.0 - info.diff, 1),
                "duration": get_duration(info.start, info.end)
            })
        return animes


class Search(AniInfo):

    def __init__(self, image=None, url=None, useImageProxy=False, filter="", trial="0", **kwargs):
        self.filter = filter
        self.trial = trial
        self.data = None
        if url:
            if useImageProxy:
#                 print("using proxy")
                self.searchUsingUrl(f"{self.host['imgproxy']}/imgproxy?url={url}", **kwargs)
            else:
                self.searchUsingUrl(url, **kwargs)
        elif image:
            self.searchUsingImage(image, **kwargs)
        else:
            raise exceptions.TraceException("Invalid args", "No image source")

    def searchUsingUrl(self, url, **kwargs):
        imageRaw = utils.downloadFile(url, save=False, **kwargs)
        self.searchUsingImage(imageRaw, **kwargs)

    def searchUsingImage(self, image, **kwargs):
        sendData = utils.getSendData(image, self.filter, self.trial)
        self.data = utils.sendPost(f"{self.host['main']}/search", data=sendData, headers=self.headers).json()
        super(Search, self).__init__(self.data)

    def __repr__(self):
        return f"TraceMoeAniInfo({self.data['docs'][0]['anilist_id']})"

    def __str__(self):
        return f"TraceMoeAniInfo({self.data['docs'][0]['anilist_id']})"
