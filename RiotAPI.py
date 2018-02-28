import requests
import RiotConstants as Consts


class RiotAPI(object):
    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region

    def request(self, url_core, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        url = Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                core=url_core,
                api_key=self.api_key
         )
        response = requests.get(url,
            params=args
        )
        #print(response.url)
        return response.json()

    def get_summoner_by_name(self, summonerName):
        url_core = Consts.URL['summoner_by_name'].format(
            summonerName=summonerName,
            sign='?'
        )
        return self.request(url_core)

    def get_champion_masteries_by_summoner_id(self, id):
        url_core = Consts.URL['champion_masteries'].format(
            summonerID=id,
            sign='?'
        )
        return self.request(url_core)

    def get_champion_by_id(self, champID):
        url_core = Consts.URL['champion_by_id'].format(
            id=champID
        )
        return self.request(url_core)

    def get_champions_by_id_list(self):
        core = Consts.URL['champions_by_id_list'].format(sign='&')
        return self.request(core)
