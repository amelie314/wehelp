import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import json
import csv
import urllib.request

def save_attractions_to_csv(attractions):
    with open('attraction.csv', mode='w', encoding='utf-8', newline='') as file:

        writer = csv.writer(file)
        
        writer.writerow(["景點名稱", "區域", "經度", "緯度", "第一張圖檔網址"])
        
        for attraction in attractions:
            name = attraction['stitle']
            district = attraction['address'].split()[1].split('區')[0] + "區"
            longitude = attraction['longitude']
            latitude = attraction['latitude']
            image_url = "https://" + attraction['file'].split('https://')[1]
            writer.writerow([name, district, longitude, latitude, image_url])
        
        print(attraction['address'].split()[1].split('區')[0] + "區")

def group_attractions_by_mrt_station(attractions):

    mrt_groups = {}
    
    for attraction in attractions:
        mrt = attraction['MRT']
        if mrt:
            station = mrt.split()[0]
            if station not in mrt_groups:
                mrt_groups[station] = []
            mrt_groups[station].append(attraction)

    return mrt_groups

def save_attractions_by_mrt_to_csv(mrt_groups, attractions_count):

    with open('mrt.csv', mode='w', encoding='utf-8', newline='') as file:
    
        writer = csv.writer(file)

        chinese_num = ["一", "二", "三", "四", "五", "六", "七"]
    
        header = ["捷運站名稱"] + ["景點名稱" + chinese_num[i] for i in range(attractions_count)]
    
        writer.writerow(header)
        
        for station, attractions in mrt_groups.items():
            attraction_names = [attraction['stitle'] for attraction in attractions]
            
            attraction_num = " "

            if len(attraction_names) >= attractions_count:
                attraction_num = attraction_names[:attractions_count]
            else:
                attraction_num = attraction_names + [''] * (attractions_count - len(attraction_names))
            writer.writerow([station] + attraction_num)
            
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))

if data:
    attractions = data['result']['results']

    save_attractions_to_csv(attractions)

    mrt_groups = group_attractions_by_mrt_station(attractions)

    attractions_count = max(len(mrt_groups[station]) for station in mrt_groups)
    
    save_attractions_by_mrt_to_csv(mrt_groups, attractions_count)