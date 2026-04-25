
import random

import ast

from Prompts import *
import time
import os
import requests as rq
from datetime import datetime, timedelta


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


def Fact():
	return AI_fetch(promt)




def Football_news():

  try:
    url = "https://football-news11.p.rapidapi.com/api/news-by-league"

    querystring = {"league_id":"52","lang":"en","page":"1"}

    headers = {
      "x-rapidapi-key": os.getenv('X_rapidapi'),
      "x-rapidapi-host": "football-news11.p.rapidapi.com"
    }

    response = rq.get(url, headers=headers, params=querystring)

    return response.json()

  except Exception:
    return ''





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


              
         




# next will be the function that will select the type of leagu to talk about.
# since some of  the data can be posted like that , the ai can decide to make a post from it


def Select_Topic():
    
    return AI_fetch(Selection(ids=competitions,matches=Topic(),news=Football_news()))


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