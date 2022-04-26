from suggestion_service.adapters import *
from typing import Set, List, Dict


"""
Adapters mock are simulations of real adapters, below classes have inherited from
the abstract classes that are in the ./adapters.py (abstract methods) -> (concrete methods)
"""



class MailerAdapterMock(MailerAdapter):
    def send_mail(self, recipients: Set[str], title: str, content: str) -> None:
        print(f"send_mail adapter: recipients: {recipients}, title: {title}, content:{content}")
        pass

class TimerAdapterMock(TimerAdapter):
    def set_timer(self, seconds_before_email_sending: int, target_company_key: int, email_type: int) -> None:
        print(f"set_timer adapter: seconds before email: {seconds_before_email_sending}, target compny: {target_company_key}, email type:{email_type}")
        pass

class CompaniesAdapterMock(CompaniesAdapter):
    def get_relevant_partnerships(self, country_code: int, industry: str) -> List[str]:
        print(f"companies adapter: country code: {country_code},  industry: {industry}")
        return ["google", "facebook", "apple"]

class PersistenceAdapterMock(PersistenceAdapter):
    def find_suggestions(self, target_company_key: int) -> Dict[str, bool]:
        print(f"get suggestion: target company: {target_company_key}")
        return {"Yamaha":True, "pepsi": False, "Microsoft":True }
    
    def add_suggestions(self, target_company_key: int, suggestions: Dict[(str, str)]) -> None:
        print(f"Add suggestion: target company: {target_company_key} suggestions {suggestions}")
        pass
    
    def update_suggestions(self, target_company_key: int, suggested_company: Dict[(str, str)]) -> None:
        print(f"Add suggestion: target company: {target_company_key} suggested cmpn {suggested_company}")
        pass

class GrowthAdapterMock(GrowthAdapter):
    def get_emails_sequence(self: "GrowthAdapter") -> List[tuple]:
        print("Growth adapter: Getting email sequence")
        return [(1, 3600),(2, 86400),(4, 604800)]
    
    def get_email_details(self: "GrowthAdapter", target_company_key: int, email_type: int, suggested_partners: List[str]) -> Dict:
        print(f"Growth adapter: Add suggestion: target company: {target_company_key} email tyoe:{email_type} suggested partners {suggested_partners}")
        return {"recipients":["john", "Monica", "Amelie"], 
        "title":"suggestions!", 
        "content":"Hello there, this is the list of etc..."}