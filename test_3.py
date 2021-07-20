import json
import random
import os

print(random.randint(2, 8))
print(random.randint(10, 50))

main_path = os.path.dirname(os.path.abspath(__file__))
res_path = os.path.join(main_path, "resources")

with open(os.path.join(res_path, "data.json")) as f:
    data_resource = json.loads(f.read()).get("place")
    print(data_resource)
# print(res_path)