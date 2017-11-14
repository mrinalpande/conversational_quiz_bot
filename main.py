import requests, json
import check_resp

#Headers to the query
url = 'http://localhost:5000/parse'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
q = {}

def main():
    
    #Welcome line
    print("Hello, Welcome to conversational quiz bot")

    #Query request and response line
    while(True):
        query = input()
        q['q'] = ''+query+''
        with open('request.json', 'w') as outfile:  
            json.dump(q, outfile)
        payload = json.load(open('request.json'))
        req = requests.post(url, data=json.dumps(payload), headers=headers)
        check_resp.check_resp(req.text)
main()