from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from collective.transmogrifier.transmogrifier import configuration_registry

from plone.testing import z2

from zope.configuration import xmlconfig


class InteraktivMigratorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import interaktiv.migrator
        xmlconfig.file(
            'configure.zcml',
            interaktiv.migrator,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'interaktiv.migrator:default')

    def tearDownPloneSite(self, portal):
        z2.uninstallProduct(portal, 'interaktiv.migrator')
        configuration_registry.clear()


class InteraktivMigratorFunctionalLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import interaktiv.migrator
        xmlconfig.file(
            'configure.zcml',
            interaktiv.migrator,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'interaktiv.migrator:default')

    def tearDownPloneSite(self, portal):
        z2.uninstallProduct(portal, 'interaktiv.migrator')
        configuration_registry.clear()


INTERAKTIV_MIGRATOR_FIXTURE = InteraktivMigratorLayer()
INTERAKTIV_MIGRATOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(INTERAKTIV_MIGRATOR_FIXTURE,),
    name="InteraktivMigratorLayer:Integration"
)

INTERAKTIV_MIGRATOR_FUNCTIONAL_FIXTURE = InteraktivMigratorFunctionalLayer()
INTERAKTIV_MIGRATOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(INTERAKTIV_MIGRATOR_FUNCTIONAL_FIXTURE,),
    name="InteraktivMigratorLayer:Functional"
)
