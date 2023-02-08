import pyqrcode
from pyqrcode import QRCode

s = 'Hello World'

url = pyqrcode.create(s)
url.svg('testqrcode.svg', scale=8)
