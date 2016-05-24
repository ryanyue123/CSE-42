import urllib.parse
import urllib.request

user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
header={'User-Agent' : user_agent}
url = "https://docs.google.com/forms/d/1SZDRadn40tmNxm-BlvSQ7KbKTlSfDD2shjffJ5amWs4/"
# values from your form. You will need to include any hidden variables if you want to..
values= {
'entry.628036071': 'Jason Wu'
}
data = urllib.parse.urlencode(values)
response = urllib.request.Request(url, data, header)