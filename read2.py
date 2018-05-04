import urllib2,json,base64
accesstoken = "KM136SBGGQALRNS3XERV"
institution = "10007772"
#page = 1          # U56135 - Computing 
#page = 4          # U56119 - Software Engineering 
page = 0           # U32101 - Accounting 
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Courses.json?pageIndex={}".format(
	institution,
	page
	)
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response = urllib2.urlopen(request)
data = json.load(response)
for c in data:
	print (c["KisCourseId"], c["Title"])
		
