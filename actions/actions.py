# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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


from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionAskForFiles(Action):
    def name(self):
        return "action_ask_for_files"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Please provide the necessary files for testing.")
        return []

class ActionPerformTesting(Action):
    def name(self):
        return "action_perform_testing"

    def run(self, dispatcher, tracker, domain):
        # Simulate a response from a testing API
        testing_report = """
        Testing completed:
        - Unit tests passed: 15/15
        - Performance: Optimal
        """

        # Send the simulated testing report back to the user
        dispatcher.utter_message(text=testing_report)
        return []

