input_unit = input()
output_unit = input()
if input_unit == "mm" and output_unit == "cm":
    number = float(input()) / 10
    print(f"{number} cm")
if input_unit == "mm" and output_unit == "m":
    number = float(input()) / 1000
    print(f"{number} m")
if input_unit == "mm" and output_unit == "km":
    number = float(input()) / 1000000
    print(f"{number} km")
if input_unit == "cm" and output_unit == "mm":
    number = float(input()) * 10
    print(f"{number} mm")
if input_unit == "cm" and output_unit == "m":
    number = float(input()) / 100
    print(f"{number} m")
if input_unit == "cm" and output_unit == "km":
    number = float(input()) / 100000
    print(f"{number} km")
if input_unit == "m" and output_unit == "mm":
    number = float(input()) * 1000
    print(f"{number} mm")
if input_unit == "m" and output_unit == "cm":
    number = float(input()) * 100
    print(f"{number} cm")
if input_unit == "m" and output_unit == "km":
    number = float(input()) / 1000
    print(f"{number} km")
if input_unit == "km" and output_unit == "mm":
    number = float(input()) * 1000000
    print(f"{number} mm")
if input_unit == "km" and output_unit == "cm":
    number = float(input()) * 100000
    print(f"{number} cm")
if input_unit == "km" and output_unit == "m":
    number = float(input()) * 1000
    print(f"{number} m")