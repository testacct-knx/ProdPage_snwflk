# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
# import requests


cnx = st.connection("snowflake")
session = cnx.session()

# smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

prod_table = session.table("zenas_athleisure_db.products.catalog_for_website")#.select(col('color_or_style'), col('file_name')) 
pd_df = prod_table.to_pandas()

color_select = st.selectbox("Pick a sweatsuit color or style", prod_table.select(col('color_or_style')))
# session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'), col('search_on'))

# TODO: create dataframe and pandas frame that can be used to extract the table catalog_for_website

if color_select:
    st.subheader(f'Product Info for {color_select} color')


    color_df = pd_df.loc[pd_df['COLOR_OR_STYLE'] == color_select, :]#.iloc[0]
    st.dataframe(color_df)
    # st.image(color_df['file_url'])
    # search_on = pd_df.loc[pd_df['color_or_style'] == color_select, 'file_name'].iloc[0]
#     st.write(f'The search value {color_select} is {search_on}')


# TODO: Create input box to search for colors at catalog_for_website.color_or_style
#TODO: Based off search results, show the first image that returns
#TODO Based off search print text of :show price, sizes available, & BONUS(?)



# st.image(image="https://sfc-prod3-ds1-86-customer-stage.s3.us-west-2.amazonaws.com/yoqz0000-s/stages/401f527e-4e80-44f4-bf6d-a94bb7c42d54/navy_blue_sweatsuit.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAUIZLYB2N3S7XF256%2F20250619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250619T170038Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=dafe48a12a73e8472015feffd919bd7f0c87b487a9ec4d300b641814123ae63c")
# my_dataframe = st.dataframe("zenas_athleisure_db.products.catalog_for_website") #.select(col('FRUIT_NAME'), col('search_on'))

# st.dataframe(pd_df)
st.stop()
#
# ingredients_list = st.multiselect(
#     'Choose up to 5 ingredients:'
#     , my_dataframe
#     , max_selections=5
# )
#
#
# if ingredients_list:
#     ingredients_string = ''
#
#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen + ' '
#
#         search_on = pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
#         # st.write(f'The search value for {fruit_chosen} is {search_on}')
#
#         fruit_api_loc = f"https://www.smoothiefroot.com/api/fruit/{str.lower(search_on)}"
#
#         st.subheader(f'{fruit_chosen} Nutritional Information')
#         smoothiefroot_response = requests.get(fruit_api_loc )
#         sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)
#
#
# # st.stop()
#     # st.write(ingredients_string)
# #
#     my_insert_stmt = """ insert into smoothies.public.orders(ingredients, color_select)
#             values ('""" + ingredients_string + """', '""" + color_select + """')"""
#
#     # st.write(my_insert_stmt)
#     ###
#     time_to_insert = st.button('Submit Order')
#     if time_to_insert:
#         session.sql(my_insert_stmt).collect()
#
#         st.success(f"Your Smoothie is ordered, {color_select}!", icon="✅")

