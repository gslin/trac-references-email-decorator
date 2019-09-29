# -*- coding: utf-8 -*-

from trac.core import Component, implements
from trac.notification.api import IEmailDecorator
from trac.notification.mail import set_header

class ReferencesEmailDecorator(Component):
    implements(IEmailDecorator)

    def decorate_message(self, event, message, charset):
        if not 'References' in message:
            set_header(message, 'References', message['Message-ID'], charset)
