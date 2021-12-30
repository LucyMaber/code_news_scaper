class Cache:
    def __init__(self) -> None:
        self.data = {}
    def set(self,name,obList):
        if name not in self.data.keys():
            self.data[name] = {}
            self.data[name]["list"] = obList
        
    def loopOver(self,name,obList):
        if name not in self.data.keys():
            self.data[name] = {}
            self.data[name]["list"] = obList
        while len(self.data[name]["list"]) != 0:
            yield self.data[name]["list"].pop()


cache = Cache()
