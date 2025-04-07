# Project:01  "Unit Converter"

import streamlit as st

def convert_units(value: float, unit_from: str, unit_to: str):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000  # 1 km = 1000 m

    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001  # 1 m = 0.001 km

    elif unit_from == "kilograms" and unit_to == "grams":
        return value * 1000  # 1 kg = 1000 g

    elif unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001  # 1 g = 0.001 kg

    else:
        return None  # Invalid conversion

# Streamlit UI
def main():
    st.title("Unit Converter")
    st.write("Welcome to the Unit Converter App!")

    value = st.number_input("Enter the value you want to convert:", min_value=0.0)

    unit_from = st.text_input("Enter the unit to convert from (meters, kilometers, grams, kilograms):")
    unit_to = st.text_input("Enter the unit to convert to (meters, kilometers, grams, kilograms):")

    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)

        if result is not None:
            st.success(f"Converted value: {result} {unit_to}")
        else:
            st.error("Conversion not supported. Please enter valid units.")

if __name__ == "__main__":
    main()

