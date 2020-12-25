from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common

class LogoViewlet(common.LogoViewlet):
    """Alter the logo to include the description of our website
    """
    def render(self):
        return self.index()
    index = ViewPageTemplateFile('logo.pt')
    
class PathBarViewlet(common.PathBarViewlet):
    """Moving to a new viewlet manager and adjusting the dividers
    """
    def render(self):
        return self.index()
    index = ViewPageTemplateFile('path_bar.pt')
    
class SearchBoxViewlet(common.SearchBoxViewlet):
    """Customizing the searchbox to use the locally defined page template
    """
    def render(self):
        return self.index()
    index = ViewPageTemplateFile('searchbox.pt')