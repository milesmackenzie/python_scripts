# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    # Add the special method here

    def column(self, label):
        if label not in self.header:
            return None

        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column


    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count

    def __str__(self):
        return str(self.data[0:10])

nfl_dataset = Dataset(nfl_data)
print (nfl_dataset)

#Challenge: Modules, Classes, Error Handling, and List Comprehensions

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0

    def get_year(self):
        return(self.year)


missing_year = Suspension(nfl_suspensions[22])

twenty_third_year = missing_year.get_year()

print(twenty_third_year)
