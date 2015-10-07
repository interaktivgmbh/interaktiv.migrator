
from plone.z3cform import layout
from plone.app.registry.browser.controlpanel import (
    RegistryEditForm,
    ControlPanelFormWrapper
)

from interaktiv.migrator.interfaces import IConfiguration


class ConfigurationForm(RegistryEditForm):

    schema = IConfiguration
    label = u"Migrator Configuration"


ConfigurationView = layout.wrap_form(
    ConfigurationForm,
    ControlPanelFormWrapper
)
