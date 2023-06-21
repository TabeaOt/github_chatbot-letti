# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionCountIntent(Action):
	def name(self):
		return 'action_count_intent'

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


		intent = str(tracker.get_intent_of_latest_message())

		if  intent == 'was_sepsiserreger': 
			count = float(tracker.get_slot("num_intent_sepsiserreger")) + 1
			return [SlotSet("num_intent_sepsiserreger", count)]
		elif  intent == 'welche_risikofaktoren':
			count = float(tracker.get_slot("num_intent_risikofaktoren")) + 1
			return [SlotSet("num_intent_risikofaktoren", count)]
		elif  intent == 'welche_spaetfolgen':
			count = float(tracker.get_slot("num_intent_spaetfolgen")) + 1
			return [SlotSet("num_intent_spaetfolgen", count)]
		else:  return []

class ActionErrorSepsiserreger(Action):
	def name(self):
		return 'action_error_sepsiserreger'

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		slot = tracker.get_slot("num_intent_sepsiserreger")
		if slot < 2:
			dispatcher.utter_message(text="error message") # apology / no aplogy
			dispatcher.utter_message(buttons=[
				{'title': "Was sind Sepsiserreger?", 'payload': '/was_sepsiserreger'}, # give options / no options
		        {'title': "Was ist eine Sepsis", 'payload': '/was_sepsis'}])
		else:
			dispatcher.utter_message("Die häufigsten Sepsiserreger sind Bakterien. Am häufigsten gehen bakterielle Infektionen der Atemwege, des Verdauungstrakts und des Urogenitaltrakts mit einer Sepsis einher, Risikofaktoren sind Alter, Abwehrschwäche, Vorerkrankung und Eingriffe in den Körper, der Erregern als Eintrittspforte dient. Aber grundsätzlich kann jede bakterielle Infektion in eine Sepsis münden.")
		return []
	
class ActionErrorRisikofaktoren(Action):
	def name(self):
		return 'action_error_risikofaktoren'

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		slot = tracker.get_slot("num_intent_risikofaktoren")
		if slot < 2:
			dispatcher.utter_message(text="error message") # apology / no aplogy
			dispatcher.utter_message(buttons=[
				{'title': "Welche Spätfolgen gibt es?", 'payload': '/welche_spaetfolgen'}, # give options / no options
		        {'title': "Was sind die Risikofaktoren?", 'payload': '/welche_risikofaktoren'}])
		else:
			dispatcher.utter_message(text="Risikofaktoren sind Alter, Abwehrschwäche, Vorerkrankung und Eingriffe in den Körper, der Erregern als Eintrittspforte dient.")
		return []

class ActionErrorSpaetfolgen(Action):
	def name(self):
		return 'action_error_spaetfolgen'

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		slot = tracker.get_slot("num_intent_spaetfolgen")
		if slot < 2:
			dispatcher.utter_message(text="error message") # apology / no aplogy
			dispatcher.utter_message(buttons=[
				{'title': "Welche Spätfolgen gibt es?", 'payload': '/welche_spaetfolgen'}, # give options / no options
		        {'title': "Was sind die Risikofaktoren?", 'payload': '/welche_risikofaktoren'}])
		else:
			dispatcher.utter_message(text="Wenn der Patient die Sepsis überlebt, hat er häufig unter Spätfolgen wie Gedächtnisstörungen , eingeschränktem Lernvermögen, Depression, Angst- und Schlafstörungen, Leistungsminderung, Nervenschmerzen (Polyneuropathie) und Schmerzen zu leiden.")
		return []
