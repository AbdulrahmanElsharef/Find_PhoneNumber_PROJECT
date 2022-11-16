import phonenumbers
from phonenumbers import geocoder, carrier, timezone
def Find_Phone_Number():
    ''' function for find phone country&network company and timezon
    args:
    phone=enter phone number with country key
    return :
    phone(country & network and time zone)
    '''
    while True:  # INFINITY loop for programme
        print(50*"x")
        phone = input("enter phone number :".title())  # enter phone number
        # fun country code and number
        phone_num = phonenumbers.parse(phone, None)
        phone_country = geocoder.description_for_number(
            phone_num, "en")  # fun find phone country
        phone_network = carrier.name_for_number(
            phone_num, "en")  # fun find phone network
        phone_tzone = timezone.time_zones_for_number(
            phone_num)  # fun find phone time zone
        print(f"Phone {phone_num}")
        print(50*"x")
        print(f"phone country is ** {phone_country} **".title())
        print(50*"x")
        print(f"phone network company is ** {phone_network} **".title())
        print(50*"x")
        print(f"phone time_zone is ** {phone_tzone} **".title())
        print("find phone is finished".title())
        
Find_Phone_Number() # run program

