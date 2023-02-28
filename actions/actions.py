'''

        List of all the custom actions that are created :
            action_session_id
            action_save_user_data
            validate_new_user_registration
            action_refill_firstname
            action_refill_lastname
            action_refill_emailid
            action_refill_mobilenumber
            action_submit_user_query
            action_faq_list
            action_ask_query_confirmation

'''



'''

Importing necessary libraries

'''


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted, FollowupAction, AllSlotsReset


import json
import os
import random
import re





'''

Code Begins

'''


####    Generating a SESSION ID for users   ####

class SessionID(Action):
    def name(self) -> Text:
        return "action_session_id"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        conversation_id = tracker.sender_id
        
        dispatcher.utter_message(f"The Conversation ID is {conversation_id}")
        


####    Refilling NEW USER details in slot      ####

class UpdateUserFirstName(Action):
    def name(self) -> Text:
        return "action_refill_first_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        updated_first_name = tracker.get_slot('refill_first_name_sl')
        return [SlotSet('first_name', updated_first_name)]

class UpdateUserLastName(Action):
    def name(self) -> Text:
        return "action_refill_last_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        updated_last_name = tracker.get_slot('refill_last_name_sl')
        return [SlotSet('last_name', updated_last_name)]

class UpdateUserEmailID(Action):
    def name(self) -> Text:
        return "action_refill_email_address"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        updated_email_id = tracker.get_slot('refill_email_address_sl')
        return [SlotSet('email_address', updated_email_id)]

class UpdateUserMobileNumber(Action):
    def name(self) -> Text:
        return "action_refill_mobile_number"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        updated_mobile_number = tracker.get_slot('refill_mobile_number_sl')
        return [SlotSet('mobile_number', updated_mobile_number)]

#### RESETTING ALL THE SLOT OF THE USER DETAILS FORM

class ResetSlotFirstName(Action):
    def name(self) -> Text:
        return "action_reset_sl_first_name"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("refill_first_name_sl", None)]

class ResetSlotLastName(Action):
    def name(self) -> Text:
        return "action_reset_sl_last_name"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("refill_last_name_sl", None)]
    
class ResetSlotEmailAddress(Action):
    def name(self) -> Text:
        return "action_reset_sl_email_address"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("refill_email_address_sl", None)]

class ResetSlotMobileNumber(Action):
    def name(self) -> Text:
        return "action_reset_sl_mobile_number"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("refill_mobile_number_sl", None)]



####    Refilling SLOTS for Booking CAR SERVICE   ####

class UpdateBookingDetailsCarModelName(Action):
    def name(self) -> Text:
        return "action_refill_car_model_name"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        update_car_model_name = tracker.get_slot("refill_car_model_name_sl")
        return [SlotSet("car_model_sl", update_car_model_name)]

class UpdateBookingDetailsCarNumber(Action):
    def name(self) -> Text:
        return "action_refill_car_number"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        update_car_number = tracker.get_slot("refill_car_number_sl")
        return [SlotSet("car_number_sl", update_car_number)]

class UpdateBookingDetailsApproxKM(Action):
    def name(self) -> Text:
        return "action_refill_approximate_kilometers"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        update_approximate_kilometers = tracker.get_slot("refill_approximate_kilometers_sl")
        return [SlotSet("approx_km_driven_sl", update_approximate_kilometers)]

class UpdateBookingDetailsUserName(Action):
    def name(self) -> Text:
        return "action_refill_user_name"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        update_user_name = tracker.get_slot("refill_service_user_name_sl")
        return [SlotSet("service_user_name_sl", update_user_name)]

class UpdateBookingDetailsMobileNumber(Action):
    def name(self) -> Text:
        return "action_refill_booking_mobile_number"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        update_user_name = tracker.get_slot("refill_service_mobile_number_sl")
        return [SlotSet("service_mobile_number_sl", update_user_name)]


###     RESETTING THE REFILLED SLOTS FOR BOOKING

class ResetBookingSlotsName(Action):
    def name(self) -> Text:
        return "action_reset_booking_slots_car_model"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("refill_car_model_name_sl", None)]

class ResetBookingSlotsNumber(Action):
    def name(self) -> Text:
        return "action_reset_booking_slots_car_number"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("refill_car_number_sl", None)]


