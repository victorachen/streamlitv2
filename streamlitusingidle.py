# to do: work on line 242
# #Vacant Lots: (1) Lot Size (2) Coach Size, (3) Status
# #New Constr (1) who is the contractor, (2) status/next steps
#
# to do next:
# alphabetize everything, do bullet points, but pricing at the top
#col 1 vs col 2: https://daniellewisdl-streamlit-cheat-sheet-app-ytm9sg.streamlitapp.com/
#plotly: https://mpkrass7-solid-octo-robot-migration-app-nabfxv.streamlitapp.com/
#nav bar: https://github.com/giswqs/geemap-apps
#testing update update once again


##terminal commands: streamlit run C:\Users\Lenovo\PycharmProjects\streamlit\streamlitusingidle.py
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import firestore
from google.oauth2 import service_account
import json


from natsort import natsorted, ns
from dummy import *


key_dict = json.loads(st.secrets['textkey'])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)

entire_collection = db.collection('Vacancy').get()

# for doc in entire_collection:
#     d = doc.to_dict()
#     for entry in d:
#         st.write(entry + ': ' + d[entry])

st.set_page_config(
     page_title='Vacancies!',
     layout="wide",
     initial_sidebar_state="expanded",
)

s = ""
##just_rented: dictionary of just rented units
# just_rented = db.collection('Vacancy').where("type", "==", "just_rented").get()
# for doc in just_rented:
#     d = doc.to_dict()
#
# for i in d:
#     print(i)
#     print(d[i])


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

#l
# st.write('''The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows:
# The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows:
# The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows: The rent guidelines are as follows: ''')

st.header('All Vacancy:')
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

#Alphabetize a list using NatSort
#given ['Pat 15','Pat 97','Wish 63'] -> alphabetize to -> ['Crest 1', 'Wish 63']
def alph(ogL, newL):
    return natsorted(ogL, alg=ns.IGNORECASE)

rent_ready = db.collection('Vacancy').where("type", "==", "rent_ready").get()
unit_turns = db.collection('Vacancy').where("type", "==", "unit_turns").get()
just_rented = db.collection('Vacancy').where("type", "==", "just_rented").get()
under_construction = db.collection('Vacancy').where("type", "==", "under_construction").get()
vacant_lots = db.collection('Vacancy').where("type", "==", "empty_lots").get()
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

col1.subheader('Recently Vacated- Needs Work:')
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
    s+= "* "+i + "\n"
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
    s+= "* "+i + "\n"
col2.code(s)

col3.subheader('New Coach/Construction:')
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

col3.subheader('Vacant Lots:')
# st.write('-  -  -  -  -  -  -  -  -  -  -')
for doc in vacant_lots:
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

col2.subheader('No Status (Pls Update):')
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
    s+= "* "+i + "\n"
col2.code(s)

#Code from Feb 2nd
#Layering in more details on Streamlit top layer
#first "gate"
def first_gate():
    form = st.form(key='input')
    form.header('Provide More Details Here:')
    list = ['Vacant Lots','New Coach/Construction','Recently Vacated-Needs Work']
    input = form.selectbox("Select Option", list)
    submit = form.form_submit_button('Submit')
    if submit:
        st.session_state['submit'] = 'yes'
    return input

#Firestore Layer 2: maps streamlit inputs into "Layer 2" of Streamlit (separate collection)
#ex) layer2mapping('Hol5','vacant_lot','lot size: 50lx34w, coach size: 20x40, status: waiting on javier'
def layer2mapping(unit,lifecyclestage,string):
    return None

def second_gate():
    input = first_gate()

    def vacant_lots():
        form = st.form(key='secondform')
        form.header('Subform:')
        list = ['a', 'b', 'c']
        category = form.selectbox("Select suboption", list)
        submit = form.form_submit_button('Submit Again')
        if submit:
            st.write('nested submit')
            st.write('category: ' + category)
        return None

    def under_construction():
        form = st.form(key='secondform')
        form.header('Subform:')
        list = ['a', 'b', 'c']
        category = form.selectbox("Select suboption", list)
        submit = form.form_submit_button('Submit Again')
        if submit:
            st.write('nested submit')
            st.write('category: ' + category)
        return None
    def unit_turns():
        form = st.form(key='secondform')
        form.header('Subform:')
        list = ['a', 'b', 'c']
        category = form.selectbox("Select suboption", list)
        submit = form.form_submit_button('Submit Again')
        if submit:
            st.write('nested submit')
            st.write('category: ' + category)
        return None
    #once you hit submit list (1) further option (depending on which category) and (2) list of possible units
    if input == 'Vacant Lots' and st.session_state.submit == 'yes':
        vacant_lots()
    if input == 'New Coach/Construction' and st.session_state.submit == 'yes':
        under_construction()
    if input == 'Recently Vacated-Needs Work' and st.session_state.submit == 'yes':
        unit_turns()
    return None

second_gate()

    # if category == 'New Coach/Construction':
    #     subform = st.form(key='subform')
    #     subform.header('Subform:')
    #     sublist = ['a', 'b', 'c']
    #     subcategory = subform.selectbox("Select suboption", sublist)
    #     submit_again = subform.form_submit_button('Submit Again')
    #     if submit_again:
    #         st.write('nested submit')
    #         st.write('subcategory ' + subcategory)
    # if category == 'Recently Vacated-Needs Work':
    #     subform = st.form(key='subform')
    #     subform.header('Subform:')
    #     sublist = ['a', 'b', 'c']
    #     subcategory = subform.selectbox("Select suboption", sublist)
    #     submit_again = subform.form_submit_button('Submit Again')
    #     if submit_again:
    #         st.write('nested submit')
    #         st.write('subcategory ' + subcategory)
        # df = purchase_history_backend(material)
        # chartname = material + "- Purchase History Below:"
        # csvname = material + "_purchase_history.csv"
        #     (df, chartname, csvname)

st.write('')
st.write('')
st.write('Please Update: https://forms.gle/ZJminE5umWn9E8YM6')

##C:\\Users\\Lenovo\\anaconda3\\envs\\streamlit


