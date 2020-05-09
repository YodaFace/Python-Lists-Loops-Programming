parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:

def get_parking_lot(): 
    total_slots = []
    available_slots = []
    occupied_slots = []
    for slots in parking_state:
        for status in slots:
            print(status)
            # print(type(status))
            if status == 1:
                occupied_slots =+ 1
        # print(status)
    print("Now the occupied slots")
    print(occupied_slots)

get_parking_lot()