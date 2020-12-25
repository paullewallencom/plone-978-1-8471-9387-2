contentPath = context.portal_url.getRelativeContentPath(context)
if not contentPath:
    return None
else:
    s = ''
    sectionId = ''
    for pathItem in contentPath:
        sectionId += pathItem + '-'
        s += 'section-' + sectionId[:-1] + ' '
    return s[:-1]