import requests
import time
from datetime import date
import smtplib
import time
import schedule


from requests.sessions import session
today = date.today()
date = today.strftime("%d-%m-%Y")

URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=390&date={}'.format(date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def send_mail(name,address,fee_type,date,vaccine,avalability):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    sender_email = "poladiyadharmesh@gmail.com"
    receiver_email = "poladiyadharmesh@gmail.com"
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('poladiyadharmesh@gmail.com', 'fhhaodpryqohbbcp')
    subject = 'Slot Available'
    body = f'\nNew Vaccine slot available\n Name: {name} \n Address: {address}\n Date: {date} \n Vaccine: {vaccine} \n Fees: {fee_type} \n Avalability: {avalability} \n\n Please confirm the slot on official site'
    msg = f"Subject: {subject}\n\n{body}"
    #server.sendmail(
    #'Price check',
    #'email-address',
    #msg
    #)
    server.sendmail(sender_email, receiver_email, msg)
    print('Hey Email has been sent!')
    server.quit()

def findAvailability():
    ct = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["centers"]
    for val in data:
        if(val['pincode']==424101):
            sessions = val['sessions']
            for ses in sessions:
                if((ses["available_capacity"] > 0) & (ses["min_age_limit"] >= 18)):
                    ct += 1
                    send_mail(val["name"],val['address'],val['fee_type'],ses["date"],ses["vaccine"],ses["available_capacity"])
                    return

    if(ct == 0):
        print("No Available Slots")
    else:
        print('tot ct',ct)


while(True):
    time.sleep(5)
    findAvailability()