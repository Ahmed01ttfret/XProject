
import random

import ast
from Prompts import *
import time
import os
import requests as rq
from datetime import datetime, timedelta




def Fact():
	return AI_fetch(promt)







class LaLigaData:
    def __init__(self):
        self.headers = {
            "x-rapidapi-key": os.getenv('X_rapidapi'),
            "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
        }

    def get_standings(self):
        url = "https://www.thesportsdb.com/api/v1/json/123/lookuptable.php"
        params = {'l': '4335'}
        res = rq.get(url, params=params)
        if res.status_code == 200:
            return res.json()
        return None

    def get_top_assists(self):
        url = "https://free-api-live-football-data.p.rapidapi.com/football-get-top-players-by-assists"
        querystring = {"leagueid": '87'}
        response = rq.get(url, headers=self.headers, params=querystring)
        return response.json()

    def get_top_goals(self):
        url = "https://free-api-live-football-data.p.rapidapi.com/football-get-top-players-by-goals"
        querystring = {"leagueid": '87'}
        response = rq.get(url, headers=self.headers, params=querystring)
        return response.json()

    def get_top_ratings(self):
        url = "https://free-api-live-football-data.p.rapidapi.com/football-get-top-players-by-rating"
        querystring = {"leagueid": '87'}
        response = rq.get(url, headers=self.headers, params=querystring)
        return response.json()

    def get_schedule(self):
        url = "https://www.thesportsdb.com/api/v1/json/123/eventsday.php"
        params = {
            "d": datetime.now().strftime("%Y-%m-%d"),
            "s": "Soccer",
            "l": "4335"
        }
        response = rq.get(url, params=params)
        return response.json()

		











now=datetime.now()
competitions = {
    "FIFA World Cup": "WC",
    "UEFA Champions League": "CL",
    "Bundesliga": "BL1",
    "Ligue 1": "FL1",
    "European Championship": "EC",
    "Serie A": "SA",
    "Premier League": "PL",
    'Laliga':4335
}





class GetData:
    def __init__(self,id):
        self.id=id
        self.header={'X-Auth-Token':os.getenv('X_foot_org')}
        self.base_url='http://api.football-data.org/v4/competitions'
    
    
    def Standings(self):
        try:
            req=rq.get(url=self.base_url+f'/{self.id}/standings',headers=self.header)
            return req.json()
        except Exception as t:
            pass


    def Goals(self):
        try:
            req=rq.get(url=self.base_url+f'/{self.id}/scorers',headers=self.header)
            return req.json()
        except Exception as t:
            pass
    def shedule(self):
        try:
            params = {
                "dateFrom": (now - timedelta(days=1)).strftime("%Y-%m-%d"),
                "dateTo": (now + timedelta(days=3)).strftime("%Y-%m-%d"),
            }
             
            req=rq.get(url=self.base_url+f"/{self.id}/matches",params=params,headers=self.header)
            return req.json()

        except Exception as t:
            pass



import time

def Topic():
    schedule = {}
    for ids in competitions.keys():
        if ids == 'Laliga':
            data = LaLigaData().get_schedule()
            schedule[ids] = data
        else:
            data = GetData(id=competitions[ids]).shedule()
            schedule[ids] = data
            time.sleep(1)
    
    return schedule
  
              
         




# next will be the function that will select the type of leagu to talk about.
# since some of  the data can be posted like that , the ai can decide to make a post from it


def Select_Topic():
	return AI_fetch(Selection(ids=competitions,matches=Topic()))


import ast

def convert_from_txt_to_dict(text):
    

    ind = []
    for index, x in enumerate(text):
        if x == '{' or x == '}':
            ind.append(index)

    

    data = text[ind[0]:ind[1] + 1]
    v = ast.literal_eval(data)
    return v


def convert_from_txt_to_list(text):
	ind=[]
	for index , x in enumerate(text):
		if x==']' or x=='[':
			ind.append(index)
    
	
	data=text[ind[0]:ind[1]+1]

	v=ast.literal_eval(data)
	return v



def create_post():
    topic = Select_Topic()
    data = convert_from_txt_to_dict(text=topic)

    first_key = list(data.keys())[0]

    if first_key == 'FFT':
        data=Fact()
        Write([data])
        return data
        

    elif first_key == 'Post':
        ret= data['Post']
        Write([ret])
        return ret

    else:
        dt=convert_from_txt_to_list(text=topic)
        if dt[0]=='Laliga':
            info=LaLigaData()
            listt=[1,2,3,4]
            
            if random.choice(listt)==1:
                #standings
                dat= Post(compname='Laliga standings',data=info.get_standings())
                Write([dat])
                return dat
            elif random.choice(listt)==2:
                # Asist
                dat= Post(compname='Laliga Asist record',data=info.get_top_assists())
                Write([dat])
                return dat
            elif random.choice(listt)==3:
                #goals
                dat= Post(compname='Laliga goal record',data=info.get_top_goals())
                Write([dat])
                return dat
            else:
                # Rattings
                dat= Post(compname='Average rating for laliga',data=info.get_top_ratings())
                Write([dat])
                return dat

        else:
            info=GetData(id=competitions[dt[0]])
            listt=[1,2]
            
            if random.choice(listt)==1:
                # standings
                dat= Post(compname=f'{dt[0]} standings',data=info.Standings())
                Write([dat])
                return dat
            else:
                # goals
                dat= Post(compname=F'{dt[0]} goal record',data=info.Goals())
                Write([dat])
                return dat
        
