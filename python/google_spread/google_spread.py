import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import json

json_key = json.load(open('google spread-95da6203c867.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
worksheet = gc.open("spread").sheet1
rows = worksheet.get_all_values()


result = []
for i in range(3, len(rows)):
    hero = dict()
    for j in range(0, len(rows[i])):
        hero[rows[0][j]] = rows[i][j]
    result.append(hero)





print(result[0])

