import pandas as pd

excel_file = 'hongkong.csv'

df = pd.read_csv(excel_file)
mylist=[10]

ls=df.loc[df['accommodates'].isin(mylist)]

# print(ls)


# Use getitem ([]) to iterate over columns in pandas DataFrame

# image
# listing url
# id
# name
for index, row in ls.iterrows():
    print(row['accommodates'], row['amenities'])
    payload = "/product{\"product_id\":\"" + str(row['id']) + "\"}"
    buttons = []
    myelements=[]
    newobj={
            "title": row['name']+row['price'],
            "subtitle": row['description'],
            "image_url": row['picture_url'],
            "buttons": [ 
                {
                "title": "Buy now",
                "url": row['listing_url'],
                "type": "web_url"
                # "type": "postback",
                # "payload":payload
                }
            ]
        }
    myelements.append(newobj)
message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": myelements
                
                }
    }
dispatcher.utter_message(attachment=message)
 