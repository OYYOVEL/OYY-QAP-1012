### задание 15.4.2

import json
import os

template = {'timestamp' : 'int',
            'referer' : 'str',        # URL (http:\\ or https:\\)
            'location' : 'str',       # URL (http:\\ or https:\\)
            'remoteHost' : 'str',
            'partyId' : 'str',
            'sessionId' : 'str',
            'pageViewId' : 'str',
            'eventType' : 'str',      # (itemBuyEvent or itemViewEvent)
            'item_id' : 'str',
            'item_price' : 'int',
            'item_url' : 'str',       # URL (http:\\ or https:\\)
            'basket_price' : 'str',
            'detectedDuplicate' : 'bool',
            'detectedCorruption' : 'bool',
            'firstInSession' : 'bool',
            'userAgentName' : 'str' 
}

f_name = 'json_example_QAP.json'
starts = ('http://', 'https://')
url = ['referer', 'location', 'item_url']
event = ['itemBuyEvent', 'itemViewEvent']
err = []

print ()
print (' Эта программа проверяет json-файл на соответствие требованиям к структуре и типам данных')
print ()

### открытие файла и чтение данных с последующей их десерилизацией
with open(f_name, encoding = 'utf8') as f_file:
    dataStr = f_file.read()
    data = json.loads (dataStr)

### проверка данных во всём файле по приоритету:
for i in range (len (data)):
    
    ### количества полей
    if len (data [i]) != len (template) :
        err.appеnd ('Ошибка количества полей: ожидалось ' + len (template) + ', по факту: ' + len (data [i]))
        break
    
    ### структуры именованных полей
    if template.keys() != data [i].keys():
        err.append ('Ошибка имён ключей: ожидалось' + template.keys() + 'По факту: ' + data [i].keys())
        break
    
    ### правильности типов данных
    for key in template.keys():
        if str (type (data [i][key])) != ("<class '" + template [key] + "'>"):
            err.append ('Ошибка типа данных: ожидалось ' + template [key] + ', по факту: ' + type (data [i][key]))
            break
        
    ### корректности URL
    for name in url:
        if not data [i][name].startswith (starts):
            err.append ('Ошибка URL: ожидалось http:// или https://, по факту: ' + data [i][name][:8])

    ### валидности eventType
    if data [i]['eventType'] not in event:
        err.append ('Ошибка значения "eventType": ожидалось itemBuyEvent или itemViewEvent, по факту: ' + data [i]['eventType'])
    
### если ошибок нет
if not err:
    print (' Данные в файле', f_name, 'полностью соответствуют требованиям документации')
else:
    print (err)

print ()
















