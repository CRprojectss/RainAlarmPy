import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

LAT = "Your Loc Latitude"  # https://www.latlong.net/
LNG = "Your Loc Longitude"
API_KEY = "YOUR API KEY"  # https://openweathermap.org/api/one-call-3#current

# Set up smtp server
smtp_server = smtplib.SMTP('smtp.gmail.com',587)
smtp_server.starttls()

# login to acc
email = "YOUR EMAIL ADDRESS"
password = "YOUR EMAIL PASSWORD"
smtp_server.login(email, password)

# create a msg
msg = MIMEMultipart()
msg['From'] = email
msg['to'] = "RECIPIENT EMAIL ADDRESS"
msg['subject'] = 'Rainalarm'
body = "Hey ho! Bring an umbrella. Rain is forecasted!"
msg.attach(MIMEText(body, 'plain'))


parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,
}

response = requests.get("API CALL", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_codes = []
for n in range(4):
    test_code = weather_data["list"][n]["weather"][0]["id"]
    weather_codes.append(test_code)
    if weather_codes[n] < 700:
        will_rain = True


if will_rain:
    smtp_server.send_message(msg)
    smtp_server.quit()
