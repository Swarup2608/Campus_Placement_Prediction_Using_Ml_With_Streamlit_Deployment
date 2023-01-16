import numpy as np
import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("placementpredictor.pkl",'rb'))


# Creating the app 
st.title("Campus Placement Prediction")
st.markdown("Upload the details of the student : ")

# Uploading the dog image
gender = st.selectbox("What is the gender?",("Male","Female"))
specialization = st.selectbox("What is the Specialization?",("Commerce","Science","Arts"))
degree = st.selectbox("What is the Degree Tech?",("Commerce & Management","Science & Tech","Others"))
exp = st.selectbox("Have Work Experience?",("Yes","No"))
tenm = st.number_input('SSC Marks')
interm = st.number_input('High School Marks')
degreem = st.number_input('Degree Marks')
mba = st.number_input('MBA Marks')
submit = st.button('Predict')
quotes = ["1. Try coding","2. Prepare well for the interview","3. Get good communication skills"]

if submit:
    if gender == 'Male':
        gender = 1
    else:
        gender = 0
    if specialization == 'Commerce':
        specialization = 1
    elif specialization == 'Science':
        specialization = 2
    else:
        specialization = 0
    if degree == 'Commerce & Management':
        degree = 0
    elif degree == 'Science & Tech':
        degree = 1
    else:
        degree = 2
    if exp == "Yes":
        exp = 1
    else:
        exp = 0
    df = pd.DataFrame({"gender":[gender],"ssc_p":[tenm],"hsc_p":[interm],"degree_p":[degreem],"degree_t":[degree],"workex":[exp],"specialisation":[specialization],"mba_p":[mba]})
    x = model.predict(df)
    if x[0] == 0:
        st.title("You could not get placed")
        for i in quotes:
            st.code(i)
    else:
        st.title("You will be placed with a probabilty percentage of : ")
        st.code(str(round(model.predict_proba(np.array(df))[0][1],5)), language="markdown")
# if submit:
#     if dog is not None:
#         # Converting the image to byte code
#         file_by = np.asarray(bytearray(dog.read()),dtype=np.uint8)
#         # Opening the image
#         open_cv = cv2.imdecode(file_by,1)
        
#         # Display the image uploaded
#         st.image(open_cv,channels="BGR")
#         # Resizing the image
#         open_cv = cv2.resize(open_cv,(224,224))
#         # Convert the image into 4 dimension 
#         open_cv.shape = (1,224,224,3)
#         Y_pred = model.predict(open_cv)
#         st.title("The dog breed of the uploaded image is : "+class_names[np.argmax(Y_pred)])


