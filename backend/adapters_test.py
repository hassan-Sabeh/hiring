"""
Unittesting the adapters Mock before integration in the domain logic.
"""
import unittest
from suggestion_service.adapters_mock import (CompaniesAdapterMock, GrowthAdapterMock,
MailerAdapterMock, TimerAdapterMock,
PersistenceAdapterMock)







TARGET_COMPANY_PK = 111
COUNTRY_CODE = 90
mail_adapter = MailerAdapterMock()
timer_adapter = TimerAdapterMock()
companies_adapter = CompaniesAdapterMock()
persistence_adapter = PersistenceAdapterMock()
growth_adapter = GrowthAdapterMock()

class DomainUnitTest(unittest.TestCase):
    """
    unit testing adapters outgoing methods
    """
    def test_send_email(self):
        self.assertEqual(mail_adapter.send_mail(("john", "Doe"),
            "title",
            "content"), None)

    def test_timer_set(self):
        self.assertEqual(timer_adapter.set_timer(3600, TARGET_COMPANY_PK, 1), None)

    def test_get_companies(self):
        self.assertTrue(type(companies_adapter.get_relevant_partnerships(
            COUNTRY_CODE,
            "tech",
        )) is list)

    def test_get_suggestions(self):
        self.assertTrue(type(persistence_adapter.find_suggestions(
            TARGET_COMPANY_PK)) is dict)

    def test_add_suggestion(self):
        self.assertEqual(persistence_adapter.add_suggestions(
            TARGET_COMPANY_PK,
            {"Microsoft":False}
            ), None)
    def test_update_suggestion(self):
        self.assertEqual(persistence_adapter.update_suggestions(
            TARGET_COMPANY_PK,
            {"google":True}
        ), None)

    def test_get_emails_sequence(self):
        self.assertTrue(type(growth_adapter.get_emails_sequence()) is list)

    def test_get_email_details(self):
        self.assertTrue(type(growth_adapter.get_email_details(
            TARGET_COMPANY_PK,
            1, # example email type 1 as an int
            ["google", "apple", "tesla"] # example list of str as suggestion list
        )) is dict)
if __name__== "__main__":
    unittest.main()
