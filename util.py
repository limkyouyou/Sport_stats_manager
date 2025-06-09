
class Util:
    def __init__(self):
        self.__file_data = None

    def loadFile(filename):
        try:
            with open(filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return None
        
    