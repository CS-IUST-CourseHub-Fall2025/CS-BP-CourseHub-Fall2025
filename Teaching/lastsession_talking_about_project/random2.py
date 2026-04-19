# # partabe tas
# import random

# def tas():
#     tas1 = random.randint(1, 6)
#     tas2 = random.randint(1, 6)
#     total = tas1 + tas2
    
#     print(f"Tas andakhti: {tas1} va {tas2}")
#     print(f"Jam-e tas: {total}")
    
#     if tas1 == tas2:
#         print("Jayeze! Tas jofte, dobare bayad bendazi (Double Roll)!")
    
#     return total, (tas1 == tas2)

# natije, jofte = tas() 









# #karte shans

# import json
# import random

# chance_cards_json = """
# [
#     {"id": 1, "text": "Boro be khane aval (200$ daryaft kon)", "action": "move", "value": 0},
#     {"id": 2, "text": "Jarimeye sorat: 15$ bedeh", "action": "money", "value": -15},
#     {"id": 3, "text": "Boro be khane Illinois Avenue", "action": "move", "value": 24},
#     {"id": 4, "text": "Bank be shoma 50$ daryafti dad", "action": "money", "value": 50},
#     {"id": 5, "text": "Boro be Zendan (Jail)", "action": "move", "value": 10}
# ]
# """

# def pick_chance_card():
#     cards = json.loads(chance_cards_json)
    
#     selected_card = random.choice(cards)
    
#     print("\n" + "*"*30)
#     print(f"karte shans: {selected_card['text']}")
#     print("*"*30 + "\n")
    
#     return selected_card

# # --- Mesale Ejrayi ---
# card = pick_chance_card()

# # Logic baraye emale natije:
# # if card['action'] == "money":
# #     player_money += card['value']
# # elif card['action'] == "move":
# #     player_position = card['value']