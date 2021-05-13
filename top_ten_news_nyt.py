import requests
import pandas as pd
#### This is a script that allows you to take details of the
# last ten news from the team or another site. Store them in a nice csv
# or excel file

# I got the links from the developers webpage
# from nyt = https://developer.nytimes.com/docs/most-popular-product/1/overview
key='CUpT0SDiyV2BWXatBG4ZKSpF8r7r7Ac6'
url ='https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key='+key
response = requests.get(url)

print('The response is: ', response.json())

dic=response.json()

print('Dictionary made from the keys: ', dic.keys())

for elem in list(dic.keys()):
    print('##############################################')
    print("clé: ",elem,"// values: ", dic[elem])

topten_results = dic['results'][:10]

for elem in enumerate(topten_results):
    print('###############################################')
    print(elem)

print(topten_results[0].keys())

df_opten_results = pd.DataFrame(topten_results)
df_opten_results.to_csv("./top_ten_news_nyt.csv")

for i in range(len(topten_results)):
    print(i)
    for elem in enumerate(topten_results[i].keys()):
            print('###############################################')
            print(' Key : ', elem[1], 'Values : ', topten_results[i][elem[1]])
