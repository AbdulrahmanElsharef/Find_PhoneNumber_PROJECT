import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from pywebio.input import *
from pywebio.output import *
def Find_Phone_Number():
    ''' function for find phone country&network company and timezon
    args:
    phone=enter phone number with country key
    return :
    phone(country & network and time zone)
    '''
    while True:
        phone = input(
            "enter phone number    ( country key '+00'):".title())  # enter phone number
        # fun country code and number
        phone_num = phonenumbers.parse(phone, None)
        phone_country = geocoder.description_for_number(
            phone_num, "en")  # fun find phone country
        phone_network = carrier.name_for_number(
            phone_num, "en")  # fun find phone network
        phone_tzone = timezone.time_zones_for_number(
            phone_num)
        # fun find phone time zone
        put_table([[phone, phone_country, phone_network, phone_tzone], ], header=[
            'phone_Number', 'Phone_Country', 'Phone_Net_Company', "Phone_Time_Zone"]).style('color: yellow; font-size: 25px')

if __name__ == "__main__":
    Find_Phone_Number()  # run program
