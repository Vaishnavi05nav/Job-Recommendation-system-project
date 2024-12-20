import streamlit as st
import pandas as pd
import pickle

from streamlit import title

job_df = pickle.load(open('job_df.pkl','rb'))
similarity = pickle.load(open('similarity (1).pkl','rb'))

import streamlit as st


def recommendation(title):
    # Ensure the title exists in the job_df
    if title not in job_df['Title'].values:
        return ["No matching job title found."]

    idx = job_df[job_df['Title'] == title].index[0]
    idx = job_df.index.get_loc(idx)

    # Calculate similarity
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[1:20]

    jobs = []
    for i in distances:
        jobs.append(job_df.iloc[i[0]].Title)

    return jobs


# Web app
st.title('Job Recommendation System')

# Allow user to search for a job title
title = st.selectbox('Search job', job_df['Title'])

if title:
    job_recommendations = recommendation(title)

    # Display the recommended jobs
    if job_recommendations:
        st.write(job_recommendations)


def recommendation (title):
    idx = job_df[job_df['Title'] == title].index[0]
    idx = job_df.index.get_loc(idx)
    distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda  x:x[1])[1:20]

    jobs = []
    for i in distances:
        jobs.append (job_df.iloc[i[0]].Title)

        return jobs

# web app
st.title('Job Recommendation system')
st.selectbox('search job',job_df['Title'])


if job:
    st.write(job)

