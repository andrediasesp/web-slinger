import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import promotions as PromotionModel

class Promotions(MongoengineObjectType):
    class Meta:
        model = PromotionModel

class Query(graphene.ObjectType):
    proms = graphene.List(Promotions)

    def resolve_proms(self, info):
    	return list(PromotionModel.objects.all())

schema = graphene.Schema(query=Query)
