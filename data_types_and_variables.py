# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, # #they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a #movie per day is 3 dollars, how much will you have to pay?

from ssl import _PasswordType
from xml.dom.pulldom import START_DOCUMENT


movies = {
    "The little mermaid": 3,
    "Brother Bear": 5,
    "Hercules": 1
}  
price_per_day = 3

total_owed = price_per_day * sum(movies.values())
print(total_owed)



movies = {
    "The little mermaid": 3,
    "Brother Bear": 5,
    "Hercules": 1
}  

movies = movies.values())

def sum_of_movies(movies):
    if a == b == c:
        return (a + b + c) * 3
    else:
        return a + b + c
    
print(sum_of_movies())


# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a # # different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will # you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours # for Amazon.


# figuring out rate per hour different companies from a dictionary

import itertools as it

company = ['Google', 'Amazon', 'Facebook']
pay = [400, 380, 350]
hours = [6, 4, 10]

for (a, b, c,) in it.zip_longest (company, pay, hours):
      print(a, b * c)

    



#def pay_per_hour(company, hours):
#    if company == 'Google':
#        return 400 * hours
#    elif company == 'Amazon':
#        return 380 * hours
#    elif company == 'Facebook':
#        return 350 * hours
#    else:
#        return 'Not a valid company'

    
#[google, amazon, facebook] = ["Google", "Amazon", "Facebook"]
#[company,rate_per_hour, hours] = ['Google', 6), pay_per_hour(Amazon, 4), pay_per_hour(Facebook, 10)]

#pay = [400, 380, 350]
#hours = [6, 4, 10]

#companies = [google,

#def pay_per_hour(company, hours):
#    for (let i in company) {
#        console.log(company[i]);
#}
#    for 
#        return pay * hours
#    elif company == "Amazon":
#        return pay * hours
#    elif company == "Facebook":
#        return pay * hours
#    else:
#        return "Company not found"
    
#print(pay_per_hour("Google", 6))
#print(pay_per_hour("Amazon", 4))
#print(pay_per_hour("Facebook", 10))

    
 #"google", 400,
 #   "amazon": 380,
 #   "facebook": 350
  

#hours_worked = {
#    "google": 6,
 #   "amazon": 4,
 #   "facebook": 10
#rate_per_hour = rate_per_hour.values()
#print(rate_per_hour)

#companies = rate_per_hour.keys()[0]
#income = rate_per_hour.values()[0]
#print (income + rate_per_hour.values)






# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.



if class_is_not_full and class_schedule_does_not_conflict:
    print("You can enroll in this class")
else:
    print("You cannot enroll in this class")


class_is_not_full = True
schedule_does_not_conflict = True
enroll = class_is_not_full and schedule_does_not_conflict
enroll


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.


def can_apply_offer(items, is_premium_member, offer_is_expired):
    if is_premium_member:
        return True
    elif items >= 2 and not offer_is_expired:
        return True
    else:
        return False



premium_member = True
more_than_two_items = False
coupon_not_expired = True
coupon_not_expired and (more_than_two_items or premium_member)
    
# username = 'codeup'
# password = 'notastrongpassword'
#Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters

password = len(password) >= 5

# the username must be no more than 20 characters

username = len(username) git <= 20

# the password must not be the same as the username

username != password


# bonus neither the username or password can start or end with whitespace

username = username.strip()
password = password.strip()


my_username = 'King'
my_password = 'Ryanisthebest'
Check_1 = len(my_password) > 4
Check_1
Check_2 = len(my_username) <= 20
Check_2
Check_3 = my_username != my_password
Check_3