URL = {
    'base': 'https://{region}.api.riotgames.com/lol{core}',
    'summoner_by_name': '/summoner/v3/summoners/by-name/{summonerName}',
    'champion_masteries': '/champion-mastery/v3/champion-masteries/by-summoner/{summonerID}',
    'champion_by_id': '/static-data/v3/champions/{id}',
    'champions_by_id_list': '/static-data/v3/champions?locale=en_US&dataById=true',
    'matchlist_by_account_id': '/match/v3/matchlists/by-account/{account_id}',
    'champion_by_id_dynamic': '/platform/v3/champions/{id}'
}


REGIONS = {
    'europe_nordic_and_east': 'eun1',
    'europe_west': 'euw1'
}