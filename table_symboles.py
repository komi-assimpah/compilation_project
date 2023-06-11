class TableSymboles:
    types = {
        type(1): "entier",
        type(True): "booleen"
    }

    def __init__(self):
        self.symboles = {}
        
    def exist(self, nom, type_args):
        if nom in self.symboles:
            if len(type_args) != len(self.symboles[nom]['args']):
                return False

            return [TableSymboles.types[i] for i in type_args] == self.symboles[nom]['args']
        else:
            return False