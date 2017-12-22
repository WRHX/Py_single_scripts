import datetime

## Everything in dd/mm/yyyy format

dob_d = input('Enter day of birth (dd)\n') #user date of birth
if len(dob_d) == 2:
    print('String length Ok')
else:
    print('Bad input')
if dob_d.isdigit() == True:
    print('Data type Ok')    
else:
    print('Bad input')
    
dob_m = input('Enter month of birth (mm)\n')
if len(dob_m) == 2:
    print('String length Ok')
else:
    print('Bad input')
if dob_m.isdigit() == True:
    print('Data type Ok')    
else:
    print('Bad input')

dob_y = input('Enteryear of birth (yyyy)\n')
if len(dob_y) == 4:
    print('String length Ok')
else:
    print('Bad input')
if dob_y.isdigit() == True:
    print('Data type Ok')    
else:
    print('Bad input')


currentDate = datetime.datetime.now()
yearDiff = currentDate.year - int(dob_y)

if currentDate.year > int(dob_y) and currentDate.month >= int(dob_m) and currentDate.day >= int(dob_d):
    age = yearDiff
else:
    age = yearDiff-1

print(age)




