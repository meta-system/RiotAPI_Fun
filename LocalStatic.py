class LocalStatic(object):

    def __init__(self, list={}):
        self.__champion_list = list
        print(self.__champion_list)

    def get_champion_by_id(self, id):
        print ("in by_id")
        return self.__champion_list["data"][id]

    def get_champion_name_by_id(self, id):
        print ("in name_by_id")

        return self.get_champion_by_id(id)['name']
