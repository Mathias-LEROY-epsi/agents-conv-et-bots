from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class NouvelleReservation(Action):

     def name(self) -> Text:
         return "action_nouvelle_reservation"

     def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="nouvelle résa")

        return []


class AnnulerReservation(Action):

    def name(self) -> Text:
        return "action_annuler_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="annuler résa")

        return []


class InformationsReservation(Action):

    def name(self) -> Text:
        return "action_informations_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="infos")

        return []


class MenuDuJour(Action):

    def name(self) -> Text:
        return "action_menu_du_jour"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="menu")

        return []


class ListeAllergenes(Action):

    def name(self) -> Text:
        return "action_liste_allergenes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="liste")

        return []

class LienVersLaCarte(Action):

    def name(self) -> Text:
        return "action_lien_vers_la_carte"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="carte")

        return []
