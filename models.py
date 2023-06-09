from pydantic import BaseModel

class Client(BaseModel):
    BALANCE:float
    BALANCE_FREQUENCY:float
    PURCHASES:float
    ONEOFF_PURCHASES:float
    INSTALLMENTS_PURCHASES:float
    CASH_ADVANCE:float
    PURCHASES_FREQUENCY:float
    ONEOFF_PURCHASES_FREQUENCY:float
    PURCHASES_INSTALLMENTS_FREQUENCY:float
    CASH_ADVANCE_FREQUENCY:float
    CASH_ADVANCE_TRX:int
    PURCHASES_TRX:int
    CREDIT_LIMIT:float
    PAYMENTS:float
    MINIMUM_PAYMENTS:float
    PRC_FULL_PAYMENT:float
    TENURE:int