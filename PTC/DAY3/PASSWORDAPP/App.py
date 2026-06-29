import streamlit as st
st.title("Password Analyser")
password=st.text_input("Enter password type",type="password")
#st.button("Validate")
if st.button("validate"):
    upper=lower=digit=special=False
    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        else:
            special=True
    if len(password)>=8 and upper and lower and digit and special:
        st.success("Strong password")
    else:
        st.error("Invalid")
    if len(password)<8:
        st.write("needs 8 characters")
    if not upper:
        st.write("needs an uppercase")
    if not lower:
        st.write("needs a lowercase")
    if not digit:
        st.write("needs a digit")
    if not special:
        st.write("needs a special character")