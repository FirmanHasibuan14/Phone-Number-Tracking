import phonenumbers
from phonenumbers import timezone,geocoder,carrier

def phone(number):
    try:
        phone_number = phonenumbers.parse(number)
        country_phone = geocoder.description_for_number(phone_number, "en")
        sim_card = carrier.name_for_number(phone_number, "en")
        time_zone = timezone.time_zones_for_number(phone_number)
        valid_number = phonenumbers.is_valid_number(phone_number)
        possible_number = phonenumbers.is_possible_number(phone_number)
        validation_number = "is it a valid phone number?"
        possibility_number = "is it a possible number?"
        print(f"Country of origin: {country_phone}")
        print(f"SIM CARD: {sim_card}")
        print(f"Time Zone: {time_zone}")
        if valid_number == True:
            print(f"{validation_number} yes, this number is a valid phone number")
        else:
            print(f"{validation_number} no, this number is not a valid phone number")
        if possible_number == True:
            print(f"{possibility_number} yes, this number is a possible phone number")
        else:
            print(f"{possibility_number} no, this number is not a possible phone number")
    except Exception:
        print("Please input a right phone number, don't forget to input + and try this program once again")

number = input("Input your phone number (using +): \n")
phone(number)
