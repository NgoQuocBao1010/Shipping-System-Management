import geocoder
g = geocoder.ip('me')
print(g.latlng)