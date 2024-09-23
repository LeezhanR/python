P ='''In today's digital world, communication happens through various channels. 
    Email remains a primary method, with addresses like john.doe@example.com,   
    jane_smith123@gmail.com, and mike123@yahoo.co.uk being common.
    You may also come across business emails like contact@business.org or support@mycompany.com. 
    Additionally, many people share their contact numbers, such as +1-202-555-0198, (123) 456-7890, 
    +44 7700 900077, or 987-654-3210, making it easier for friends, colleagues, and family to stay in touch. 
    Social media platforms also encourage sharing, with users often providing their Instagram handles or
    Twitter usernames. It's essential to protect personal information while enjoying these communication tools. 
    Remember to always think twice before sharing sensitive data online.'''
import re
Pattern_P = r"\+?[-\s]?\d{1,4}?\(?\d{1,4}\)?[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,4}"

Pattern_G = r"[a-zA-Z0-9]+@[a-zA-Z]+\.[com|in]+"

PhoneNumber = re.findall(Pattern_P,P)
Gmail = re.findall(Pattern_G,P)
print(PhoneNumber)
print(Gmail)