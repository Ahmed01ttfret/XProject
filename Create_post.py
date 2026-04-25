


from Fetch_Data import *
from Write_to_json import Write
import random


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
        