class ResetBookingSlotsApproximateKM(Action):
    def name(self) -> Text:
        return "action_reset_booking_slots_approximate_km"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("refill_approximate_kilometers_sl", None)]
    
class ResetBookingSlotsUserName(Action):
    def name(self) -> Text:
        return "action_reset_booking_slots_user_name"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("refill_service_user_name_sl", None)]
    
class ResetBookingSlotsMobileNumber(Action):
    def name(self) -> Text:
        return "action_reset_booking_slots_mobile_number"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("refill_service_mobile_number_sl", None)]
    

####    Refilling Slots in USER QUERY FORM  ####

class UpdateUserQueryUserDetailsUserName(Action):
    def name(self) -> Text:
        return "action_refill_query_user_name"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        update_query_user_name = tracker.get_slot("query_name_refill_sl")

        return [SlotSet("user_name_need_help_sl", update_query_user_name)]


class UpdateUserQueryUserDetailsMobileNumber(Action):
    def name(self) -> Text:
        return "action_refill_query_mobile_number"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        update_query_mobile_number = tracker.get_slot("query_mobile_number_refill_sl")

        return [SlotSet("mobile_number_need_help_sl", update_query_mobile_number)]


#### RESETTING THE USER QURY SLOTS  
class ResetQueryDetailsUserName(Action):
    def name(self) -> Text:
        return "action_reset_slot_query_user_name"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("query_name_refill_sl", None)]

class ResetQueryDetailsMobileNumber(Action):
    def name(self) -> Text:
        return "action_reset_slot_query_mobile_number"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("query_mobile_number_refill_sl", None)]

###     VALIDATING THE EXISTING USER ENTERED MOBILE NUMBER FROM DATABASE    ###

class CheckExistingUserMobileNumber(Action):
    def name(self) -> Text:
        return "action_validating_mobile_number"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[List, Any]) -> List[Dict[Text, Any]]:
        filename = "user_data.json"
        filepath = "./actions/"
        file = filepath + filename
        with open(file, "r") as f:
            data = json.load(f)

        match_found = False
        for user_details in data["user_details"]:
            if user_details.get("Mobile Number") == tracker.get_slot("existing_customer_mobile_number_sl"):
                match_found = True
                break
        first_name = user_details.get("First Name")
        last_name = user_details.get("Last Name")
        if match_found:
            buttons = [{'title': 'KIA Sonet', 'payload': '/kia_sonet'},
            {'title': 'KIA Seltos', 'payload': '/kia_seltos'},
            {'title': 'KIA Carnival', 'payload': '/kia_carnival'}]
            dispatcher.utter_message(text=f"Welcome back! {first_name} {last_name}.\nWe have the following cars available in our showroom right now.", buttons=buttons, button_type = 'vertical')

        if not match_found:
            buttons = [{'title': 'Back', 'payload': '/back_to_mm'}]
            dispatcher.utter_message(text="We could not find any user with that mobile number, please check your mobile number or create a new account.", buttons=buttons)
        
### Resetting the existing user mobile number slot

class ResetSlotExistingUserMobileNumber(Action):
    def name(self) -> Text:
        return "action_reset_slot_existing_mobile_number"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("existing_customer_mobile_number_sl", None)]



# Saving the user details into slot values within a json file -   

class UserDataJSON(Action):
    def name(self) -> Text:
        return "action_save_user_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        first_name = tracker.get_slot("first_name")
        last_name = tracker.get_slot("last_name")
        email_address = tracker.get_slot("email_address")
        mobile_number = tracker.get_slot("mobile_number")

        # Create the user data dictionary
        user_data = {
            "First Name": first_name,
            "Last Name": last_name,
            "Email Address": email_address,
            "Mobile Number": mobile_number
        }

        # Define the filename and path where the json file will be saved
        filename = "user_data.json"
        filepath = "./actions/"
        file = filepath + filename

        # Create the json file if it does not exist
        if not os.path.exists(file):
            with open(file, "w") as f:
                json.dump({"user_details": []}, f)
        
        # Append the user data to the json file
        with open(file, "r+") as f:
            data = json.load(f)
            data["user_details"].append(user_data)
            f.seek(0)
            json.dump(data, f, indent=4)



# Saving the user input into the slot --- Help Me ---
class SaveUserQuery(Action):
    def name(self) -> Text:
        return "action_save_user_query"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_query_sl = tracker.latest_message.get('text')
        return [SlotSet("user_help_query", user_query_sl)]


# Saving the user help query into the json file :
class UserHelpQuery(Action):
    def name(self) -> Text:
        return "action_submit_user_query"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict [Text, Any]]:
        user_query = tracker.get_slot("need_help_sl")
        user_name = tracker.get_slot("user_name_need_help_sl")
        mobile_number = tracker.get_slot("mobile_number_need_help_sl")
        compalaint_id = str((random.randint(100000,999999)))
        user_query_data = {
            "Name": user_name,
            "Mobile Number": mobile_number,
            "User Query": user_query,
            "Querry ID": compalaint_id,
            "Status" : "Active"
        }
        # Define the filename and path where the json file will be saved
        filename = "user_data.json"
        filepath = "./actions/"
        file = filepath + filename

        # Create the json file if it does not exist
        if not os.path.exists(file):
            with open(file, "w") as f:
                json.dump({"user_query": []}, f)
        
        # Append the user data to the json file
        with open(file, "r+") as f:
            data = json.load(f)
            data["user_query"].append(user_query_data)
            f.seek(0)
            json.dump(data, f, indent=4)
        dispatcher.utter_message(text = f"Your query has been logged successfully. Your Query ID is  {compalaint_id}. Please keep checking your inbox our support executive will contact you soon.")



###         SAVING THE BOOKING DETAILS INTO THE JSON FILE           ###

class BookingDetails(Action):
    def name(self) -> Text:
        return "action_save_booking_details"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        car_model = tracker.get_slot("car_model_sl")
        car_number = tracker.get_slot("car_number_sl")
        approx_km = tracker.get_slot("approx_km_driven_sl")
        user_name = tracker.get_slot("service_user_name_sl")
        mobile_number = tracker.get_slot("service_mobile_number_sl")
        appointment_number = str(random.randint(100000,999999))

        booking_data = {
            "Car Model": car_model,
            "Car Number": car_number,
            "Approximate Kilometers": approx_km,
            "User Name": user_name,
            "Mobile Number": mobile_number,
            "Appointment Number": appointment_number,
            "Status": "Active"
        }
        # Define the filename and path where the json file will be saved
        filename = "car_service_booking.json"
        filepath = "./actions/"
        file = filepath + filename

        # Create the json file if it does not exist
        if not os.path.exists(file):
            with open(file, "w") as f:
                json.dump({"car_service_booking": []}, f)
        
        # Append the user data to the json file
        with open(file, "r+") as f:
            data = json.load(f)
            data["car_service_booking"].append(booking_data)
            f.seek(0)
            json.dump(data, f, indent=4)

        dispatcher.utter_message(text=f"Your service booking is confirmed and your appointment number is {appointment_number}.")



####        Checking the status of the service              ####

class ServiceStatusCheck(Action):
    def name(self) -> Text:
        return "action_check_status"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        filename = "user_data.json"
        filepath = "./actions/"
        file = filepath + filename
        with open(file, "r") as f:
            data = json.load(f)

        match_found = False
        for user_details in data["user_query"]:
            if user_details.get("Querry ID") == tracker.get_slot("status_sl"):
                match_found = True
                break
        service_status = user_details.get("Status")
        first_name = user_details.get("Name")
        if match_found:
            dispatcher.utter_message(text=f"Welcome {first_name}\nQuery Status : {service_status}")
        if not match_found:
            dispatcher.utter_message(text="We could not find any query number that you provided, kindly check your appointment number and try again.")
        
        # buttons = [{"title": "Check another query status", "payload": "/change_status_id"}]
        # dispatcher.utter_message(text="Want to check another query status?",buttons=buttons, button_type = 'vertical')
        # return []


###     RESETTING ALL THE SLOTS FILLED AFTER FORM COMPLETION

class ResetAllSlots(Action):
    def name(self) -> Text:
        return "action_reset_all_slots"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text,Any]) -> List[Dict[Text, Any]]:
        return [AllSlotsReset()]






















'''

                                    DISPOSAL

'''



#### Refilling the Service Booking Details slots


# ### Car Model Name

# class RefillServiceBookingDetailsCarModelName(Action):
#     def name(self) -> Text:
#         return "action_refill_service_car_model"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         updated_car_model_name = tracker.get_slot("refill_car_model_name_sl")

