## Question
![](/assets/q_idempotency.png)
## Response Section

**Idempotency** คือ คุณสมบัติที่รองรับการเรียกใช้งานโดย parameter เดิมซ้ำอีกครั้งผลลัพท์ที่ได้จะเหมือนครั้งแรก ซึ่งคุณสมบัตินี้จะช่วยให้เราจัดการกับ request ที่มีการส่งซ้ำเข้ามาได้อย่างถูกต้อง เช่น การเรียก GET ข้อมูลเข้าด้วย parameter เดิมก็จะได้ ผลลัพท์ออกมาเหมือนเดิม

### ตัวอย่างการ Implement ด้วย Python FastAPI

ด้วยความที่ Post จะต้องมีการเช็ค UUID ใน Header ของ Request เพื่อที่จะรู้ว่า Request นี้ถูกส่งมารึยังหรือว่ามีคนแอบใช้ Request นี้เพื่อเจาะระบบจะได้ตอบสนองได้โดยไม่เปิดช่องโหว่อะไร

```python
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

# dummy DB
idempotency_store = {} 
payments_db = []

class PaymentRequest(BaseModel):
    user_id: int
    amount: float

@app.post("/payments", status_code=201)
def create_payment(
    payload: PaymentRequest,
    idempotency_key: str = Header(..., alias="Idempotency-Key")
):
    # Idempotency-Key validation
    if idempotency_key in idempotency_store:
        cached = idempotency_store[idempotency_key]
        
        # response for duplicate Idempotency-Key and we can ban this user or blacklist IP in future
        if cached["request_payload"] != payload.model_dump():
            raise HTTPException(
                status_code=422,
                detail="Idempotency-Key already used with different request payload"
            )
        
        # return prev response for same body
        return cached["response"]

    # Idempotency-Key correct
    transaction_id = str(uuid.uuid4())
    payment_record = {
        "transaction_id": transaction_id,
        "user_id": payload.user_id,
        "amount": payload.amount,
        "status": "SUCCESS"
    }
    payments_db.append(payment_record)

    idempotency_store[idempotency_key] = {
        "request_payload": payload.model_dump(),
        "response": payment_record
    }

    return payment_record
```