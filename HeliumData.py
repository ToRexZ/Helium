from pushbullet import Pushbullet
import requests
import json

with open('Endpoints.json','r') as ApiManager:
  api = json.load(ApiManager)
  ApiManager.close()

accessToken = api['PushbulletAccessToken']
hotspotAddress = api['B58_Address']

# Accessing the Endpoints object
endpoints = api['URL_Endpoints']


activityCountURL = endpoints['ActivityCount']
rewardsURL = endpoints['rewardsURL']


URL = activityCountURL.replace(":address", hotspotAddress)

filter = {'filter_types': 'rewards_v2'}

response = requests.get(URL, params=filter)

data = json.loads(response.text)

dataStorage = {'rewards_v2_num'}

number = data['data']['rewards_v2']
with open('hotspotdata.json','r') as previousData:
  datacontents = json.loads(previousData.read())
  last_number = datacontents['rewards_v2_num']

if number > last_number:
  with open('hotspotdata.json','w') as datafileWrite:
    dataStorage = {'rewards_v2_num':str(number)}
    json.dump(dataStorage,datafileWrite)

  pb = Pushbullet(accessToken)
  push = pb.push_note('Rewards',number)

