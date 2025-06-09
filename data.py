
class Data:
    def __init__(self, rawData):
        self.__rawData = rawData
    
    def __parseData(self, rawData):
        
        parsedData = []
        for line in rawData:
            
