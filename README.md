# Campus_Placement_Prediction_Using_Ml_With_Streamlit_Deployment

Predict wheter a student can get placement or not based on his or her performance in academics , work experience, projects etc.... 
Where this is project is limited to few properties like : SSC Marks, High School Marks, Techinal Degree, Degree Specialization,MBA Marks, Degree Marks

The UI of the project will be ->
![main · Streamlit - Google Chrome 16-01-2023 16_40_15](https://user-images.githubusercontent.com/82018631/212665354-bfa83048-97f9-4c1b-96d5-13b7da3fb055.png)


If the person or student the qualities enough he would be getting the postive report with percentage of selection as shown below ->
![main · Streamlit - Google Chrome 16-01-2023 16_40_47](https://user-images.githubusercontent.com/82018631/212665534-aca3642d-1d15-4ef8-b999-f86e0cf83191.png)

Else he would be getting a negative message along with few suggestion which can be modified to give a better successfull outcome, Base view is shown below -> 
![main · Streamlit - Google Chrome 16-01-2023 16_41_02](https://user-images.githubusercontent.com/82018631/212665690-1a96c6f0-751c-4547-95aa-129082cd2b8c.png)


The steps involved in the system is : 
-> Loading the data 
-> Performing the data preprocessing like Handling Missing Data, Finding Correlation, Feature Creation etc..
-> Perform Exploratory Data Analysis and the find the best features to run the model
-> Create the model and find the accuracy score and make it the test the test set
-> Pickle the model into .pkl file which is will be used to predict the data
-> Create the UI using streamlit and combine the pkl file into the UI
-> Run it using streamlit run main.py to get the outcome

U can use the pkl file directly instead of creating the model