#         return [SlotSet("car_model_sl", updated_car_model_name)]
    

# ### Car Number

# class RefillServiceBookingDetailsCarModelName(Action):
#     def name(self) -> Text:
#         return "action_refill_service_car_number"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         updated_car_number = tracker.get_slot("refill_car_number_sl")

#         return [SlotSet("car_number_sl", updated_car_number)]
    

# ### Approximate Driven

# class RefillServiceBookingDetailsCarModelName(Action):
#     def name(self) -> Text:
#         return "action_refill_service_approximate_kilometers"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         updated_approximate_kilometers = tracker.get_slot("refill_approximate_kilometers_sl")

#         return [SlotSet("approx_km_driven_sl", updated_approximate_kilometers)]
    
# ### User Name

# class RefillServiceBookingDetailsCarModelName(Action):
#     def name(self) -> Text:
#         return "action_refill_service_user_name"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         updated_user_name = tracker.get_slot("refill_service_user_name_sl")

#         return [SlotSet("service_user_name_sl", updated_user_name)]
    

# ### Mobile Number

# class RefillServiceBookingDetailsCarModelName(Action):
#     def name(self) -> Text:
#         return "action_refill_service_mobile_number"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         updated_mobile_number_service = tracker.get_slot("mobile_number_refill_sl")

#         return [SlotSet("service_mobile_number_sl", updated_mobile_number_service)]
    

# # Saving the user input into the slot --- Suspension ---
# class SaveUserQuerySuspension(Action):
#     def name(self) -> Text:
#         return "action_save_user_query_suspension"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_query_sl = tracker.latest_message.get('text')
#         return [SlotSet("user_server_query", user_query_sl)]


# # Saving the user help query into the json file :
# class UserHelpQuerySuspension(Action):
#     def name(self) -> Text:
#         return "action_submit_user_query_suspension"
    
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict [Text, Any]]:
#         user_query = tracker.get_slot("user_server_query")
#         compalaint_id = (random.randint(100000,999999))
#         user_query_data = {
#             "User Query": user_query,
#             "Complaint ID": compalaint_id
#         }
#         # Define the filename and path where the json file will be saved
#         filename = "user_data.json"
#         filepath = "./actions/"
#         file = filepath + filename

#         # Create the json file if it does not exist
#         if not os.path.exists(file):
#             with open(file, "w") as f:
#                 json.dump({"user_query": []}, f)
        
#         # Append the user data to the json file
#         with open(file, "r+") as f:
#             data = json.load(f)
#             data["user_query"].append(user_query_data)
#             f.seek(0)
#             json.dump(data, f, indent=4)
#         dispatcher.utter_message(text = f"Your query has been logged successfully. Your Query ID is  {compalaint_id}. Please keep checking your inbox our support executive will contact you soon.")



# # Saving the user input into the slot --- Engine ---
# class SaveUserQueryEngine(Action):
#     def name(self) -> Text:
#         return "action_save_user_query_engine"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_query_sl = tracker.latest_message.get('text')
#         return [SlotSet("user_website_query", user_query_sl)]



# # Saving the user help query into the json file :
# class UserHelpQueryEngine(Action):
#     def name(self) -> Text:
#         return "action_submit_user_query_engine"
    
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict [Text, Any]]:
#         user_query = tracker.get_slot("user_website_query")
#         compalaint_id = (random.randint(100000,999999))
#         user_query_data = {
#             "User Query": user_query,
#             "Complaint ID": compalaint_id
#         }
#         # Define the filename and path where the json file will be saved
#         filename = "user_data.json"
#         filepath = "./actions/"
#         file = filepath + filename

#         # Create the json file if it does not exist
#         if not os.path.exists(file):
#             with open(file, "w") as f:
#                 json.dump({"user_query": []}, f)
        
#         # Append the user data to the json file
#         with open(file, "r+") as f:
#             data = json.load(f)
#             data["user_query"].append(user_query_data)
#             f.seek(0)
#             json.dump(data, f, indent=4)
#         dispatcher.utter_message(text = f"Your query has been logged successfully. Your Query ID is  {compalaint_id}. Please keep checking your inbox our support executive will contact you soon.")



