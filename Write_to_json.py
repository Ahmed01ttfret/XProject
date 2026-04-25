import json

def Write(text):
  data=Read_last_3()
  if len(data)<10 and len(data)>0:
    data.append(text[0])
  elif len(data)==0:
    data=text
  else:
    
    data.pop(0)
    data.append(text[0])

  with open("data.json", "w") as f:
    json.dump(data, f)

def Read_last_3():
  with open("data.json", "r") as f:
    data = json.load(f)
    return data