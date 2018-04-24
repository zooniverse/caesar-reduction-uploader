import pickle

class RunCache:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        self.load()
        
    def load(self):
        try:
            with open(self.filename, 'rb') as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            print("INFO: No prior run data")
            
    def save(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.data, f)
            
    def update(self, id, content):
        self.data[id] = content
       
    def is_changed(self, id, content):
        return not id in self.data or self.data[id] != content
