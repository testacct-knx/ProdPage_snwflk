# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col


cnx = st.connection("snowflake")
session = cnx.session()


# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

prod_table = session.table("zenas_athleisure_db.products.catalog_for_website")#.select(col('color_or_style'), col('file_name')) 
color_select = st.selectbox("Pick a sweatsuit color or style", prod_table.select(col('color_or_style')))

# Currently app has problems switching colors for all of them, unknown why but may be the way streamlit is caching and pulling data.
# Improvment idea: Convert the dataframe converstion to pandas INTO a sql select statement and pull the values from that table
if color_select:
    # Create dataframe, select color, return results
    pd_df = prod_table.to_pandas()
    st.subheader(f'Product Info for {color_select} color')


    color_df = pd_df.loc[pd_df['COLOR_OR_STYLE'] == color_select, :]#.iloc[0]
    # st.dataframe(color_df)
    st.image(color_df['FILE_URL'].values[0], caption=f"Warm Comfortable {color_select} sweatsuit.")
    st.write(f"""
    Price: {color_df['PRICE'].values[0]}\n
    Sizes Available: {color_df['SIZE_LIST'].values[0]}\n
    BONUS: {color_df['UPSELL_PRODUCT_DESC'].values[0]}
    """)

st.stop()

# CopyPasta from training, uses different method to pull data which may be why my version is not always returning the correct results, something to da with caching of the table and then converting to pandas is loosing it :/
# import streamlit as st
# from snowflake.snowpark.context import get_active_session
# from snowflake.snowpark.functions import col
# import pandas as pd
#
# st.title("Zena's Amazing Athleisure Catalog")
#
# session = get_active_session()
#
# # get a list of colors for a drop list selection
# table_colors = session.sql("select color_or_style from catalog_for_website")
# pd_colors = table_colors.to_pandas()
#
# # Oyt the list of colors into a drop list selector 
# option = st.selectbox('Pick a sweatsuit color or style:', pd_colors)
#
# # We'll build the image caption now, since we can
# product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
#
# # use the color selected to go back and get all the info from the database
# table_prod_data = session.sql("select file_name, price, size_list, upsell_product_desc, file_url from catalog_for_website where color_or_style = '" + option + "';")
# pd_prod_data = table_prod_data.to_pandas() 
#
# # assign each column of the row returned to its own variable 
# price = '$' + str(pd_prod_data['PRICE'].iloc[0])+'0'
# file_name = pd_prod_data['FILE_NAME'].iloc[0]
# size_list = pd_prod_data['SIZE_LIST'].iloc[0]
# upsell = pd_prod_data['UPSELL_PRODUCT_DESC'].iloc[0]
# url = pd_prod_data['FILE_URL'].iloc[0]
#
# # display the info on the page
# st.image(image=file_name, width=400, caption=product_caption)
# st.markdown('**Price:** '+ price)
# st.markdown('**Sizes Available:** ' + size_list)
# st.markdown('**Also Consider:** ' + upsell)
#
#
# # st.write(url)
