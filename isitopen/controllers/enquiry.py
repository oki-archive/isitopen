from ckan.lib.base import *

import ckan.lib.gmail

class EnquiryController(BaseController):

    def index(self):
        return self.list()
    
    def choose(self):
        return render('enquiry/choose.html')

    def create(self, template=''):
        c.email_template = template_2
        if not ('preview' in request.params or 'commit' in request.params):
            return render('enquiry/create.html')

        c.to = request.params['to']
        c.subject = request.params['subject']
        c.body = request.params['body']
        if 'preview' in request.params:
            return render('enquiry/preview')
        if 'commit' in request.params:
            enq = model.Enquiry(
                    to=c.to,
                    subject=c.subject,
                    body=c.body
                    )
            model.Session.commit()
            # need to get back the gmail id
            gmail = ckan.lib.gmail.Gmail.default()
            msg = ckan.lib.gmail.create_msg(c.body,
                to=c.to,
                subject=c.subject
                )
            gmail.send(msg)
            c.enquiry = enq
            return render('enquiry/sent.html')

    def list(self):
        c.enquiries = model.Enquiry.query.all()
        return render('enquiry/list.html')

    def view(self, id=''):
        enq = model.Enquiry.query.get(id)
        if enq is None:
            abort(404)
        c.enquiry = enq
        return render('enquiry/view.html')

follow_up_email = '''It might also be good to apply a specific 'open data' licence --
you can find examples of such licenses at: ...
'''

template_2 = \
'''Dear Editor,

I am a [[INSERT INFORMATION INCLUDING DISCIPLINE]].

I am writing on behalf of the Open Scientific Data Working Group of the Open Knowledge Foundation. We are seeking clarification of the 'openness' of the scientific data associated with your publications.

We weren't able to find an explicit statement of this fact such as a reference to an open knowledge license[3] so we're writing to find out what the exact situation is, specifically to ask you whether the material can be made available under an open license of some kind[3].

Regards,

[[INSERT NAME HERE]]

[1]: [[INSERT LINK HERE]]
[2]: http://www.opendefinition.org/1.0/
[3]: http://www.opendefinition.org/licenses/
'''
