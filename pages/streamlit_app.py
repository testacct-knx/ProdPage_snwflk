# Import python packages
import streamlit as st

cnx = st.connection("snowflake")
session = cnx.session()

# smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
  "Choose the fruits you want in your custom Smoothie!"
)

name_on_order = st.text_input("Name on Smoothie:", max_chars=100)
st.write("The name on your smoothie will be: ", name_on_order)

st.image(image="https://sfc-prod3-ds1-86-customer-stage.s3.us-west-2.amazonaws.com/yoqz0000-s/stages/401f527e-4e80-44f4-bf6d-a94bb7c42d54/navy_blue_sweatsuit.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAUIZLYB2N3S7XF256%2F20250619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250619T170038Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=dafe48a12a73e8472015feffd919bd7f0c87b487a9ec4d300b641814123ae63c")
# my_dataframe = st.dataframe("zenas_athleisure_db.products.catalog_for_website") #.select(col('FRUIT_NAME'), col('search_on'))

# pd_df = my_dataframe.to_pandas()
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
#     my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
#             values ('""" + ingredients_string + """', '""" + name_on_order + """')"""
#
#     # st.write(my_insert_stmt)
#     ###
#     time_to_insert = st.button('Submit Order')
#     if time_to_insert:
#         session.sql(my_insert_stmt).collect()
#
#         st.success(f"Your Smoothie is ordered, {name_on_order}!", icon="✅")

