from database import db

class Note():
    def __init__(self, note):
        self.collection = db["notes"]
        self.note = note
        
    def find_by_id(self, id):
        try:
            note = self.collection.find_one({"_id": id})
            return True
        except Exception as e:
            return e.message
        
    def create(self):
        try:
            self.collection.insert_one({"note": self.note})
            return True
        except Exception as e:
            return e.message
        
    def update_one(self, id, note):
        try:
            self.collection.find_one_and_update({"_id": id, "note": note})
            return True
        except Exception as e:
            return e.message
        
    def remove_one(self, id):
        try:
            self.collection.delete_one({"_id": id})    
            return True
        except Exception as e:
            return e.message