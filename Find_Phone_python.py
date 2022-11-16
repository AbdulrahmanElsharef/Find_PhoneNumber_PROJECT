import phonenumbers
from phonenumbers import geocoder, carrier, timezone
def Find_Phone_Number():
    ''' function for find phone country&network company and timezon
    args:
    phone=enter phone number with country key
    return :
    phone(country & network and time zone)
    '''
    phone = input("enter phone number :".title())  # enter phone number
    phone_num = phonenumbers.parse(phone, None)  # fun country code and number
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


Find_Phone_Number()

# ___________________________________________________
# +962789994570
# Enter Phone Number :+962789994570
# Phone Country Code: 962 National Number: 789994570
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Phone Country Is ** Jordan **
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Phone Network Company Is ** Umniah **
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Phone Time_Zone Is ** ('Asia/Amman',) **

# _______________________________________________
# +201145466788
# Enter Phone Number :+201145466788
# Phone Country Code: 20 National Number: 1145466788
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Phone Country Is ** Egypt **
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Phone Network Company Is ** Etisalat **
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Phone Time_Zone Is ** ('Africa/Cairo',) **
# _____________________________________________________
# 212641999248
# Enter Phone Number :+212641999248
# Phone Country Code: 212 National Number: 641999248
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Phone Country Is **  **
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Phone Network Company Is ** Maroc Telecom **
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Phone Time_Zone Is ** ('Atlantic/Canary',) **
