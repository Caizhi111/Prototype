from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.reverse("114.3594147, 30.5401222")
print(location.address)

 # try {
        #addresses = geocoder.getFromLocation(place.getLatLng().latitude, place.getLatLng().longitude, 1);
        #String address = addresses.get(0).getAddressLine(0);
        #String city = addresses.get(0).getLocality();
        #String state = addresses.get(0).getAdminArea();
        #String zipCode = addresses.get(0).getPostalCode();
        #String country = addresses.get(0).getCountryCode();

        #addStr = address + "," + city + "," + state + "," + zipCode + "," + country;
        #L.e("选择地址", addStr);
    #} catch (IOException e) {
        #e.printStackTrace();
    #}

#原文链接：https://blog.csdn.net/shao941122/article/details/52291907
