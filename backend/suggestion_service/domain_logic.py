from suggestion_service.adapters import *
from suggestion_service.models import Company

class SuggestionsDomain:
    mail = MailerAdapterMock()

    def handle_user_action_web_console(self, company_key: int, suggested_company: str):  
        #changing the status of the suggested partner from user input.
        suggestions_on_db = PersistenceAdapter() 
        suggestion = suggestions_on_db.find_suggestions(company_key)
        suggestion[suggested_company] = False
        suggestions_on_db.update_suggestions(company_key, suggestion)
        return (company_key, suggestion)

    def handle_timer_expired(self, company_key, email_type):
        # suggestions_find = PersistenceAdapter()
        # suggestions = suggestions_find.find_suggestions(company_key)
        # suggestions_to_send = [company_name for company_name in suggestions if suggestions[company_name] is True]
        # growth_adapter = GrowthAdapter()
        # email_details = growth_adapter.get_email_details(company_key, email_type, suggestions_to_send)
        # mail = MailerAdapter()
        # mail.send_mail(email_details["recipients"],email_details["title"], email_details["content"])
        # return (email_details["recipients"],email_details["title"], email_details["content"])
        print(company_key, email_type)
        self.mail.send_mail("hassan", 12, "dsfdfdf")

    def send_email(self, recipients, title, content):
        self.mail.send_mail(recipients, title, content)

    def handle_company_created(self, new_company: dict):
        company = Company(new_company["pk"], new_company["country"], new_company["industry"]) 
        #asking for suggestions through the adapter
        company_adapter = CompaniesAdapter()
        new_suggestions_list = company_adapter.get_relevant_partnerships(company.country, company.industry)
        new_suggestions_dict = {}
        #converting list into dict
        for sugg in new_suggestions_list:
            new_suggestions_dict[sugg] = True
        PersistenceAdapter.add_suggestions(company.pk, new_suggestions_dict)
        return (company.pk, new_suggestions_dict)

    def handle_new_suggestions_added(self):
        growth_adapter = GrowthAdapter() 
        return growth_adapter.get_emails_sequence()

    def set_timer(self, seconds, company_pk, email_type):
        timer_adapter = TimerAdapter()
        timer_adapter.set_timer(seconds, company_pk, email_type)
        return seconds

    # TODO: Add any private / public method you need to implement the business logic


        

