from isitopen.tests import *

class TestAdminController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='admin', action='index'))
        assert 'Enquiry' in response
        assert 'Message' in response

