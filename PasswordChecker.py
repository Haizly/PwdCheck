import streamlit as st 
import re # regular expression
st.set_page_config(page_title="Password Checker", layout="centered")

st.title("Is Your Password Good?")

password = st.text_input("Enter the password: ", type = "password") # type password means the entered password would be shown in *


#check length should be more than 8
if password:
    if len(password) >= 8:
        st.success("✅ Length is good")
    else:
        st.warning("❌ Password should be at least 8 characters long")


# captialzation check

if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
    st.success("✅ Contains uppercase and lowercase letters")
else:
    st.warning("❌ Must contain both uppercase and lowercase letters")


# check number
if re.search(r'[0-9]', password):
    st.success("✅ Contains a number")
else:
    st.warning("❌ Must contain a number")

# check symbol
if re.search(r'[^a-zA-Z0-9]', password ):
    st.success("✅ Contains a symbol")
else:
    st.warning("❌ Must contain a symbol")

if re.search(r'(..+?)\1', password ) or re.search(r'(.)\1{2,}', password ):
    # first check is for patterens like ababab second is for 111 
    st.warning("❌ Contains a pattern")
else:
    st.success("✅ No pattern detected")


# this function is where we detect common sequences, we have to hardcode it
def has_sequence(password):
    sequences = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'[::-1],
                 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']

    pwd_lower = password.lower() # we convert the string to lower cases
    for seq in sequences:
        for i in range(len(seq) - 3):
            if seq[i:i+4] in pwd_lower: # we check if the seqence is in fact in password
                return True
    return False

# check if theres a common patern line 123 or abc or zxcv
if has_sequence(password):
    st.warning("❌ Contains a common sequence")
else:
    st.success("✅ No obvious sequences")


# we make a strenght checker bases on the criteria met
strength_score = 0

if len(password) >= 8: strength_score += 1
if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password): strength_score += 1
if re.search(r'[0-9]', password): strength_score += 1
if re.search(r'[^a-zA-Z0-9]', password): strength_score += 1
if not re.search(r'(..+?)\1', password) and not re.search(r'(.)\1{2,}', password): strength_score += 1
if not has_sequence(password): strength_score += 1

if strength_score == 6:
    st.success("🔥 Very strong password!")
elif strength_score >= 4:
    st.info("🟡 Decent, but could be better")
else:
    st.error("🔴 Weak password")
