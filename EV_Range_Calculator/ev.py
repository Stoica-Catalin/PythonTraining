total_battery_capacity=62
energy_consumption=15.6

def ev_function(battery_level):  
    full_battery_range=(total_battery_capacity*100)/energy_consumption
    actual_range=(full_battery_range*battery_level)/100
    print (round(actual_range,2),"km")

ev_function(50)

    