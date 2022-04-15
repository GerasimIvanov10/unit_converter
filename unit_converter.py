convert = {"km_to_m": lambda x: x * 1000,
           "m_to_km": lambda x: x / 1000,
           "cm_to_m": lambda x: x / 100,
           "CtoF": lambda x: x * 1.8 + 32
}

some_distance_in_key = float(input())
converted_distance = convert["CtoF"](some_distance_in_key)

print(converted_distance)