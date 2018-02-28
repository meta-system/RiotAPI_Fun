from RiotAPI import RiotAPI
from LocalStatic import LocalStatic
import datetime
import RiotConstants
import PrivateData
import ChampionList

epoch = datetime.datetime.utcfromtimestamp(0)


def main():
    api = RiotAPI(PrivateData.RiotAPIKey)
    s1 = PrivateData.meta
    # s1_id = 71460630
    #print(s1)
    # ls = LocalStatic(api.get_champions_by_id_list())
    ls = LocalStatic(ChampionList.list)
    print("===")

    '''
    sChamps = api.get_champion_masteries_by_summoner_id(s1['id'])
    chest_champs = []
    for champ in sChamps:
        if champ['chestGranted']:
            chest_champs.append(ls.get_champion_name_by_id(str(champ['championId'])))
    print("Chest granted on: ", chest_champs)
    '''

    milli_secs_per_week = 1000 * 60 * 60 * 24 * 7

    end_time_dt = datetime.datetime.now()
    week_td = datetime.timedelta(weeks=1)

    first_rot_dt = datetime.datetime(year=2018, month=2, day=27)
    beginTime = int((unix_time_millis(first_rot_dt)))
    print (beginTime)
    matches = api.request(RiotConstants.URL[
                              'matchlist_by_account_id'].format(account_id=s1['accountId']),
                          {'beginTime':int(unix_time_millis(first_rot_dt))})

    owned_champs = []


    for match in matches['matches']:
        t_champ = api.request(RiotConstants.URL['champion_by_id_dynamic'].format(id=match['champion']))
        t_champ_name = ls.get_champion_name_by_id(t_champ['id'])
        if (not t_champ['freeToPlay']):
            owned_champs.append(t_champ_name)

    print ("===")
    print(owned_champs)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


if __name__ == "__main__":
    main()
