from enum import Enum


class PrepGuidance(str, Enum):
    CONSULTHELPDOCUMENTS = "ConsultHelpDocuments"
    NOADDITIONALPREPREQUIRED = "NoAdditionalPrepRequired"
    SEEPREPINSTRUCTIONSLIST = "SeePrepInstructionsList"

    def __str__(self) -> str:
        return str(self.value)
