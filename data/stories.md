## say goodbye
* goodbye
  - action_get_intent
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
  - action_get_intent
  - utter_greet
* mood_happy
  - action_get_intent
  - utter_happy
* affirm
  - action_get_intent
  - utter_question

## sad path 1
* mood_sad
  - action_get_intent
  - utter_sad

## say inquire
* inquire
  - action_get_intent
  - utter_info
  - utter_policy
* appreciate
  - action_get_intent
  - utter_thanks

## greet interuption
* greet
  - action_get_intent
  - utter_greet
* inquire
  - action_get_intent
  - utter_info
  - utter_policy
  - utter_greet_int

 ## out of bounds
 * wrongreply
  - action_get_intent
  - utter_error