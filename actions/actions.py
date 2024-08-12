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

from rasa_sdk import Action, Tracker
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