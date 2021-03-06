from isitopen.tests import *

import isitopen.model as model

class TestModel(object):
    @classmethod
    def setup_class(self):
        self.enq_id, self.mess_id = Fixtures.create()

    @classmethod
    def teardown_class(self):
        Fixtures.remove()

    def test_fixtures(self):
        mess = model.Message.query.get(self.mess_id)
        enq = model.Enquiry.query.get(self.enq_id)

        assert enq.owner.email == Fixtures.user_email
        assert enq.summary == Fixtures.summary
        assert enq.extras['ckan-package'] == u'xyz'

        assert mess.enquiry == enq
        subj = mess.email['Subject']
        assert subj == u'testing email', subj
        assert mess.subject == subj, mess.subject
        assert mess.to == Fixtures.to, mess.to
        assert mess.sender == Fixtures.sender, mess.sender
        assert mess.status == model.Message.SENT_REREAD
        assert mess.email['Message-Id'] is not None, mess.mimetext
        assert mess.body == Fixtures.body, mess.body

