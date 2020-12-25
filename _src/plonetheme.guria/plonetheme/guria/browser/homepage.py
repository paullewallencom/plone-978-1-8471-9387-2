from zope.interface import implements
from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView

from Products.ATContentTypes.interface.topic import IATTopic

from plonetheme.guria.browser.interfaces import IHomepage
from plone.memoize.instance import memoize

DEFAULT_NUMBER_OF_ITEMS = 3

class Homepage(BrowserView):
    """Browser view for homepage logic"""
    
    implements(IHomepage)
    def __init__(self, context, request):
        super(Homepage, self).__init__(context, request)
        self.portal = getToolByName(self.context, "portal_url").getPortalObject()

    def _getSlotItems(self, slot_number, 
                      folder_name='homepage',
                      base_name="slot",
                      num_items=DEFAULT_NUMBER_OF_ITEMS):
        """Helper to be reused below. We're using sensible defaults for the optional args:
        folder_name: name of folder containing our Collections.  Can be a full path relative to the root.
        base_name: used with slot_number to construct the id of the Collection.
        """
        slot_obj = self.portal.restrictedTraverse("%s/%s%s" % (folder_name, base_name, slot_number), None)
        if slot_obj is None:
            return None
        if IATTopic.providedBy(slot_obj):
            return [brain.getObject() for brain in slot_obj.queryCatalog()[:num_items]]
        else:
            return [slot_obj,]
        
    def _getSlotImage(self, slot_number, 
                      folder_path='homepage/images',
                      base_name='slot',
                      base_ext='jpg'):
        """Helper method.  We're using sensible defaults for the optional args:
        folder_path: relative to root; path to the dir containing the fallback image
        base_name, base_ext: used with slot_number to determine fallback image id
        """
        method = getattr(self, "getSlot%sItems" % slot_number)
        objs = method()[:1]
        if objs:
            obj = objs[0]
            if hasattr(aq_inner(obj), 'getImage') and obj.getImage():
                return "%s/image" % obj.absolute_url()
        # if we get this far, we need to explore our fallback option
        fallback = self.portal.restrictedTraverse("%(folder)s/%(base)s%(number)s.%(ext)s" % {
                                                    "folder": folder_path,
                                                    "base": base_name,
                                                    "number": slot_number,
                                                    "ext": base_ext,
                                                    }, None)
        if fallback is not None:
            return fallback.absolute_url()
        else:
            return None
        
        
    def getSlot1Image(self):
        """Returns an absolute url for the image to appear in the first slot"""
        return self._getSlotImage(1)
    
    @memoize
    def getSlot1Items(self):
        """Return the first 3 content items for the first slot.  We're assuming that a
        Collection lives at the path /homepage/slot1; we'll return its first three items.
        """
        return self._getSlotItems(1)

    def getSlot2Image(self):
        """Returns an absolute url for the image to appear in the second slot"""
        return self._getSlotImage(2)

    @memoize
    def getSlot2Items(self):
        """Return the first 3 content items for the first slot.  We're assuming that a
        Collection lives at the path /homepage/slot2; we'll return its first three items.
        """
        return self._getSlotItems(2)

    def getSlot3Image(self):
        """Returns an absolute url for the image to appear in the third slot"""
        return self._getSlotImage(3)

    @memoize
    def getSlot3Items(self):
        """Return the first 3 content items for the first slot.  We're assuming that a
        Collection lives at the path /homepage/slot3; we'll return its first three items.
        """
        return self._getSlotItems(3)
