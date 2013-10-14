import re
ERR_USER_LESS_THAN_4 = "Username cannot have less than 4 characters"
ERR_PASS_LESS_THAN_6 = "Password cannot have less than 6 characters"
ERR_PASS_NOT_IDENTICAL = "The password fields are not identical"
ERR_EMPTY_FIELDS = "There are some fields missing, or the POST failed!"
ERR_INVALID_EMAIL = "Email not valid"
ERR_COORDINATE_NOT_FLOAT = "Coordinates should be float numbers"
ERR_COORDINATE_OUT_OF_BOUNDS = "Coordinate is out of bounds"
ERR_FIELDS_NULL = "Fields cannot be null or empty"
FORM_OK = "Form ok"
ADDRESS = "Address"
CONTACT = "Contact"
EMAIL = "Email"
HOURS = "Hours"
LATITUDE = "Latitude"
LONGITUDE = "Longitude"
PASSWORD = "Password"
PICTURE = "Picture"
REGISTRATION_ID = "RegistrationId"
RESTAURANT_NAME = "RestaurantName"
USERNAME = "Username"


def formHasErrors(dictionary):
    for k, v in dictionary.items():
        if v == "" or v is None or v == "null":
            return ERR_FIELDS_NULL
    if len(dictionary[USERNAME]) < 4:
        return ERR_USER_LESS_THAN_4
    if len(dictionary[PASSWORD]) < 6:
        return ERR_PASS_LESS_THAN_6
    # Even if you can verify that the email address is syntactically valid, you'll still need to check
    # that it was not mistyped, and that it actually goes to the person you think it does.
    # The only way to do that is to send them an email and have them click a link to verify.
    if not re.match(r"[^@]+@[^@]+\.[^@]+", dictionary[EMAIL]):
        return ERR_INVALID_EMAIL
    if dictionary[LATITUDE] > 90L or dictionary[LATITUDE] < -90L\
            or dictionary[LONGITUDE] > 180L or dictionary[LONGITUDE] < -180L:
        return ERR_COORDINATE_OUT_OF_BOUNDS


    return FORM_OK