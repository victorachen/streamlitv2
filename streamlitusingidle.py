# to do next:
# figure out how to write to new lines on streamlit

##terminal commands: streamlit run C:\Users\Lenovo\PycharmProjects\streamlit\streamlitusingidle.py
import streamlit as st
from dummy import *

##Firebase stuff below:
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(st.secrets["firestore_keys_baby"])
    firebase_admin.initialize_app(cred)

db = firestore.client()
##db.collection('persons').add({'name':'Jeff','age':40})


# Goal: work on getting firebase data and printing it
##specificresult = db.collection('persons').document("p1").get()
##if specificresult.exists:
##    print(specificresult.to_dict())
##


entire_collection = db.collection('Vacancy').get()

s = ""
##just_rented: dictionary of just rented units
just_rented = db.collection('Vacancy').where("type", "==", "just_rented").get()
for doc in just_rented:
    d = doc.to_dict()
print(d)

for i in d:
    print(i)
    print(d[i])


# no_status
# recently_updated
# rent_ready
# under_construction
# unit_turns

# outputs the entire text output (for streamlit to display)
def text_output():
    for i in d:
        line_item = i + ": " + d[i]
        st.write(line_item)
    return None


# commenting off for now
##for unit_type in entire_collection:
##    docs = db.collection
##    #THIS IS WHAT YOU ARE LOOKING FOR
##    dic = entire_collection.to_dict()
##    print('dic:')
##    print(dic)
##    for i in dic:
##        s += str(dic[i])
##print(s)

text_output()
st.markdown("""Hello

This is a cheat sheet built with the most common charts that I use in the data analysis for the projects.

The idea is to have a quick and useful sheet where anyone can copy and past the code (1 line command usually) to generate the charts below.
""")

L = ['a', 'b', 'c', 'd']
s = """ """
for i in L:
    s += i + "\n"
st.markdown(s)

##C:\\Users\\Lenovo\\anaconda3\\envs\\streamlit


