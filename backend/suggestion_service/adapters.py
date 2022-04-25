from suggestion_service.ports import *
from typing import Set, List, Dict

class MailerAdapterMock(MailerAdapter):
    def send_mail(self, recipients: Set[str], title: str, content: str) -> None:
        pass

class TimerAdapterMock(TimerAdapter):
    def set_timer(self, seconds_before_email_sending: int, target_company_key: int, email_type: int) -> None:
        pass

class CompaniesAdapterMock(CompaniesAdapter):
    def get_relevant_partnerships(self, country_code: int, industry: str) -> List[str]:
        return ["google", "facebook", "apple"]

class PersistenceAdapterMock(PersistenceAdapter):
    def find_suggestions(self, target_company_key: int) -> Dict[str, bool]:
        return {"Yamaha":False, "pepsi": False, "Microsoft":False }
    def add_suggestions(self, target_company_key: int, suggestions: Dict[(str, str)]) -> None:
        pass
    def update_suggestions(self, target_company_key: int, suggested_company: Dict[(str, str)]) -> None:
        pass

class GrowthAdapterMock(GrowthAdapter):
    def get_emails_sequence(self: "GrowthAdapter") -> List[tuple]:
        return [(1, 3600),(2, 86400),(4, 604800)]
    def get_email_details(self: "GrowthAdapter", target_company_key: int, email_type: int, suggested_partners: List[str]) -> Dict:
        return {"recipients":["john", "Monica", "Amelie"], 
        "title":"suggestions!", 
        "content":"Hello there, this is the list of etc..."}