from RiotAPI import RiotAPI
from LocalStatic import LocalStatic
import datetime
import RiotConstants
import PrivateData
import ChampionList
import FreeRotation

epoch = datetime.datetime.utcfromtimestamp(0)

api = RiotAPI(PrivateData.RiotAPIKey)
ls = LocalStatic(ChampionList.list["data"])


def main():

    s1 = api.get_summoner_by_name(input("Please enter League Account Name"))
    key = input("Please enter RiotAPI key")

    #s1 = PrivateData.meta
    #key = PrivateData.RiotAPIKey


    #ls = LocalStatic(api.get_champions_by_id_list())
    print("===")

    #print(find_champs("MyInputFile.txt"))


    sChamps = api.get_champion_masteries_by_summoner_id(s1['id'])
    chest_champs = []
    for champ in sChamps:
        if champ['chestGranted']:
            chest_champs.append(ls.get_champion_name_by_id(str(champ['championId'])))
    print("Chest granted on: ", chest_champs)
    


    week_td = datetime.timedelta(weeks=1)

    beginTime = datetime.datetime(year=2018, month=2, day=27)
    print(beginTime)


    owned_champs = []
    for rot in FreeRotation.free_rotation:
        matches = api.request(RiotConstants.URL['matchlist_by_account_id'].format(account_id=s1['accountId']),
                              {'beginTime': int(unix_time_millis(beginTime))})
        owned_champs = list(set (owned_champs + check_week(matches, rot)))
        beginTime = beginTime - week_td

    print("===")
    print("You definitely own the champions:")
    print(owned_champs)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


def check_week(matches={}, free_rot=()):
    owned_champs = []
    for match in matches['matches']:
        t_champ_dynamic = api.request(RiotConstants.URL['champion_by_id_dynamic'].format(id=match['champion']))
        t_champ_name = ls.get_champion_name_by_id(t_champ_dynamic['id'])
        if not t_champ_name in free_rot:
            owned_champs.append(t_champ_name)
    return owned_champs

'''
def find_champs(file_name):
    champs = []
    file = open(file_name, 'r')

    for line in file:
        for champ in ls.champion_list:
            print (champ)
            cur_champ_name = champ['name']
            print(cur_champ_name)
            if not line.find() == -1:
                champs.append(cur_champ_name)

    return champs
'''

if __name__ == "__main__":
    main()
