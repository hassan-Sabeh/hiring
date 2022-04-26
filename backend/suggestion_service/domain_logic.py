from suggestion_service.adapters_mock import *
from suggestion_service.models import Company

mail_adapter = MailerAdapterMock()
timer_adapter = TimerAdapterMock()
companies_adapter = CompaniesAdapterMock()
persistence_adapter = PersistenceAdapterMock()
growth_adapter = GrowthAdapterMock()

class SuggestionsDomain:
    def __init__(self):
        self.company = {}
    #private methods
    def __handle_new_suggestions_added(self):
        return growth_adapter.get_emails_sequence()

    def __set_timer(self, seconds, company_pk, email_type):
        timer_adapter.set_timer(seconds, company_pk, email_type)
    
    #public methods
    def handle_user_action_web_console(self, company_pk, suggested_company):  
        #changing the status of the suggested partner from user input.
        suggestion = persistence_adapter.find_suggestions(company_pk)
        suggestion[suggested_company] = False
        persistence_adapter.update_suggestions(company_pk, suggestion)
        

    def handle_timer_expired(self, company_pk, email_type):
        suggestions = persistence_adapter.find_suggestions(company_pk)
        #cleaning up suggestions list before sending
        suggestions_to_send = [company_name for company_name in suggestions if suggestions[company_name] is True]
        email_details = growth_adapter.get_email_details(company_pk, email_type, suggestions_to_send)
        mail_adapter.send_mail(email_details["recipients"],email_details["title"], email_details["content"])

    def handle_company_created(self, new_company): # -> new company {pk: int, country code: int, industry: str}
        self.company = Company(new_company["pk"], new_company["country"], new_company["industry"]) 
        #asking for suggestions through the adapter
        new_suggestions_list = companies_adapter.get_relevant_partnerships(self.company.country, self.company.industry)
        new_suggestions_dict = {}
        #converting list into dict
        for sugg in new_suggestions_list:
            new_suggestions_dict[sugg] = True
        persistence_adapter.add_suggestions(self.company.pk, new_suggestions_dict)
        #getting email sequence
        email_sequence = self.__handle_new_suggestions_added()
        #setting timer for the frist email:
        self.__set_timer(email_sequence[0][1], self.company.pk, email_sequence[0][0])

        

    # TODO: Add any private / public method you need to implement the business logic


        

