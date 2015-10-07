# -*- coding: utf-8 -*-
from z3c.form import form
from z3c.form import button
from collective.transmogrifier.transmogrifier import Transmogrifier
# from Products.CMFCore.utils import getToolByName
from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView

from interaktiv.migrator.interfaces import IConfiguration


class ExportContentForm(form.Form):

    def description(self):
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IConfiguration, check=False)
        return "<b>Target URL</b>: %s" % settings.target_url

    @button.buttonAndHandler(u'Export Content')
    def handle_import_stuff(self, action):
        transmogrifier = Transmogrifier(self.context)
        transmogrifier(u'export_content')


class ExportReferencesForm(form.Form):

    @button.buttonAndHandler(u'Export References')
    def handle_import_stuff(self, action):
        transmogrifier = Transmogrifier(self.context)
        transmogrifier(u'export_references')


class ExportContentView(BrowserView):

    def __call__(self):
        transmogrifier = Transmogrifier(self.context)
        transmogrifier(u'export_content')
