# -*- coding: utf-8 -*-

from trac.core import Component, implements
from trac.notification.api import IEmailDecorator
from trac.notification.mail import set_header

class ReferencesEmailDecorator(Component):
    implements(IEmailDecorator)

    def decorate_message(self, event, message, charset):
        domain = self.config.get('notification', 'smtp_from') or \
            self.config.get('notification', 'smtp_replyto')
        ticket = event.target

        mid = '<ticketref{}@{}>'.format(ticket.id, domain)
        if 'References' in message:
            mid += ' ' + message['References']
        set_header(message, 'References', mid, charset)
