import mongoengine

class promotions(mongoengine.Document):
    """Promotions Collection from the MongoDB instance"""
    insert_date = mongoengine.DateTimeField()
    game = mongoengine.StringField()
    price = mongoengine.DecimalField()
    currency = mongoengine.StringField()
