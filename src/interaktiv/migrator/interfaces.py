# -*- coding: UTF-8 -*-
from zope.interface import Interface
from zope import schema


class IExportUtility(Interface):
    """ utility to provide methods for Content Export
    """


class IImportUtility(Interface):
    """ utility to provide methods for Content Import
    """


class IConfiguration(Interface):
    """"""

    target_url = schema.TextLine(
        title=u"target url",
        required=False,
        description=u"",
    )

    api_key = schema.TextLine(
        title=u"api key",
        required=True,
        description=u"",
    )

    type_mapping = schema.List(
        title=u"type mapping",
        required=False,
        description=u"",
        value_type=schema.TextLine(),
        default=[
            "Topic|Collection",
            "ATImage|Image",
            "ATFile|File",
            "Large Plone Folder|Folder",
            "PloneGlossary|Glossary",
            "PloneGlossaryDefinition|GlossaryDefinition",
        ]
    )

    field_mapping = schema.List(
        title=u"field mapping",
        required=False,
        description=u"",
        value_type=schema.TextLine(),
        default=[
            "leadImage|image",
            "leadImage_caption|image_caption",
            "startDate|start_date",
            "endDate|end_date",
            "eventUrl|event_url",
            "contactName|contact_name",
            "contactEmail|contact_email",
            "contactPhone|contact_phone",
        ]
    )

    view_mapping = schema.List(
        title=u"view mapping",
        required=False,
        description=u"",
        value_type=schema.TextLine(),
        default=[
            "folder_summary_view|summary_view",
            "folder_tabular_view|tabular_view",
            "atct_album_view|album_view",
        ]
    )
