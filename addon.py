import re
import xbmcgui
import requests

url = 'https://apid.sky.it/vdp/v1/getLivestream?id=2&jsonp=jsonP.queue.jsonP0_1570037187545'
res = requests.get(url)

try:
	streaming_url = 'https://sbshdlu5-lh.akamaihd.net/i/sbshdl_7@106896/master.m3u8?hdnts=st=1584575040~exp=1584661440~acl=/i/*~hmac=408719d9932fa30c431509eb224d265c6fca2b4a1c5ef014c4ac8e67a183f024&mux_audio=true'
	thumb_url = 'https://' + re.findall('"img":"https{0,1}://(.*?)"', res.text)[1]
	listitem = xbmcgui.ListItem('Home and Garden TV')
	listitem.setInfo('video', {'Title': 'Home and Garden  TV'})
	listitem.setArt({ 'thumb': thumb_url})
	xbmc.Player().play(streaming_url, listitem)

except Exception as ex:
	message = 'Eccezione: %s' % ex
	listitem = xbmcgui.ListItem('Home and Garden  - Errore')
	listitem.setInfo('video', {'Title': 'Errore nell\' avvio del plugin Home and Garden '})
	listitem.setInfo('video', { 'plot': message })
