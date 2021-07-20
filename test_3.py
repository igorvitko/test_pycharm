from uuid import uuid4

for _ in range(5):
    dto = {
        "_id": str(uuid4()),
        "_payroll": str(uuid4())
    }
    print(dto)

