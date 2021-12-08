import streamlit as st
import newsreader as nr
import summarizer as summ


st.title('Welcome to Summarizer')

## Import URL
URL = st.text_input('Enter URL to generate summary')

if URL=="":
    data_load_state = st.text("Waiting for URL")
else:
    data_load_state = st.text('Extracting data in progress...')
    title,publish_date,text,keywords = nr.newsextract(URL)
    data_load_state.text('Extraction complete!')
    st.write('Title:',title)
    st.write('Published on:', publish_date)
    st.write('Keywords:', keywords)
    st.subheader('News')
    st.write(text)
    data_load_state2 = st.text('Summarization starts...')
    summary = summ.summarization(text)
    data_load_state2.text('Summarization complete!')
    st.subheader('Summary')
    st.write(summary)