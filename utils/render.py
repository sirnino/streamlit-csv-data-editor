import streamlit as st

def init(title:str):
    st.set_page_config(page_title=title, layout="wide", initial_sidebar_state="collapsed")

def render_sidebar():
    with st.sidebar:
        st.subheader("Discover a smarter way to manage your CSV data with our user-friendly app.")
        st.text("Simply upload your CSV file to instantly see the total number of rows and begin editing the raw data directly within the interface.")
        st.text("For CSV files that include a 'type' column, our tool goes a step further by providing a clear percentage breakdown of each value, offering valuable insights at a glance.")
    return

def render_header(title:str):
    st.title(title)
    uploaded_file = st.file_uploader('Upload CSV data', type='csv', accept_multiple_files=False)
    st.divider()
    return uploaded_file

def render_metrics(file_name:str, row_count:int, types:dict):
    st.header(file_name)      
    st.metric('Total rows', row_count, border=True)

    if types:
        type_keys = list(types.keys())
        st.subheader('Types')
        cols = st.columns(len(type_keys))
        for col, (key, value) in zip(cols, types.items()):
            col.metric(label=key, value=f"{value}%", border=True)
    
    return


def render_data(data, download_file_name:str="edited_data.csv"):
    st.subheader('The data')
    edited_data = st.data_editor(data, use_container_width=True, hide_index=True)

    st.download_button("Download CSV", 
                       edited_data.to_csv(), 
                       file_name=download_file_name,
                       mime='text/csv')