# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ActionBookTable(Action):

    def name(self) -> str:
        return "action_book_table"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> list:

        print("call action book table \n")
        print(tracker)

        # Giả lập việc lấy các thực thể từ tracker
        number_of_people = tracker.get_slot("number_of_people")
        time = tracker.get_slot("time")

        # Tạo phản hồi
        response = f"Đã đặt bàn cho {number_of_people} người vào lúc {time}."

        # Gửi phản hồi tới người dùng
        dispatcher.utter_message(text=response)

        return []

# action_provide_quote
class ActionProvideQuote(Action):

    def name(self) -> str:
        return "action_provide_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> list:

        print("call action provice quote\n")
        route = tracker.get_slot("route")
        ready_to_load = tracker.get_slot("ready_to_load")
        transport_type = tracker.get_slot("transport_type")

        # Tạo phản hồi
        response = f"Match Price for {route} , {ready_to_load}."
        dispatcher.utter_message(text=response)
        return []

class ValidateQuoteForm(FormValidationAction):

    def name(self) -> str:
        return "validate_quote_form"

    def validate_route(self, slot_value: str, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> dict:
        """Validate `route` value."""

        if "-" in slot_value:
            # Tuyến đường hợp lệ
            return {"route": slot_value}
        else:
            dispatcher.utter_message(text="Vui lòng cung cấp tuyến đường hợp lệ theo định dạng from - to.")
            return {"route": None}  # Không thiết lập slot nếu không hợp lệ

    def validate_date(self, slot_value: str, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> dict:
        """Validate `date` value."""

        # Giả sử kiểm tra định dạng ngày hợp lệ
        if len(slot_value.split("/")) in [2, 3] or len(slot_value.split("-")) in [2, 3]:
            return {"ready_to_load": slot_value}
        else:
            dispatcher.utter_message(text="Vui lòng cung cấp ngày vận chuyển hợp lệ.")
            return {"ready_to_load": None}  # Không thiết lập slot nếu không hợp lệ