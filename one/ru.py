from pprint import pprint

data = [
    {"front": "B","to": "E"},
    {"front": "A","to": "C"},
    {'front': 'F','to': 'B'},
    {'front': 'D','to': 'A'},
    {'front': 'C','to': 'F'},
]

_from, _to = [], []
for i in data:
    _from.append(i['front'])
    _to.append(i['to'])

[start] = [i for i in _from if i not in _to]

newData = []
cursor = ""

while len(newData) != len(data):
    for elem in data:
        if len(newData) == 0 and elem.get("front") == start:
            newData.append(elem)
            cursor = elem['to']
        else:
            if elem.get('front') == cursor:
                newData.append(elem)
                cursor = elem['to']


pprint(newData, indent=4)