from django.utils.translation import gettext_lazy


try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    name = 'pretix_clippy'
    verbose_name = 'Clippy for pretix'

    class PretixPluginMeta:
        name = gettext_lazy('Clippy for pretix')
        author = 'Martin Gross'
        description = gettext_lazy('Plugin to add Clippy to pretix - The one plugin you didn\'t knew you even needed it. Until now.')
        visible = False
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA
