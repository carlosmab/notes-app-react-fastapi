from database import db

class Note():
    def __init__(self, note, test):
        if test:
            self.collection = db["test_notes"]
        else:
            self.collection = db["notes"]
        
        self.id = None
        self.note = note
        
    def find_by_id(self, id):
        try:
            note = self.collection.find_one({"_id": id})
            return True
        except Exception as e:
            return e
        
    def create(self):
        try:
            result = self.collection.insert_one({"note": self.note})
            self._id = result.inserted_id
            return True
        except Exception as e:
            return e
        
    def update(self, note):
        if self._id != None:
            try:
                self.collection.update_one(
                    {"_id": self._id}, 
                    { "$set": {"note": note} }
                )
                return True
            
            except Exception as e:
                return e
        return False
        
    def remove(self):
        if self._id != None:
            try:
                self.collection.delete_one({"_id": self._id})
                self._id = None    
                return True
            except Exception as e:
                return e
        return False