### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

I have used /pages concept to implement all questions with sidebar to choose from.

1. In Pod_tracker I used pd.Dataframe to create table from dictionary data. Then I filtered based on input from selectbox. Then I used filtered data for sorting based on input.<br>

2. In weather data I have used http://api.weatherapi.com for fecthing details and alerts. Here I have displayed routes and based on input I will display weather at city A and B and also alerts. I have formed on table hypothetically to decide speed limits. Speed limit gets printed based on if else conditions and weather data fetched.<br>

3. In this I have created some energy facts in json format and this is returned as response when api is called. I have used https://tahapp.free.beeceptor.com/ this site for the same. And the displayed the energy facts.<br>

4. Here I have used same pod data from first question and gave user input to select which 2 pods to select on. I extracted data into two lists based on iloc and then printed accordingly.<br>

5. For hyperloop facts I have st.markdown to give some different colors for showing diiferent facts. Here also I have stored facts in json format and is received as response when api is queried. I have used fun facts on main page itself.





