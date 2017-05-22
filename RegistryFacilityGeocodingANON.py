# Google maps JavaScript API 
# 10x multiplier for text search towards quota
## https://maps.googleapis.com/maps/api/place/textsearch/json?query=123+main+street&key=YOUR_API_KEY

import urllib.request, json, csv
apikey = "YOUR_API_KEY_HERE"
f = open('../Input/Data To Merge/ReportingFacilityCrosswalk.csv','r')
reader = csv.reader(f)
facilitylist = list(reader)
#print(facilitylist[1:10])

#Grabbing and parsing the JSON data
def GoogPlac(placename,key):
  #making the url
  MyUrl = ('https://maps.googleapis.com/maps/api/place/textsearch/json'
           '?query=%s'
           '&key=%s') % (placename, apikey)
  #grabbing the JSON result
  response = urllib.request.urlopen(MyUrl)
  jsonRaw = response.read()
  jsonData = json.loads(jsonRaw)
  return jsonData

#Format place name for insertion into url
def NameFormat(placename):
    return(('+').join(placename.split()))

for facility in facilitylist:
    testname = NameFormat(facility[1])
    x = GoogPlac(testname, apikey)
    try:
        address = x['results'][0]['formatted_address']
        facility.append(address)
    except:
        print(x)
        facility.append('')
        
with open('../Input/Data To Merge/ReportingFacilityAddresses.csv', "w", newline="\n", encoding="utf-8") as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(facilitylist)


