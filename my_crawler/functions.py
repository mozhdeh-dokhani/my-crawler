#------------------------- Mozhdeh Dokhani ---------------------------------------
# date:    97/04/19
# version: 1.0
#---------------------------------------------------------------------------------

#------------------------------- Libraries ---------------------------------------
import re
#---------------------------------------------------------------------------------

#------------------------------------ Main ---------------------------------------
def processText( text, replaceExtra = True, removeExtraSpaces = True, removeTags = True, huffington = False ):

    #Slice text up to some specific extra parts
    if huffington:
        i = text.rfind('HuffPost may receive a share from purchases made via links on this page')
        if i:
            text = text[:i]

        i = text.rfind('RELATED...')
        if i:
            text = text[:i]

        i = text.rfind('RELATED COVERAGE')
        if i:
            text = text[:i]

        i = text.rfind('RELATED CONTENT')
        if i:
            text = text[:i]

        i = text.rfind('More from PureWow:')
        if i:
            text = text[:i]

    #Replace extra characters
    if replaceExtra:
        text = text.replace('"', '').replace("\'", '').replace(' .', '.').replace('\\n', '')

    #Remove the spaces from the end and at the begining and also duplicate spaces
    if removeExtraSpaces:
        text = " ".join(text.split())

    #Remove all html tags, <style> and <script>
    if removeTags:
        text = re.sub(r'<(style).*?<(\/style)>', '', text, flags = re.DOTALL)
        text = re.sub(r'<(script).*?<(\/script)>', '', text, flags=re.DOTALL)
        text = re.sub('<.*?>', '', text)

    #Remove Download word at the end of string
    if huffington:
        if text.endswith('Download'):
            text = text[:-len('Download')]

    return text
#---------------------------------------------------------------------------------

#TODO not able to remove codes between <script>