# to do next:
# alphabetize everything, do bullet points, but pricing at the top
#col 1 vs col 2: https://daniellewisdl-streamlit-cheat-sheet-app-ytm9sg.streamlitapp.com/
#plotly: https://mpkrass7-solid-octo-robot-migration-app-nabfxv.streamlitapp.com/
#nav bar: https://github.com/giswqs/geemap-apps
#testing update update once again


##terminal commands: streamlit run C:\Users\Lenovo\PycharmProjects\streamlit\streamlitusingidle.py
import streamlit as st
from dummy import *

st.set_page_config(
     page_title='Vacancies!',
     layout="wide",
     initial_sidebar_state="expanded",
)

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
st.write('''The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows: 
The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows: 
The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows: ''')

col1, col2, col3 = st.columns(3)

# L = ['a', 'b', 'c', 'd']
# s = """"""
# for i in L:
#     s += "- " + i + "\n"
#     # st.markdown("- "+i)
# col1.markdown(s)

# st.write(":heavy_minus_sign:" * 34)
# st.write('whatsup')
# STARTING THE REAL CODE BABYyy

#Alphabetize a list (recursively)
#given ['Pat 15','Pat 97','Wish 63'] -> alphabetize to -> ['Crest 1', 'Wish 63']
def alph(ogL, newL):
    if len(ogL) == 0:
        return newL
    min_ = min(ogL)
    ogL.remove(min_)
    newL.append(min_)
    return alph(ogL,newL)

rent_ready = db.collection('Vacancy').where("type", "==", "rent_ready").get()
unit_turns = db.collection('Vacancy').where("type", "==", "unit_turns").get()
just_rented = db.collection('Vacancy').where("type", "==", "just_rented").get()
under_construction = db.collection('Vacancy').where("type", "==", "under_construction").get()
no_status = db.collection('Vacancy').where("type", "==", "no_status").get()

#Helper: replaces all "_" with " "
def format(key,value):
    return key.replace('_',' ')+value

def format2(dic):
    s = ''''''
    for i in dic:
        if i!='type':
            s += format(i,'') + ', '+"\n"
    return s

col1.subheader('Rent Ready:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')

for doc in rent_ready:
    d = doc.to_dict()
#put everything into a list -> alphabetize list --> put alpha list into """ """ string
L = []
for i in d:
    if i != 'type':
        combined_str = format(i,'') + '' + d[i]
        L.append(combined_str)
Alph_L = alph(L,[])

s = """"""
for i in Alph_L:
    s+= "* "+i + "\n"
col1.code(s)

col1.subheader('Unit Turns:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
for doc in unit_turns:
    d = doc.to_dict()
#put everything into a list -> alphabetize list --> put alpha list into """ """ string
L = []
for i in d:
    if i != 'type':
        combined_str = format(i,'') + '' + d[i]
        L.append(combined_str)
Alph_L = alph(L,[])

s = """"""
for i in Alph_L:
    s+= "- "+i + "\n"
col1.code(s)


col2.subheader('Just Rented:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
for doc in just_rented:
    d = doc.to_dict()
#put everything into a list -> alphabetize list --> put alpha list into """ """ string
L = []
for i in d:
    if i != 'type':
        combined_str = format(i,'') + '' + d[i]
        L.append(combined_str)
Alph_L = alph(L,[])

s = """"""
for i in Alph_L:
    s+= "- "+i + "\n"
col2.code(s)

col3.subheader('Under Construction:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
for doc in under_construction:
    d = doc.to_dict()
#put everything into a list -> alphabetize list --> put alpha list into """ """ string
L = []
for i in d:
    if i != 'type':
        combined_str = format(i,'') + '' + d[i]
        L.append(combined_str)
Alph_L = alph(L,[])

s = """"""
for i in Alph_L:
    s+= "* "+i + "\n"
col3.code(s)

col2.subheader('No Status:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
for doc in no_status:
    d = doc.to_dict()
#put everything into a list -> alphabetize list --> put alpha list into """ """ string
L = []
for i in d:
    if i != 'type':
        combined_str = format(i,'') + '' + d[i]
        L.append(combined_str)
Alph_L = alph(L,[])

s = """"""
for i in Alph_L:
    s+= "- "+i + "\n"
col2.code(s)

st.write('')
st.write('')
st.write('Updates Made Here: https://forms.gle/ZJminE5umWn9E8YM6')

##C:\\Users\\Lenovo\\anaconda3\\envs\\streamlit


