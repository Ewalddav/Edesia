import pymongo
from bson.objectid import ObjectId

class MongoHelper(object):

    @staticmethod
    def insertRecipes(recipes):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client.edesia
        recipeIds = db.dirty_recipes.insert_many(recipes).inserted_ids
        client.close()
        return recipeIds

    @staticmethod
    def getRecipeByUrl(url):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client.edesia
        recipe = db.dirty_recipes.find({"url": url})
        client.close()
        return recipe

    @staticmethod
    def getRecipeById(recipe_id):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client.edesia
        recipe = db.dirty_recipes.find_one({"_id": ObjectId(recipe_id)})
        client.close()
        return recipe

