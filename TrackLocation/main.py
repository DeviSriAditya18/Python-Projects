import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

pnum=phonenumbers.parse(number)
loc=geocoder.description_for_number(pnum,"en")
print(loc)

ser_pro=phonenumbers.parse(number)
print(carrier.name_for_number(ser_pro,"en"))

key='a557b6f9eef44902be0fb14528ccdec1'
geocoder=OpenCageGeocode(key)
query=str(loc)
res=geocoder.geocode(query)
#print(res)

lat=res[0]['geometry']['lat']
lng=res[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(loc=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=loc).add_to(myMap)

myMap.save("mylocation.html")
