"""
this file is example of generation uuid
add string in branch feature_4
add 2 string in branch feature_4
add 3 string in branch feature_4

"""

from uuid import uuid4

for _ in range(5):
    dto = {
        "_id": str(uuid4()),
        "_payroll": str(uuid4())
    }
    print(dto)

