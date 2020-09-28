from titanic.entitiy import Entity

class Service:
    def __init__(self):
        self.entitiy = Entity()  # Autowired Entitiy entity

    def new_model(self, payload):
        pass

    @staticmethod
    def create_train(this):
        pass

    @staticmethod
    def create_label(this):
        pass
    
    @staticmethod
    def drop_feature(this):
        pass