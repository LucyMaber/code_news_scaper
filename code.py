import os
import importlib.util

data = []

for root, dirs, files in os.walk("./scrapers/news/UK"):
    for file_A in files:
        try:
            spec_a = importlib.util.spec_from_file_location("module.name", "./scrapers/news/UK/"+file_A)
            foo_a = importlib.util.module_from_spec(spec_a)
            spec_a.loader.exec_module(foo_a)
            for file_B in files:
                try:
                    spec_b = importlib.util.spec_from_file_location("module.name", "./scrapers/news/UK/"+file_B)
                    foo_b = importlib.util.module_from_spec(spec_b)
                    spec_b.loader.exec_module(foo_b)
                except:
                    pass
        except:
            data.append({"type":"unknow Error","file":file_A})
print(data)
            
