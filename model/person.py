import json

class Person:
    __slots__ = (
        'first_name',
        'last_name',
        'national_id',
        'birth_certificate',
        'birth_day',
        'birth_month',
        'birth_year',
        'phone',
        'state',
        'city'
    )

    def __init__(self, file):
        with open(file) as json_file:
            # load the file as a json object
            data = json.load(json_file)
            # initialize slots with json_file data
            self.first_name = data['firstName']
            self.last_name = data['lastName']
            self.national_id = data['nationalId']
            self.birth_certificate = data['birthCertificate']
            self.birth_day = data['birthDay']
            self.birth_month = data['birthMonth']
            self.birth_year = data['birthYear']
            self.phone = data['phoneNumber']
            self.state = data['state']
            self.city = data['city']
        
