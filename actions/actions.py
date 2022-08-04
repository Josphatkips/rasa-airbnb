# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import pandas as pd

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#
class ActionGetSuggestion(Action):

    def name(self) -> Text:
        return "action_get_room"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            excel_file = 'hongkong.csv'
            df = pd.read_csv(excel_file)
            mylist=[int(tracker.get_slot('room_id'))]

            ls=df.loc[df['id'].isin(mylist)]
            buttons = []
            myelements=[]
            print(tracker.get_slot('room_id'))
            print(ls)
            for index, row in ls.iterrows():
                print("I am in for")
                dispatcher.utter_message(text = row['name'])
                dispatcher.utter_message(text = row['price'])
                dispatcher.utter_message(image = row['picture_url'])
                dispatcher.utter_message(text = row['description'])
                # print(tracker.get_slot('room_id'))
                # print("hello")
            
            return []

class ActionGetSuggestion(Action):

    def name(self) -> Text:
        return "action_get_suggestion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        excel_file = 'hongkong.csv'
        df = pd.read_csv(excel_file)
        mylist=[1]

        ls=df.loc[df['accommodates'].isin(mylist)]
        buttons = []
        myelements=[]
        for index, row in ls.iterrows():
            # print(row['id'])
            # print('1.+++++++++++++++++++++++++++++++++++++++')
            # print(row['listing_url'])
            # print('2.+++++++++++++++++++++++++++++++++++++++')
            # print(row['name'])
            # print('3.+++++++++++++++++++++++++++++++++++++++')
            # # print(row['description'])
            # # print('4. +++++++++++++++++++++++++++++++++++++++')
            # print(row['picture_url'])
            # print('4. +++++++++++++++++++++++++++++++++++++++')
            # print(row['listing_url'])
            # print('5. +++++++++++++++++++++++++++++++++++++++')
            payload = "/room{\"room_id\":\"" + str(row['id']) + "\"}"
        
            newobj={
                    "title": row['name'],
                    "subtitle": row['name'],
                    "image_url": row['picture_url'],
                    "buttons": [ 
                        {
                        "title": "View",
                        "url": row['listing_url'],
                        "type": "web_url"
                        # "type": "postback",
                        # "payload":payload
                        },
                        {
                        "title": "View More",
                        # "url": row['listing_url'],
                        # "type": "web_url"
                        "type": "postback",
                        "payload":payload
                        },
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

        print('message')
        # print(message)
        dispatcher.utter_message(attachment=message)

        # dispatcher.utter_message(text="Hello World!")

        return []
