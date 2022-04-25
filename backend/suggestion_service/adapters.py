from typing import Set, List, Dict


#outgoing adapters (orange arrows)

class MailerAdapter:
    """
    For Outbound Adapters you need to define classes/methods/interfaces and specify their signature
    but the body should remain empty (cf following example)
    """
    def send_mail(self: "MailerAdapter", recipients: Set[str], title: str, content: str) -> None:
        raise NotImplemented
    

class TimerAdapter:
    def setTimer(self: "TimerAdapter", seconds_before_email_sending: int) -> None:
        raise NotImplemented

class CompaniesAdapter:
    def get_relevant_partnerships(self: "CompaniesAdapter", country_code: int, industry: str) -> List[str]:
        raise NotImplemented

class PersistenceAdapter:
    #find a company from a key, returns the object from db
    def find_suggestions(self: "PersistenceAdapter", target_company_key: int) -> Dict[str, str]:
        raise NotImplemented
    # output is a list of suggestions where every suggested company is represented as a tuple (name, accepted/declined)
    def add_suggestions(self: "PersistenceAdapter", target_company_key: int, suggestions: Dict[(str, str)]) -> None:
        raise NotImplemented
    def update_suggestions(self: "PersistenceAdapter", target_company_key: int, suggested_company: Dict[(str, str)]) -> None:
        #suggested_company is a tuple containing the name of the company and the status (accepted or decline as from the web app adapter)
        raise NotImplemented

class GrowthAdapter:
    def get_emails_sequence(self: "GrowthAdapter", target_company_key: int) -> List[tuple]:
        raise NotImplemented
    def get_email_details(self: "GrowthAdapter", target_company_key: int, email_type: int, suggested_partners: List[str]) -> None:
        raise NotImplemented