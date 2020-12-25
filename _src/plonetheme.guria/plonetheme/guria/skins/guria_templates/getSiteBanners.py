
## Script (Python) "getSiteBanners"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Get site banners
##
 
# returns section ids and image urls for section banners
# consult the onenw.template/docs/section-banners.txt for more info

from Products.CMFCore.utils import getToolByName

site = getToolByName(context, 'portal_url').getPortalObject()
IMAGES_FOLDER_NAME  = 'images'
BANNERS_FOLDER_NAME = 'banners'
# these all need to be the same length
BANNER_PREFIXES     = ('banner-', 'header-')

def isBannerish(name):
    """returns True if name starts with a banner prefix"""
    for b in BANNER_PREFIXES:
        if name.startswith(b):
            return True
    return False

banners_folder_path = '%s/%s/%s' % ('/'.join(site.getPhysicalPath()),
                                    IMAGES_FOLDER_NAME,
                                    BANNERS_FOLDER_NAME)
banners = context.portal_catalog.searchResults(path=banners_folder_path,
                                               portal_type='Image',
                                               depth=1,
                                               sort_on='getId',
                                               sort_order='descending')

prefix_length = len(BANNER_PREFIXES[0])
return [{'section':b.getId[prefix_length:-4],
         'url': b.getURL() } for b in banners if isBannerish(b.getId)]