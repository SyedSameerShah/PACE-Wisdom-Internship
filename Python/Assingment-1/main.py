from tkinter import ttk
import tkinter as tk

def convert():
    unit_type = drop_down_selected.get()
    value = float(input_text.get())

    if unit_type == "length":
        convert_length(value)
    elif unit_type == "mass":
        convert_mass(value)
    elif unit_type == "temperature":
        convert_temperature(value)
    elif unit_type == "time":
        convert_time(value)
    elif unit_type == "speed":
        convert_speed(value)
    elif unit_type == "energy":
        convert_energy(value)
    elif unit_type == "pressure":
        convert_pressure(value)
    

def convert_length(value):
    conv_type = drop_down_sub_selected.get()

    if conv_type == "Centimeter to Meter":
        result_text.config(text="{} cm is equal to {} m.".format(value, value / 100))
    elif conv_type == "Meter to Centimeter":
        result_text.config(text="{} m is equal to {} cm.".format(value, value * 100))
    elif conv_type == "Centimeter to INCH":
        result_text.config(text="{} cm is equal to {} inch.".format(value, value / 2.54))
    elif conv_type == "INCH to Centimeter":
        result_text.config(text="{} inch is equal to {} cm.".format(value, value * 2.54))
    elif conv_type == "Centimeter to KiloMetre":
        result_text.config(text="{} cm is equal to {} km.".format(value, value / 100000))
    elif conv_type == "KiloMetre to Centimeter":
        result_text.config(text="{} km is equal to {} cm.".format(value, value * 100000))
    elif conv_type == "Centimeter to Feet":
        result_text.config(text="{} cm is equal to {} feet.".format(value, value / 30.48))
    elif conv_type == "Feet to Centimeter":
        result_text.config(text="{} feet is equal to {} cm.".format(value, value * 30.48))
    elif conv_type == "Kilometre to Mile":
        result_text.config(text="{} KM is equal to {} mile".format(value, value / 1.609))
    elif conv_type == "Mile to Kilometre":
        result_text.config(text="{} mile is equal to {} KM".format(value, value * 1.609))

def convert_mass(value):
    conv_type = drop_down_sub_selected.get()

    if conv_type == "Gram to Kilogram":
        result_text.config(text="{} gm is equal to {} kg.".format(value, value / 1000))
    elif conv_type == "Kilogram to Gram":
        result_text.config(text="{} kg is equal to {} gm.".format(value, value * 1000))
    elif conv_type == "Kilogram to Tonne":
        result_text.config(text="{} kg is equal to {} T.".format(value, value / 1000))
    elif conv_type == "Tonne to Kilogram":
        result_text.config(text="{} T is equal to {} kg.".format(value, value * 1000))
    elif conv_type == "Milligram to Kilogram":
        result_text.config(text="{} mg is equal to {} kg.".format(value, value / 1000000))
    elif conv_type == "Kilogram to Milligram":
        result_text.config(text="{} kg is equal to {} mg.".format(value, value * 1000000))
    elif conv_type == "Milligram to Gram":
        result_text.config(text="{} mg is equal to {} gm.".format(value, value / 1000))
    elif conv_type == "Gram to Milligram":
        result_text.config(text="{} gm is equal to {} mg.".format(value, value * 1000))
    elif conv_type == "kilogram to pound":
        result_text.config(text="{} kg is equal to {} pound".format(value, value * 2.20462))
    elif conv_type == "pound to Kilogram":
        result_text.config(text="{} pound is equal to {} kg".format(value, value / 2.20462))
    elif conv_type == "Micrograms to gram":
        result_text.config(text="{} microg is equal to {} gm".format(value, value / 1e+6))
    elif conv_type == "Micrograms to Kilogram":
        result_text.config(text="{} microg is equal to {} kg".format(value, value / 1e+9))

