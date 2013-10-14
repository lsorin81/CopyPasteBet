from django.test import TestCase, RequestFactory
from .confirm_page import confirm


# Constants by convention
ARG_BET = "Bet"


class ConfirmPage(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_http_response_bet(self):
        request = self.factory.post('/cpbet/',
                                    data={ARG_BET: "dsfsaf", })
        response = confirm(request)
        self.assertContains(response, "7:00")