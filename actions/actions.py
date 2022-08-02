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
        return "action_get_suggestion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        excel_file = 'hongkong.csv'
        df = pd.read_csv(excel_file)
        mylist=[10]

        ls=df.loc[df['accommodates'].isin(mylist)]
        for index, row in ls.iterrows():
            print(row['accommodates'], row['amenities'])

        dispatcher.utter_message(text="Hello World!")

        return []
