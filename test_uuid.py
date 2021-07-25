from uuid import uuid4

"""
this file is example of generation uuid

"""


for _ in range(5):
    dto = {
        "_id": str(uuid4()),
        "_payroll": str(uuid4())
    }
    print(dto)

