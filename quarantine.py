import requests
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#from requests_toolbelt.utils import dump

class Opeviabrowser:
    def __init__(self, user='', passwd=''):
        self.s = requests.Session()
        self.login_url = 'https://defense-prod05.conferdeploy.net/login'
        payload = json.dumps({'username': user,'password': passwd})
        headers = {'Content-Type':'application/json'}
        self.r = self.s.post(self.login_url, data=payload, headers=headers, verify=False)
        self.orgId = self.r.json()["currentOrgId"]
#        data = dump.dump_all(self.r)
#        print data.decode('utf-8')
        print 'login status:', self.r.status_code
        csrftoken = self.r.headers['x-csrf-token']
        self.s.headers.update({'X-CSRF-Token': csrftoken})

    def quarantine(self,deviceId,onoff):
        payload = json.dumps({"deviceIds":[deviceId]})
        headers = {'Content-Type':'application/json'}
        req = self.s.post('https://defense-prod05.conferdeploy.net/appservices/v5/orgs/{0}/devices/actions/quarantine/{1}'.format(self.orgId,onoff),data=payload, headers=headers)
#        data = dump.dump_all(req)
#        print data.decode('utf-8')
        print req.status_code
        print req.text


if __name__ == "__main__":
    q = Opeviabrowser()
    q.quarantine(sys.argv[1],sys.argv[2])
