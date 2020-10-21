## say goodbye
* goodbye
  - action_get_intent
  - utter_goodbye

## happy path
* greet
  - action_get_intent
  - utter_greet
* mood_happy
  - action_get_intent
  - utter_happy

## path 2
* greet
  - action_get_intent
  - utter_greet
* mood_sad
  - action_get_intent
  - utter_nf
* deny
  - action_get_intent
  - utter_question
* road_accident
  - action_get_intent
  - utter_inqu
* deny
  - action_get_intent
  - utter_accident

## path 2_1
* greet
  - action_get_intent
  - utter_greet
* mood_sad
  - action_get_intent
  - utter_nf
* deny
  - action_get_intent
  - utter_question
* road_accident
  - action_get_intent
  - utter_inqu
* affirm
  - action_get_intent
  - utter_inqu2
* affirm
  - action_get_intent
  - utter_seri

## path 2_2
* greet
  - action_get_intent
  - utter_greet
* mood_sad
  - action_get_intent
  - utter_nf
* road_accident
  - action_get_intent
  - utter_inqu
* deny
  - action_get_intent
  - utter_accident

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