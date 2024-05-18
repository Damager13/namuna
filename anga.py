import streamlit as st
import requests
import json 
import re

res = requests. get(' https://devapi.beyondchats.com/api/get_message_with_sources')
File = json.loads(res.text)

Main=File['data']['data']
All_responses=[Main[i]['response'] for i in range(len(Main)-1) ]
#responses_set=set([Main[i]['response'].lower() for i in range(len(Main)-1)])



option = st.selectbox(
   "How would you like to be contacted?",
   (All_responses),
   index=None,
   placeholder="Select Your Reponse",
)



   
   

try:
    i = All_responses.index(option)
except ValueError:
    st.warning('Select Responses From Above')
    st.stop()




Citation=[]
Citation=[]
for contexts in range(len(Main[i]['source'])):
    Temp_id = Main[i]['source'][contexts]['id']
    Temp_link = Main[i]['source'][contexts]['link']
    Temp_context = Main[i]['source'][contexts]['context']
    
    if Temp_link == '':
        link = re.findall(r'https?://\S+', Temp_context)
        if link:
            Citation.append({"id": Temp_id, "link": link[0]})
    else:
        Citation.append({"id": Temp_id, "link": Temp_link})


for contexts in range(len(Main[i]['source'])): 
    if Main[i]['source'][contexts]['link']== '':
      Temp_context=Main[i]['source'][contexts]['context']
      link=re.findall('https?://\S+',Temp_context)
      Temp_id=Main[i]['source'][contexts]['id']
      if link: 
        Citation.append ({"id": Temp_id,
                        "link":link[0]})# If you want multiple links for the same id Then you can remove the link index[0]
        
    Temp_id=Main[i]['source'][contexts]['id']
    Temp_link=Main[i]['source'][contexts]['link']
    if Temp_link:
        Citation.append({"id": Temp_id,"link":Temp_link})



st.write('Citation :', Citation)


