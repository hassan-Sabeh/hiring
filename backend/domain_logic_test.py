from suggestion_service.domain_logic import SuggestionsDomain


"""
Integration testing the domain logic from the public interfaces exposed to other services.

Below is a description of the expected behavior of each method.
"""


"""
handle_user_action_web_console
--------------------------------
Caller: action web console port
--------------------------------
1. getting suggestions from presistence adapter
2. feeding back the updated suggestion back to the adapter

"""

"""
handle_timer_expired
--------------------------------
Caller: timer port
--------------------------------
1. getting suggestions from presistence adapter
2. cleaning up suggestions before sending (removing the ones
that have been accepted or rejected)
3. Getting email details from growth adapter
4. transfering details to email adapter to send the mail.

"""


"""
handle_company_created
--------------------------------
Caller: companies adapter
--------------------------------
1. creating company object -> storing data on the model
2. Getting the relevant suggestions by country code and industry
from the compamies adapter.
3. Building the suggestions dict.
4. saving the suggestions via the persistence adapter
5. getting email sequence from growth adapter
6. setting first timer on the with the timer adapter
"""


"""
__handle_new_suggestions_added
--------------------------------
Caller: private
--------------------------------
1.get email sequence from growth adapter and return it
"""

"""
__set_timer
--------------------------------
Caller: private
--------------------------------
1.set the timer via the timer adapter.
"""

if __name__=="__main__":
    new_company = {
        "pk": 300,
        "country": 99,
        "industry": "tech"
    }
    domain = SuggestionsDomain()
    #testing public and private calls.
    print("########## handle_company_created ##############")
    domain.handle_company_created(new_company)

    print("########## handle_user_action_web_console ##############")
    domain.handle_user_action_web_console(new_company["pk"], "Microsoft")

    print("########## handle_timer_expired ##############")
    domain.handle_timer_expired(new_company["pk"], 1)