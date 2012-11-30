"""Definition of the Galleryfolder content type
"""
from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from collective.ptg.galleryfolder.interfaces import IGalleryfolder
from collective.ptg.galleryfolder.config import PROJECTNAME


class Galleryfolder(folder.ATFolder):
    """Galleryfolder is a copy of a normal folder"""


#registerATCT(Galleryfolder, PROJECTNAME)    
atapi.registerType(Galleryfolder, PROJECTNAME)
