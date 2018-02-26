from RiotAPI import RiotAPI
from LocalStatic import LocalStatic

def main():
    api = RiotAPI('')

    #ls = LocalStatic(api.get_champions_by_id_list())

    #s1_name = "metaleaguesystem"
    #s1= api.get_summoner_by_name('metaleaguesystem')
    s1_id = 71460630
    print(s1_id)
    print(LocalStatic.get_champion_by_id('202'))
    print(LocalStatic.get_champion_name_by_id("202"))
    sChamps = api.get_champion_masteries_by_summoner_id(s1_id)

    '''
    {'championPointsSinceLastLevel': 147023,
    'playerId': 71460630,
    'championPointsUntilNextLevel': 0,
    'chestGranted': True,
    'tokensEarned': 0,
    'championPoints': 168623,
    'championLevel': 7,
    'lastPlayTime': 1516487394000,
    'championId': 268}
    '''

    chest_champs = []
    for champ in sChamps:
        if champ['chestGranted']:
            chest_champs.append(LocalStatic.get_champion_name_by_id(str(champ['championId'])))
    print(chest_champs)

    #top_champ = sChamps[0]
    #print(top_champ)
    #print(top_champ['championId'])
    #top_champ_name=api.get_champion_by_id(top_champ['championId'])['key']
    #print(top_champ_name)


    #print("The champ with most mastery points for the player ", s1_name, " is: ", top_champ_name , " with ", top_champ['championPoints'], " points")


    #r = api.get_summoner_by_name('metaleaguesystem')
    #print(r)


if __name__ == "__main__":
    main()
