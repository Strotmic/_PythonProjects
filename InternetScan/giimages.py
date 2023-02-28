from google_images_search import GoogleImagesSearch

gis = GoogleImagesSearch('AIzaSyB0ci0PP2Ev4PO57f9UI7ExtCTHp0XE5kM', 'My First Project')

_search_params = {
    'q': '...',
    'num': 10,
    'fileType': 'jpg|gif|png',
    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
    'safe': 'active|high|medium|off|safeUndefined', ##
    'imgType': 'clipart|face|lineart|stock|photo|animated|imgTypeUndefined', ##
    'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined', ##
    'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined', ##
    'imgColorType': 'color|gray|mono|trans|imgColorTypeUndefined' ##
}

# this will only search for images:
gis.search(search_params=_search_params)

# this will search and download:
gis.search(search_params=_search_params, path_to_dir='/path/')

# this will search, download and resize:
gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

