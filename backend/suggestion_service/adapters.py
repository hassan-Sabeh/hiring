from typing import Set, List, Dict
from abc import ABC, abstractmethod

#outgoing adapters (orange arrows)

class MailerAdapter(ABC):
    def __init__(self):
        super().__init__()
    """
    For Outbound Adapters you need to define classes/methods/interfaces and specify their signature
    but the body should remain empty (cf following example)
    """
    @abstractmethod
    def send_mail(self: "MailerAdapter", recipients: Set[str], title: str, content: str) -> None:
        raise NotImplementedError
    

class TimerAdapter(ABC):
    @abstractmethod
    def set_timer(self: "TimerAdapter", seconds_before_email_sending: int, target_company_key: int, email_type: int) -> None:
        raise NotImplementedError

class CompaniesAdapter(ABC):
    @abstractmethod
    def get_relevant_partnerships(self: "CompaniesAdapter", country_code: int, industry: str) -> List[str]:
        raise NotImplementedError

class PersistenceAdapter(ABC):
    #find a company from a key, returns the object from db
    @abstractmethod
    def find_suggestions(self: "PersistenceAdapter", target_company_key: int) -> Dict[str, bool]:
        raise NotImplementedError
    # output is a list of suggestions where every suggested company is represented as a tuple (name, accepted/declined)
    @abstractmethod
    def add_suggestions(self: "PersistenceAdapter", target_company_key: int, suggestions: Dict[(str, str)]) -> None:
        raise NotImplementedError
    @abstractmethod
    def update_suggestions(self: "PersistenceAdapter", target_company_key: int, suggested_company: Dict[(str, str)]) -> None:
        #suggested_company is a tuple containing the name of the company and the status (accepted or decline as from the web app adapter)
        raise NotImplementedError

class GrowthAdapter(ABC):
    @abstractmethod
    def get_emails_sequence(self: "GrowthAdapter") -> List[tuple]:
        raise NotImplementedError
    #adapter output is dict with title, recipient and content with values
    @abstractmethod
    def get_email_details(self: "GrowthAdapter", target_company_key: int, email_type: int, suggested_partners: List[str]) -> Dict:
        raise NotImplementedError