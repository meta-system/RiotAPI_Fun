class LocalStatic(object):

    def __init__(self, new_list={}):
        self.champion_list = new_list
        #print(self.champion_list)

    def get_champion_by_id(self, id):
        return self.champion_list[str(id)]

    def get_champion_name_by_id(self, id):
        return self.get_champion_by_id(id)['name']