# # Saving the user input into the slot --- Interior ---
# class SaveUserQueryInterior(Action):
#     def name(self) -> Text:
#         return "action_save_user_query_interior"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_query_sl = tracker.latest_message.get('text')
#         return [SlotSet("user_application_query", user_query_sl)]



# # Saving the user help query into the json file :
# class UserHelpQueryInterior(Action):
#     def name(self) -> Text:
#         return "action_submit_user_query_interior"
    
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict [Text, Any]]:
#         user_query = tracker.get_slot("user_application_query")
#         compalaint_id = (random.randint(100000,999999))
#         user_query_data = {
#             "User Query": user_query,
#             "Complaint ID": compalaint_id
#         }
#         # Define the filename and path where the json file will be saved
#         filename = "user_data.json"
#         filepath = "./actions/"
#         file = filepath + filename

#         # Create the json file if it does not exist
#         if not os.path.exists(file):
#             with open(file, "w") as f:
#                 json.dump({"user_query": []}, f)
        
#         # Append the user data to the json file
#         with open(file, "r+") as f:
#             data = json.load(f)
#             data["user_query"].append(user_query_data)
#             f.seek(0)
#             json.dump(data, f, indent=4)
#         dispatcher.utter_message(text = f"Your query has been logged successfully. Your Query ID is  {compalaint_id}. Please keep checking your inbox our support executive will contact you soon.")



# # Saving the user input into the slot --- Brake ---
# class SaveUserQueryBrake(Action):
#     def name(self) -> Text:
#         return "action_save_user_query_brake"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_query_sl = tracker.latest_message.get('text')
#         return [SlotSet("user_other_query", user_query_sl)]



# # Saving the user help query into the json file :
# class UserHelpQueryBrake(Action):
#     def name(self) -> Text:
#         return "action_submit_user_query_brake"
    
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict [Text, Any]]:
#         user_query = tracker.get_slot("user_other_query")
#         compalaint_id = (random.randint(100000,999999))
#         user_query_data = {
#             "User Query": user_query,
#             "Complaint ID": compalaint_id
#         }
#         # Define the filename and path where the json file will be saved
#         filename = "user_data.json"
#         filepath = "./actions/"
#         file = filepath + filename

#         # Create the json file if it does not exist
#         if not os.path.exists(file):
#             with open(file, "w") as f:
#                 json.dump({"user_query": []}, f)
        
#         # Append the user data to the json file
#         with open(file, "r+") as f:
#             data = json.load(f)
#             data["user_query"].append(user_query_data)
#             f.seek(0)
#             json.dump(data, f, indent=4)
#         dispatcher.utter_message(text = f"Your query has been logged successfully. Your Query ID is  {compalaint_id}. Please keep checking your inbox our support executive will contact you soon.")



####    Action for FAQ list     ###

# class FAQList(Action):
#     def name(self) -> Text:
#         return "action_faq_list"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         buttons = [{"title": "What is the difference between a formal and an informal complaint?", "payload": "/formal_informal"},
#         {"title": "Who can file a complaint with Employee Relations?", "payload": "/who_can_file"},
#         {"title": "Will I get in trouble for filing a complaint?", "payload": "/trouble"},
#         {"title": "If I file a formal complaint with Employee Relations, can I still file a grievance?", "payload": "/file_grievence"}]

#         dispatcher.utter_message(text="Following are few FAQs that might help you : ", buttons=buttons, button_type='vertical')



# Checking if the mobile number starts with 6,7,8,9 and is of 10-digit length

# class NewUserRegistration(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_new_user_registration"

#     def validate_mobile_number(self, value, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
#         if not (value.startswith("6") or value.startswith("7") or value.startswith("8") or value.startswith("9")) or len(value) != 10:
#             dispatcher.utter_message(text = "Please enter a valid mobile number.")





### Action to ask for User Query Confirmation ###

# class UserQuery(Action):
#     def name(self) -> Text:
#         return "action_ask_query_confirmation"

#     def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_help_query = tracker.get_slot("user_help_query")
#         buttons = [{"title":"Yes", "payload":"/confirm_user_help"},
#         {"title": "No", "payload": "/reject_user_help"}]
#         dispatcher.utter_message(text=f"You have entered the following as your query :\n\n{user_help_query}\n\nThis query will be submitted to our sytem. Our team will reach back to you soon.", buttons=buttons)

