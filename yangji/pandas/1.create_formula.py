import json
import pandas as pd

# data = json.loads([{"index":1,"slot":"1","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":2,"slot":"17","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":3,"slot":"20","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":4,"slot":"37","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":5,"slot":"43","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":6,"slot":"55","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":7,"slot":"66","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":8,"slot":"77","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":9,"slot":"85","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":10,"slot":"93","standard_time":1,"max_time":1,"load_module":"","load_value":""}])
data = json.loads('[{"index":1,"slot":"1","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":2,"slot":"17","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":3,"slot":"20","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":4,"slot":"37","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":5,"slot":"43","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":6,"slot":"55","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":7,"slot":"66","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":8,"slot":"77","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":9,"slot":"85","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":10,"slot":"93","standard_time":1,"max_time":1,"load_module":"","load_value":""}]')

df = pd.DataFrame(data)
print(df)






