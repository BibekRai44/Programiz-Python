from datetime import datetime
my_date_string="feb 23 2021 08:54AM"
datetime_object = datetime.strptime(my_date_string,'%b %d %Y %I:%M%p')
print(type(datetime_object))
print(datetime_object)