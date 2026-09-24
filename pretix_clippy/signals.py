import pytz
from django.conf import settings
from django.dispatch import receiver
from django.template.loader import get_template
from django.utils.timezone import now
from django.utils.translation import pgettext, gettext_lazy as _
from pretix.control.signals import html_page_start, nav_topbar


@receiver(html_page_start, dispatch_uid="clippy_html_page_start")
def html_page_start(sender, request=None, **kwargs):
    if not settings.DEBUG and not 'staging.pretix.eu' in settings.SITE_URL and now().astimezone(pytz.timezone('Europe/Berlin')).date().isoformat() != '2019-04-01':
        return ''
    template = get_template('pretix_clippy/control_body.html')
    return template.render({})


@receiver(nav_topbar, dispatch_uid="clippy_nav")
def control_support_nav(sender, request=None, **kwargs):
    if not settings.DEBUG and not 'staging.pretix.eu' in settings.SITE_URL and now().astimezone(pytz.timezone('Europe/Berlin')).date().isoformat() != '2019-04-01':
        return []
    return [
        {
            'label': _('Clippy'),
            'icon': 'paperclip',
            'url': ""
        }
    ]
