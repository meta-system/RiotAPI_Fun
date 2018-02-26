URL = {
    'base': 'https://{region}.api.riotgames.com/lol{core}api_key={api_key}',
    'summoner_by_name': '/summoner/v3/summoners/by-name/{summonerName}',
    'champion_masteries': '/champion-mastery/v3/champion-masteries/by-summoner/{summonerID}',
    'champion_name_by_id': '/static-data/v3/champions/{id}',
    'champions_by_id_list': '/static-data/v3/champions?locale=en_US&dataById=true{sign}'
}


REGIONS = {
    'europe_nordic_and_east': 'eun1',
    'europe_west': 'euw1'
}