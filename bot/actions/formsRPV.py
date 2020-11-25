from typing import Dict, Text, Any, List, Union, Optional
import logging
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
)

#logger = logging.getLogger(__name__)

class CpfForm(FormAction):
    """Pay credit card form..."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "cpf_form"
 
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["cpf", "confirm"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "cpf":
                self.from_entity(entity="cpf"),
            "confirm": [
                self.from_intent(value=True, intent="afirmar"),
                self.from_intent(value=False, intent="negar"),
            ],
        }

   # def validate_cpf(
   #     self,
   #     value: Text,
   #     dispatcher: CollectingDispatcher,
   #     tracker: Tracker,
   #     domain: Dict[Text, Any],
   # ) -> Dict[Text, Any]:
   #     """Validate cpf value."""

        #cpf = tracker.get_slot("cpf")
        
        #try:    
        #    return cpf
        #except (TypeError, AttributeError):
        #    pass
    #    pass

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        #cpf = tracker.get_slot("cpf")    
        
        #SlotSet("cpf", "1234")
        cpf = tracker.get_slot("cpf")

        if tracker.get_slot("confirm"):
            #dispatcher.utter_message(template="utter_cpf_confirmed")
            dispatcher.utter_message("Confirmado, recuperado CPF: {}".format(cpf))
        else:
            #dispatcher.utter_message(template="utter_cpf_cancelled")
            dispatcher.utter_message("Cancelado, porém recuperado CPF: {}".format(cpf))
        return []