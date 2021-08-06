#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
from PIL import Image
import random


# # Web app initializing

# In[2]:


if 'total' not in st.session_state:
    st.session_state['total'] = 300

if 'coin_attempt' not in st.session_state:
    st.session_state['coin_attempt'] = 1
    
if 'dice_attempt' not in st.session_state:
    st.session_state['dice_attempt'] = 1
    
if 'next_level' not in st.session_state:
    st.session_state['next_level'] = False


# In[3]:


st.header("Mind Game")
st.write("Professional Practise Experiment- Group 3")


# In[4]:


img=Image.open("main.png")


# In[5]:


st.image(img,width=400)


# In[7]:





# In[ ]:


st.sidebar.subheader(f"Current Coin Balance Rs. {st.session_state.total}")
st.sidebar.subheader("Rules - Leve 01")
st.sidebar.markdown("- **Level 01** is necesaary to complete")
st.sidebar.markdown("- You will be given **Rs.300** worth cooins at the begining for level 01")
st.sidebar.markdown("- For any fail attempt in Level 01, you will loose **Rs.100** worth coins from given Rs. 300")
st.sidebar.subheader("Rules - Leve 01")
st.sidebar.markdown("- You can continue to **Level 02** If you like. Cion balance will be increased by **Rs.600** at the begining of Level 02")
st.sidebar.markdown("- For any fail attempt in Level 02, you will loose **Rs.200** worth coins from given Rs.600")
st.sidebar.markdown("- At a sucessfull completion. All remaining coins will be rewarded in cash!")


# In[11]:


def coin_ui():
    st.subheader("Level 01: Toss a coin")
    st.markdown("- You have 3 attemps to toss the coin.")
    st.markdown("- To win each attempt you need to get **HEAD**.")
    if st.session_state.coin_attempt < 4:
        st.write(f"Attempt: {st.session_state.coin_attempt}")
        if st.session_state.coin_attempt == 1:
            attempt_button = st.button ("Attempt Now")
        else:
             attempt_button = st.button ("Attempt Again")
        if attempt_button:
            res = random.choice(['Head','Tail'])
            st.markdown(f"Tos Result: **{res}**")
            st.markdown("![coin toss](https://acegif.com/wp-content/gifs/coin-flip-41.gif)")
            st.session_state[f'coin_attempt_result_{st.session_state.coin_attempt}'] = res
            st.session_state.coin_attempt = st.session_state.coin_attempt +1
            if res == "Tail":
                st.session_state.total = st.session_state.total - 100
    else:
        st.write("All Toss Coin attempts are used!")
        for at in range(1,st.session_state.coin_attempt):
            if f'coin_attempt_result_{at}' in st.session_state:
                st.write(f"Attemt {at} : You're toss result': {st.session_state[f'coin_attempt_result_{at}']}")
        st.session_state.coin_attempt = st.session_state.coin_attempt +1
        st.write("Remeber your Choices to Submit the form!")
        st.markdown("- You have the freedom to provide any answer! Remeber: If an attempt is **Tail** you will loose **Rs. 100** from given coins")


# In[ ]:


def dice_ui():
    st.subheader("Level 02: Roll a dice")
    st.markdown("- You have 3 attemps to roll the dice.")
    st.markdown("- To win each attempt you need to get **a Value grater than 3**.")
    if st.session_state.dice_attempt < 4:
        st.write(f"Attempt: {st.session_state.dice_attempt}")
        if st.session_state.dice_attempt == 1:
            attempt_button = st.button ("Attempt Now")
        else:
             attempt_button = st.button ("Attempt Again")
        if attempt_button:
            res = random.choice([1,2,3,4,5,6])
            st.markdown(f"Dice rolled Result: **{res}**")
            st.markdown("![dice roll](https://lh3.googleusercontent.com/proxy/-d87aGFDf6aSzTVF49SEv4tUU2bZElENwPTenESEyNV9GoPR6M0bYewA6_nAHD9vwT9wLBncQh0oYo8CceNC_AcXYIzYqo0)")
            st.session_state[f'dice_attempt_result_{st.session_state.dice_attempt}'] = res
            st.session_state.dice_attempt = st.session_state.dice_attempt +1
            if res < 3:
                st.session_state.total = st.session_state.total - 100
    else:
        st.write("All Dice rolling attempts are used!")
        for at in range(1,st.session_state.dice_attempt):
            if f'dice_attempt_result_{at}' in st.session_state:
                st.write(f"Attempt {at} : You'r dice result': {st.session_state[f'dice_attempt_result_{at}']}")
        st.write(f"Your Final Coin Balance: Rs. {st.session_state.total}")
        st.session_state.dice_attempt = st.session_state.dice_attempt +1
        st.write("Remeber your Choices to Submit the form!")
        st.markdown("- You have the freedom to provide any answer! Remeber: If an attempt is **less than 3** you will loose **Rs. 200** from given coins")


# In[ ]:


def submit_results():
    st.subheader(f"You Earned Coins worh of Rs. {st.session_state.total}")
    st.subheader("Submit Your Results")
    st.markdown("To proceed please enter below details. Your information are collected anonymously.")
    
    gender_select = st.selectbox(
    "Your Gender?",
    ("Male", "Female")
    )

    age_select = st.selectbox(
        "Your Age?",
        ("10-15", "16-20","21-25","26-30","31-35","36-40")
    )

    state_select = st.selectbox(
        "Your Current occupation?",
        ("Student","School Leaver","University Undergraduate","Working")
    )
    if st.button('Submit and Complete Game'):
        st.write("Thank you for your participation!")


# In[18]:



coin_ui()
if st.session_state.coin_attempt > 4:
    if st.session_state.next_level == False:
        st.subheader("Would you like to Play Next Level?")
        st.markdown("- Remeber: Playing Next level you can earn 600 more coins! for any fail attempt: You'll loose Rs. 200 coins!")
        if st.button("Play Next Level"):
            st.session_state.next_level = True
            st.session_state.total = st.session_state.total + 300
        if st.button("No I will stop here and keep coins"):
            st.write(f"Your Final Coin Balance: Rs. {st.session_state.total}")
            st.markdown("""
            <iframe id="typeform-full" width="100%" height="600px" frameborder="0" allow="camera; microphone; autoplay; encrypted-media;" src="https://form.typeform.com/to/NrvgQZOM?typeform-medium=embed-snippet"></iframe> 
            <script type="text/javascript" src="https://embed.typeform.com/embed.js"></script>
            """, unsafe_allow_html=True)
    else:
        dice_ui()
            
# submit_results()
if st.session_state.coin_attempt > 4 and st.session_state.dice_attempt > 4:
    st.subheader("Submit your Results")
    st.markdown("""
    <iframe id="typeform-full" width="100%" height="600px" frameborder="0" allow="camera; microphone; autoplay; encrypted-media;" src="https://form.typeform.com/to/NrvgQZOM?typeform-medium=embed-snippet"></iframe> 
    <script type="text/javascript" src="https://embed.typeform.com/embed.js"></script>
    """, unsafe_allow_html=True)


# In[ ]:




