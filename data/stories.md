## say goodbye
* goodbye
  - utter_goodbye

## happy path 1
* greet
  - action_get_intent
  - utter_greet
* mood_happy
  - action_get_intent
  - utter_happy
* deny
  - action_get_intent
  - utter_goodbye2

## happy path 2
* greet
  - utter_greet
* mood_happy
  - utter_happy
* affirm
  - utter_question

## sad path 1
* mood_sad
 - utter_sad

## say inquire
* inquire
  - utter_info
  - utter_policy
* appreciate
  - utter_thanks

## greet interuption
* greet
 - utter_greet
* inquire
 - utter_info
 - utter_policy
 - utter_greet_int

 ## out of bounds
 * wrongreply
  - utter_error