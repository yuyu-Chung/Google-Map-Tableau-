# Google map 軌跡資料集json檔案轉換成DataFrame再轉換成CSV2檔案匯出
import json
import pandas as pd

def data_fransfer():
    with open("時間軸.json", "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    raw_data_fixed = raw_data.copy()

    #print(raw_data_fixed.keys)

    df = pd.DataFrame(columns=["No", "Lat", "Lon", "timestamp", "day"])

    print(len(raw_data_fixed))
    print(raw_data_fixed.keys())
    target = raw_data_fixed['semanticSegments']

    No = 0
    for i in range(len(target)):
        if 'timelinePath' in target[i]:
            timelinePath = target[i]["timelinePath"]
            for j in range(len(timelinePath)):
                point = timelinePath[j]["point"]
                time = timelinePath[j]["time"]
                point_fixed = point.split(",")
                Lat = point_fixed[0]
                Lon = point_fixed[1].strip() 
                time_fixed = time[:19]
                df.loc[No, "No"] = No+1
                df.loc[No, "Lat"] = Lat[:7]
                df.loc[No, "Lon"] = Lon[:8]
                df.loc[No, "timestamp"] = time_fixed
                No+= 1
    day = 1
    for k in range(len(df)):
        if k == 0:
            df.loc[k, "day"] = 1
        elif df.loc[k, "timestamp"][:10] == df.loc[k-1, "timestamp"][:10]:
            df.loc[k, "day"] = day
        else:
            df.loc[k, "day"] = day+1
            day+= 1

    print(df.head())
    print(df.tail())
    df.to_csv("Google定位資訊set.csv")
    
    #dict_keys(['semanticSegments', 'rawSignals', 'userLocationProfile'])
    #target = raw_data_fixed["semanticSegments"]
    #timeline = target[::2]

    #for i in range(len(timeline)):
        #print(timeline[i])


    #print(raw_data_fixed.values())
    #for key, value in raw_data_fixed.items():
        #print(key, value)


data_fransfer()
