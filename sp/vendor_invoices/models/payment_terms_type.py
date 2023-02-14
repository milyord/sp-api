from enum import Enum


class PaymentTermsType(str, Enum):
    BASIC = "Basic"
    ENDOFMONTH = "EndOfMonth"
    FIXEDDATE = "FixedDate"
    PROXIMO = "Proximo"
    PAYMENTDUEUPONRECEIPTOFINVOICE = "PaymentDueUponReceiptOfInvoice"
    LETTEROFCREDIT = "LetterofCredit"

    def __str__(self) -> str:
        return str(self.value)
