import streamlit as st
import pandas as pd

st.title('CSV Data Editor')

st.subheader("Discover a smarter way to manage your CSV data with our user-friendly app.")
st.text("Simply upload your CSV file to instantly see the total number of rows and begin editing the raw data directly within the interface.")
st.text("For CSV files that include a 'type' column, our tool goes a step further by providing a clear percentage breakdown of each value, offering valuable insights at a glance.")

uploaded_file = st.file_uploader('Upload CSV data', type='csv', accept_multiple_files=False)

if uploaded_file is not None:
    st.divider()
    filename=uploaded_file.name
    st.header(filename)
    df = pd.read_csv(uploaded_file)
    
    row_count = df.shape[0]
    
    st.metric('Total rows', row_count, border=True)
    if 'type' in df.columns:
        st.subheader('Types')
        types = df['type'].unique()
    
        cols = st.columns(len(types))
        for idx, c in enumerate(cols):
            amount_for_type = df[df['type']==types[idx]].shape[0]
            perc = round(100*amount_for_type/row_count, 1)
            cols[idx].metric(types[idx], f'{perc}%', border=True)
    
    st.subheader('The data')
    edited_data = st.data_editor(df, use_container_width=True, hide_index=True)

    st.download_button("Download CSV", 
                       edited_data.to_csv(), 
                       file_name=f"edited_{filename}",
                       mime='text/csv')