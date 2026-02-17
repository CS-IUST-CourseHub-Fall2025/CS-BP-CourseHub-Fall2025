parking_slots = {"F1": [0,0,0],
                 "F2": [0,0,0],
                 "F3": [0,0,0]}
cars_dict = {}
fee = 10

def enter_car(id, entry_date):
    global cars_dict
    global parking_slots
    
    car_info = {"entry_date": entry_date,
                "parking_slot": ""}
    
    for floor in parking_slots.keys():
        for slot in range(len(parking_slots[floor])):
            if parking_slots[floor][slot] == 0:
                parking_slots[floor][slot] = id
                car_info["parking_slot"] = f"{floor}S{slot+1}"
                cars_dict[id] = car_info
                return f"car {id} is parked in {car_info["parking_slot"]}"
            
    return "parking lot is full!"

def exit_car(id, exit_date):
    global cars_dict
    global parking_slots

    if id in cars_dict.keys():
        
        for floor in parking_slots.keys():
            for slot in range(len(parking_slots[floor])):
                if parking_slots[floor][slot] == id:
                    parking_slots[floor][slot] = 0
        
        entry_date = cars_dict[id]["entry_date"]
        parking_slot = cars_dict[id]["parking_slot"]        
        cars_dict.pop(id)
        
        return f"parked in {parking_slot} with the fee of {calculate_fee(entry_date, exit_date)}$"
        
    return "no such a car in the parking lot!"

def calculate_fee(entry_date, exit_date):
    global fee
    return fee * (exit_date - entry_date)
    
    
commands = []

while True:
    line = input().strip()
    if line == "EOF":
        break
    if line == "":
        continue
    commands.append(line)


for cmd in commands:
    parts = cmd.split()
    order = parts[0]
    id = parts[1]
    date = int(parts[2])

    if order == "enter":
        print(enter_car(id, date))
    elif order == "exit":
        print(exit_car(id, date))
