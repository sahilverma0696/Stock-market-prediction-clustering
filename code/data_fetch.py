from nsepy import get_history
from datetime import date
from yaml import dump

def save_data(name,df):
    if(df.to_csv(path_or_buf="../data/"+name)):
        return True
    else:
        return False


def yml_update(entry_dict):
    with open("../data/entries.yaml",'w') as f:
        data = dump(entry_dict,f,)
        print(data)


def get_data(symbol,start_date=date(2000,1,1),end_date=date.today()):
    data = get_history(symbol,start_date,end_date)
    if(data):
       if(save_data(symbol,data)):
           data_dict = {"Name":symbol,"start_date":start_date,"end_date":end_date}
           yml_update(entry_dict)
    else:
        return False

#get_data(symbol="SBIN", start_date=date(2015,1,1), end_date=date(2015,1,31))