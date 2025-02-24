import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.youtube.com')
except:
    print('Nao esta acessivel.')
else:
    print('Esta acessivel.')