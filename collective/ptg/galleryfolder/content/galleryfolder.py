"""Definition of the Galleryfolder content type
"""
from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from collective.ptg.galleryfolder.interfaces import IGalleryfolder
from collective.ptg.galleryfolder.config import PROJECTNAME
from Products.ATContentTypes.content import schemata


from zope.interface import implements

GalleryfolderSchema = folder.ATFolderSchema.copy() 

GalleryfolderSchema['title'].storage = atapi.AnnotationStorage()
GalleryfolderSchema['description'].storage = atapi.AnnotationStorage()


schemata.finalizeATCTSchema(GalleryfolderSchema, moveDiscussion=False)



class Galleryfolder(folder.ATFolder):
    """Galleryfolder is a copy of a normal folder"""
    implements(IGalleryfolder)

    meta_type = "Galleryfolder"
    schema = GalleryfolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(Galleryfolder, PROJECTNAME)
