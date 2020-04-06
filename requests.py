import requests

data_s={
    "name": "mars35",
    "paradigm": "mars programing language"
}
r=requests.post("http://localhost:8000/test/api/languages",data=data_s)