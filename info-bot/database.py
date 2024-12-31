import json

class Database():
    def __init__(self, database):
        self.file = database
        with open(database, "r") as f:
            self.data = json.load(f)

    def edit(self, category, value):
        if category in self.data:
            self.data[category] += f", {value}"
        else:
            self.data[category] = value

        with open(self.file, "w") as f:
            json.dump(self.data, f)

    def open(self):
        with open(self.file, "r") as f:
            self.data = json.load(f)
        return self.data


class System():
    def __init__(self, database):
        self.database = Database(database)

    def edit(self, category, value):
        self.database.edit(category, value)

    def open(self):
        database = self.database.open()
        return database