def convert_temperature(value):
    conv_type = drop_down_sub_selected.get()

    if conv_type == "Celsius to Fahrenheit": 
        result_text.config(text="{} C is equal to {} F.".format(value, (value * 9/5) + 32))
    elif conv_type == "Celsius to Kelvin":
        result_text.config(text="{} C is equal to {} K.".format(value, value + 273.15))
    elif conv_type == "Fahrenheit to Celsius":
        result_text.config(text="{} F is equal to {} C.".format(value, (value - 32) * 5/9))
    elif conv_type == "Fahrenheit to Kelvin":
        result_text.config(text="{} F is equal to {} K.".format(value, (value - 32) * 5/9 + 273.15))
    elif conv_type == "Kelvin to Celsius":
        result_text.config(text="{} K is equal to {} C.".format(value, value - 273.15))
    elif conv_type == "Kelvin to Fahrenheit":
        result_text.config(text="{} K is equal to {} C.".format(value, (value - 273.15) * 95 + 32))

def convert_time(value):
    conv_type = drop_down_sub_selected.get()

    if conv_type == "Second to Minute": 
        result_text.config(text="{} S is equal to {} M.".format(value, value / 60))
    elif conv_type == "Minute to Second":
        result_text.config(text="{} M is equal to {} S.".format(value, value * 60))
    elif conv_type == "Second to Hour":
        result_text.config(text="{} S is equal to {} H.".format(value, value / 3600))
    elif conv_type == "Minute to Hour":
        result_text.config(text="{} M is equal to {} H.".format(value, value / 60))
    elif conv_type == "Hour to Minute":
        result_text.config(text="{} H is equal to {} M.".format(value, value * 60))
    elif conv_type == "Day to Hour":
        result_text.config(text="{} day is equal to {} H.".format(value, value * 24))
    elif conv_type == "Hour to Day":
        result_text.config(text="{} H is equal to {} day.".format(value, value / 24))

def convert_speed(value):
    conv_type = drop_down_sub_selected.get()

    if conv_type == "Mile per hour to kilometer per hour": 
        result_text.config(text="{} Ml is equal to {} Km.".format(value, value * 1.609))
    elif conv_type == "Kilometer per hour to Mile per hour":
        result_text.config(text="{} Km is equal to {} Ml.".format(value, value / 1.609))
    elif conv_type == "Mile per hour to Meter per Second":
        result_text.config(text="{} Ml is equal to {} M.".format(value, value / 2.237))
    elif conv_type == "Meter per Second to Mile per hour":
        result_text.config(text="{} M is equal to {} Ml.".format(value, value * 2.237))
    elif conv_type == "Kilometer per hour to Meter per Second":
        result_text.config(text="{} Km is equal to {} M.".format(value, value / 3.6))
    elif conv_type == "Meter per Second to Kilometer per hour":
        result_text.config(text="{} M is equal to {} Km.".format(value, value * 3.6))
    

def convert_energy(value):
    conv_type = drop_down_sub_selected.get()

    if conv_type == "Joule to Kilojoule": 
        result_text.config(text="{} J is equal to {} Kj.".format(value, value / 1000))
    elif conv_type == "Kilojoule to Joule":
        result_text.config(text="{} Kj is equal to {} J.".format(value, value * 1000))
    elif conv_type == "Joule to Kilocalorie":
        result_text.config(text="{} J is equal to {} Kc.".format(value, value / 4184))
    elif conv_type == "Kilocalorie to Joule":
        result_text.config(text="{} MKc is equal to {} J.".format(value, value * 4184))
    elif conv_type == "Kilojoule to Kilocalorie":
        result_text.config(text="{} Kj is equal to {} Kc.".format(value, value / 4.184))
    elif conv_type == "Kilocalorie to Kilojoule":
        result_text.config(text="{} Kc is equal to {} Kj.".format(value, value * 4.184))

