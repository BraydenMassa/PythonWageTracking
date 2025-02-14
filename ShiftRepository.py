from bson import ObjectId
from pymongo import MongoClient
from Shift import Shift


# Handles CRUD operations on Shifts collection
class ShiftRepository:

    def __init__(self, connection_string):
        client = MongoClient(connection_string)
        db = client["WageTracking"]
        self.collection = db["Shifts"]

    # Returns a list of all Shifts in the collection
    def get_all_shifts(self):
        all_shifts = self.collection.find()
        return [Shift(**shift) for shift in all_shifts]

    # Returns a shift based on provided id parameter
    def get_shift_by_id(self, id):
        try:
            shift = self.collection.find_one({"_id": ObjectId(id)})
            return shift
        except Exception as e:
            print(f"Error fetching shift: {e}")
            return None

    # Attempts to add a shift to the collection
    def add_shift(self, shift):
        try:
            shift_data = shift.__dict__.copy()
            shift_data.pop("_id", None)
            result = self.collection.insert_one(shift_data)
            shift._id = result.inserted_id
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error adding shift: {e}")
            return None

    # Attempts to delete shift from collection based on id
    def delete_shift(self, id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting shift: {e}")
            return False

