# to do next:
# alphabetize everything

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
# def text_output():
#     for i in d:
#         line_item = i + ": " + d[i]
#         st.write(line_item)
#     return None

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

# text_output()

L = ['a', 'b', 'c', 'd']
s = """ """
for i in L:
    # s += i + "\n"
    st.markdown("- "+i)
st.write(":heavy_minus_sign:" * 34)
st.write('whatsup')
#STARTING THE REAL CODE BABY

rent_ready = db.collection('Vacancy').where("type", "==", "rent_ready").get()
unit_turns = db.collection('Vacancy').where("type", "==", "unit_turns").get()
just_rented = db.collection('Vacancy').where("type", "==", "just_rented").get()
under_construction = db.collection('Vacancy').where("type", "==", "under_construction").get()
no_status = db.collection('Vacancy').where("type", "==", "no_status").get()

#Helper: replaces all "_" with " "
def format(key,value):
    return key.replace('_',' ')+value

def format2(dic):
    s = ""
    for i in dic:
        if i!='type':
            s += format(i,"") + ", "
    return s
#to do: put everything in """"""" string
st.header('Rent Ready:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
s = """"""
for doc in rent_ready:
    d = doc.to_dict()
    for i in d:
        if i != 'type':
            s+= format(i,d[i]) + "\n"+"\n"
st.markdown(s)

st.header('Unit Turns:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
for doc in unit_turns:
    d = doc.to_dict()
    for i in d:
        if i != 'type':
            st.write(format(i,d[i]))
st.title('Just Rented:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
for doc in just_rented:
    d = doc.to_dict()
    for i in d:
        if i != 'type':
            st.write(format(i,d[i]))
st.title('Under Construction:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
for doc in under_construction:
    d = doc.to_dict()
    string = format2(d)
    st.markdown(string)

st.header('No Status:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
for doc in no_status:
    d = doc.to_dict()
    string = format2(d)
    st.write(string)
##C:\\Users\\Lenovo\\anaconda3\\envs\\streamlit


