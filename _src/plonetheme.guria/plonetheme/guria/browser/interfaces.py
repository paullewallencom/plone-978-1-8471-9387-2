from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IHomepage(Interface):
    """Browser view for homepage logic"""

    def getSlot1Image():
        """Returns an absolute url for the image to appear in the first slot.
            
          Use either the image associated with the first item returned by getSlot1Items or
          the fallback, which lives in homepage/images/slot1.jpg
          
          If that doesn't exist either, return None.
        """

    def getSlot1Items():
        """Return the first 3 content items for the first slot.  We're assuming that a
        Collection lives at the path /homepage/slot1; we'll return its first three items.
        """

    def getSlot2Image():
        """Returns an absolute url for the image to appear in the second slot.
            
          Use either the image associated with the first item returned by getSlot1Items or
          the fallback, which lives in homepage/images/slot2.jpg
          
          If that doesn't exist either, return None.
        """

    def getSlot2Items():
        """Return the first 3 content items for the first slot.  We're assuming that a
        Collection lives at the path /homepage/slot2; we'll return its first three items.
        """

    def getSlot3Image():
        """Returns an absolute url for the image to appear in the third slot.
            
          Use either the image associated with the first item returned by getSlot1Items or
          the fallback, which lives in homepage/images/slot3.jpg
          
          If that doesn't exist either, return None.
        """

#    def getSlot3Items():
#        """Return the first 3 content items for the first slot.  We're assuming that a
#        Collection lives at the path /homepage/slot3; we'll return its first three items.
#        """