def load_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    
def save_file(filename: str, lines: list[str]) -> bool:
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        return True
    except Exception as e:
        print(f"Error: Could not save to file '{filename}'. {str(e)}")
        return False
    
def get_leaf_subclasses(cls):
    leaves = []
    for subclass in cls.__subclasses__():
        if not subclass.__subclasses__():
            leaves.append(subclass)
        else:
            leaves.extend(get_leaf_subclasses(subclass))
    return leaves

def is_leaf_class(cls):
    return not cls.__subclasses__()
