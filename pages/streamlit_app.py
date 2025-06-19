# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col


cnx = st.connection("snowflake")
session = cnx.session()


# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

prod_table = session.table("zenas_athleisure_db.products.catalog_for_website")#.select(col('color_or_style'), col('file_name')) 
pd_df = prod_table.to_pandas()

color_select = st.selectbox("Pick a sweatsuit color or style", prod_table.select(col('color_or_style')))


if color_select:
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
