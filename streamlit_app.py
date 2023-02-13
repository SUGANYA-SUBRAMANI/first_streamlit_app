
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLerror
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('omega 3 and blueberry oatmeal')
streamlit.text('kale ,spinach & rocket smoothie')
streamlit.text('hard-boiled egg')
streamlit.text('chocolates')
streamlit.header('🍇build your 🍌🥭first smoothie🍇')
# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)) # Display the table on the page.
# streamlit.dataframe(my_fruit_list)
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
# import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as table
streamlit.dataframe(fruityvice_normalized)
streamlit.stop()
# import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows= my_cur.fetchall()
streamlit.header("The fruit Load List contains:")
streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_input('What Fruit Would You Like To Add?','Jackfruit')
streamlit.write('Thanks For Adding',add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")

