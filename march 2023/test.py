import http.client
import pprint
import json

conn = http.client.HTTPSConnection("api.surveymonkey.com")

headers = {
    'Accept': "application/json",
    'Authorization': "Bearer {access_token}"
}



conn.request("GET", "/v3/surveys/406561997/pages/39283261/questions/123840398/", headers=headers)

res = conn.getresponse()
data = res.read()

pprint.pprint(json.loads(data.decode("utf-8")))
