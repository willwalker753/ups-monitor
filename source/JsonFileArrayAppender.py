import os
import json

class JsonFileArrayAppender:
    def __init__(self, filePath, arrayKey):
        self.filePath = filePath
        self.arrayKey = arrayKey

    '''
    @param  (any)  value  

    @return  self
    '''
    def append(self, value):
        try:
            # try to open the JSON file
            with open(self.filePath, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            # if the file does not exist, create an empty dict
            data = {}

        # ensure that the arrayKey exists in the data before appending the value
        data.setdefault(self.arrayKey, []).append(value)

        # write the updated data back to the JSON file
        with open(self.filePath, 'w') as file:
            json.dump(data, file, indent=2)
        
        return self
