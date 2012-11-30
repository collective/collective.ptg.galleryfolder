from zope import schema
from zope.interface import Interface 

from zope.app.container.constraints import contains, containers

from collective.plonetruegallery import MessageFactory as _


class IGalleryfolder(Interface):
    """Galleryfolder content type"""
    

