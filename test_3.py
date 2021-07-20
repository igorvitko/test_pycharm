import random
import os

print(random.randint(2, 8))
print(random.randint(10, 50))

main_path = os.path.dirname(os.path.abspath(__file__))
res_path = os.path.join(main_path, "resources")

print(res_path)