# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from collections import Counter
from datetime import datetime
from pymongo import MongoClient
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

convoList = []

class ActionGetIntent(Action):

     def name(self) -> Text:
          return "action_get_intent"

     def run(self, dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          intent= tracker.latest_message['intent'].get('name')
          sender_id = tracker.current_state()["sender_id"]
          conn= MongoClient("mongodb://localhost:27017/")
          
          db = conn.Status
          collection = db.conversations
          
          subs = "mood"
          stat = 0

          if intent == "goodbye":
              moodList = [i for i in convoList if subs in i]
              
              count = Counter(moodList)
              c1 = count['mood_happy']*0.45
              c2 = count['mood_sad']*0.20 + count['mood_depression']*0.15
              c3 = count['mood_anger']*0.25 + count['mood_disgust']*0.20
              c4 = count['mood_fear']*0.15 + count['mood_anxiety']*0.20
              
              if (c1 > c2+c3+c4):
                  stat = 1
                  
              else:
                  stat = -1
                  
            
              rec = {
                  "date":datetime.now(),
                  "status":stat
              }
              print(rec)
              collection.insert(rec)
          else:
              convoList.append(intent)
        
          return []