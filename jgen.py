# import json
# data = {}
# data['q'] = 'value'
# # json_data = json.dumps(data)

# # data['people'].append({  
# #     'name': 'Larry',
# #     'website': 'google.com',
# #     'from': 'Michigan'
# # })
# # data['people'].append({  
# #     'name': 'Tim',
# #     'website': 'apple.com',
# #     'from': 'Alabama'
# # })

# with open('data.json', 'w') as outfile:  
#     json.dump(data, outfile)
# import json
# from pprint import pprint

# json_input = '{"intent": {"name": "greet", "confidence": 0.7028232958181023}, "entities": [], "intent_ranking": [{"name": "greet", "confidence": 0.7028232958181023}, {"name": "goodbye", "confidence": 0.14298864950963153}, {"name": "quiz_search", "confidence": 0.08743951469218535}, {"name": "affirm", "confidence": 0.06674853998008078}], "text": "hello"}{"intent": {"name": "greet", "confidence": 0.7028232958181023}, "entities": [], "intent_ranking": [{"name": "greet", "confidence": 0.7028232958181023}, {"name": "goodbye", "confidence": 0.14298864950963153}, {"name": "quiz_search", "confidence": 0.08743951469218535}, {"name": "affirm", "confidence": 0.06674853998008078}], "text": "hello"}'


# json_data=open('data.json').read()

# data = json.loads(json_data)
# pprint(data)

# try:
#     decoded = json.loads(json_input)
 
#     # Access data
#     for x in decoded['intent']:
#         print(x['name'])
 
# except (ValueError, KeyError, TypeError):
#     print("JSON format error")
 
# for element in data['drinks']:
#     print(element)


import json
from pprint import pprint

st = """{
    "intent": {
        "name": "greet", 
        "confidence": 0.7028232958181023
    }, 
    "entities": [], 
    "intent_ranking": 
    [{
        "name": "greet", 
        "confidence": 0.7028232958181023
    }, 
    {
        "name": "goodbye", 
        "confidence": 0.14298864950963153
    }, 
    {
        "name": "quiz_search", 
        "confidence": 0.08743951469218535
    }, 
    {
        "name": "affirm", 
        "confidence": 0.06674853998008078
    }], 
    "text": "hello"
    }"""
data = json.load(st)
print(data['intent']['name'])