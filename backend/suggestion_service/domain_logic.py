from adapters import *

class SuggestionsDomain:
    def handle_user_action_web_console(self, company_key, suggested_company):  
        #changing the status of the suggested partner from user input.
        suggestion = PersistenceAdapter.find_suggestions(company_key)
        #delete directly assuming any change (accept or decline) should remove this suggestions.
        del suggestion[suggested_company]
        PersistenceAdapter.update_suggestions(company_key, suggestion)
        pass

    def handle_timer_expired(self, company_key, email_type):
        #take the latest email
        pass

    def handle_company_created(): 
        # TODO: Body to be specified
        pass

    # TODO: Add any private / public method you need to implement the business logic
        

