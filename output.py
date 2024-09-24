import base64
import pandas as pd
import streamlit as st

# Check if the DataFrame exists in session state
if 'shared_df_org_page_2' in st.session_state:
    df_org = st.session_state['shared_df_org_page_2']
    st.write("DataFrame from Page 1:")
    st.write(df_org)

# Your code to process the DataFrame further...

    dataset_1 = pd.DataFrame(df_org)

#def get_clustered_data_download_link(df):
   
    #Generates a link to download the clustered dataset as a CSV.

 #   csv = df.to_csv(index=False)
  #  csv_bytes = csv.encode()
   # b64 = base64.b64encode(csv_bytes).decode()
    #href = f'<a href="data:file/csv;base64,{b64}" download="clustered_dataset.csv">Download Clustered Dataset (CSV)</a>'
    #return href

# Assuming you have your clustered dataset in a DataFrame called 'clustered_df'
    clustered_df = dataset_1

# Your clustered data here

# Create a download button
    if st.button('Convert the dataframe to CSV'):
        csv = clustered_df.to_csv(index=False)
        csv_bytes = csv.encode()
        st.download_button(
            label="Download Clustered Dataset (CSV)",
            data=csv_bytes,
            file_name="clustered_dataset.csv",
            mime="text/csv",
        )
else:
    st.write("No DataFrame found. Please upload the dataset in Exploratory data analysis🙂.")
# Alternatively, you can use the get_clustered_data_download_link function
#st.markdown(get_clustered_data_download_link(clustered_df), unsafe_allow_html=True)