def convert_pressure(value):
    conv_type = drop_down_sub_selected.get()

    if conv_type == "Bar to Pascal": 
        result_text.config(text="{} Bar is equal to {} P.".format(value, value * 100000))
    elif conv_type == "Bar to Std atmosphere":
        result_text.config(text="{} Bar is equal to {} atm.".format(value, value / 1.013))
    elif conv_type == "Pascal to Bar":
        result_text.config(text="{} P is equal to {} Bar.".format(value, value / 100000))
    elif conv_type == "Pascal to Std atmosphere":
        result_text.config(text="{} P is equal to {} atm.".format(value, value / 101300))
    elif conv_type == "Std atmosphere to Pascal":
        result_text.config(text="{} atm is equal to {} P.".format(value, value * 101300))
    elif conv_type == "Std atmosphere to Bar":
        result_text.config(text="{} atm is equal to {} Bar.".format(value, value * 1.013))
    
# GUI setup
window = tk.Tk()
window.title("Unit_Converter")

drop_down_menu = ttk.Label(window, text="Select Category of Convertion  :")
drop_down_menu.grid(row=0, column=0, padx=10, pady=10)

types = ["length", "mass", "temperature", "time", "speed", "energy", "pressure"]
drop_down_selected = ttk.Combobox(window, values=types)
drop_down_selected.grid(row=0, column=1, padx=10, pady=10)


drop_down_sub_menu = ttk.Label(window, text="Conversion Type  :")
drop_down_sub_menu.grid(row=1, column=0, padx=10, pady=10)

#for conditional rendering of the second dropdown based on first dropdown
drop_down_list = {
    "length": ["Centimeter to Meter", "Meter to Centimeter", "Centimeter to INCH", "INCH to Centimeter","Centimeter to KiloMetre","KiloMetre to Centimeter","Centimeter to Feet","Feet to Centimeter","Kilometre to Mile","Mile to Kilometre"],
    "mass": ["Gram to Kilogram", "Kilogram to Gram", "Kilogram to Tonne", "Tonne to Kilogram","Milligram to Kilogram","Kilogram to Milligram","Milligram to Gram","Gram to Milligram","kilogram to pound","pound to Kilogram","Micrograms to gram","Micrograms to Kilogram"],
    "temperature": ["Celsius to Fahrenheit","Celsius to Kelvin","Fahrenheit to Celsius","Fahrenheit to Kelvin","Kelvin to Celsius","Kelvin to Fahrenheit"],
    "time" : ["Second to Minute","Minute to Second","Second to Hour","Minute to Hour","Hour to Minute","Day to Hour","Hour to Day"],
    "speed" : ["Mile per hour to kilometer per hour","Kilometer per hour to Mile per hour","Mile per hour to Meter per Second","Meter per Second to Mile per hour","Kilometer per hour to Meter per Second","Meter per Second to Kilometer per hour"],
    "energy" : ["Joule to Kilojoule","Kilojoule to Joule","Joule to Kilocalorie","Kilocalorie to Joule","Kilojoule to Kilocalorie","Kilocalorie to Kilojoule"],
    "pressure" : ["Bar to Pascal","Bar to Std atmosphere","Pascal to Bar","Pascal to Std atmosphere","Std atmosphere to Pascal","Std atmosphere to Bar"]

}

drop_down_sub_selected = ttk.Combobox(window)
drop_down_sub_selected.grid(row=1, column=1, padx=10, pady=10)


input_text_lable = ttk.Label(window, text="Enter The Value  :")
input_text_lable.grid(row=2, column=0, padx=10, pady=10, sticky="w")

input_text = ttk.Entry(window)
input_text.grid(row=2, column=1, padx=10, pady=10)

convert_button = ttk.Button(window, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_text = ttk.Label(window, text="Result : ")
result_text.grid(row=4, column=0, columnspan=2, pady=10)

def update_conversion_types(event):
    selected_type = drop_down_selected.get()
    drop_down_sub_selected['values'] = drop_down_list.get(selected_type, [])

# Bind the update_conversion_types function to the <<ComboboxSelected>> event
drop_down_selected.bind("<<ComboboxSelected>>", update_conversion_types)

window.mainloop()