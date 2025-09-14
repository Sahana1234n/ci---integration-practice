import streamlit as st

#Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate square , cube and fifth number")

#get user input
n = st.number_input("enter an integer", value=1 , step=1)

#calculate
square = n ** 2
cube = n ** 3
fifth_number = n ** 5

#Display results
st.write(f"The square of the {n} is : {square}")
st.write(f"The cube of the {n} is : {cube}")
st.write(f"The fifth number of the {n} is : {fifth_number}")