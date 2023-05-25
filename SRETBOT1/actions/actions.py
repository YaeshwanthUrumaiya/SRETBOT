# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class Action_specific_fees(Action):
    def name(self) -> Text:
        return "Action_explain_specific_fees"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course={"aida":"2,50,000Rs for Btech and 75,00 for Bsc","aiml":"2,50,000Rs for Btech","cybsec":"2,50,000Rs","medsci":"2,50,000Rs","bioinfomatics":"75,000Rs", "da":"75,000Rs"}

        inter_c=tracker.get_slot("interested_course")
        if inter_c is not None: 
            inter_c=inter_c.lower()
        if inter_c in course:
            res = course[inter_c]
            dispatcher.utter_message(text=res)
        else:
            dispatcher.utter_message(text="Course fees information not found. Please try again")
        return[]
