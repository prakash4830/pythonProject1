import streamlit as st

# Add title only to specific pages
st.title("Credit Card Customer Segmentation using K-Means Clustering")

home_page = st.Page(
    "pages/kmean_theory.py",
    title="KMean",
    icon=":material/home:",
    default=True,
)
page_1 = st.Page(
    "pages/eda.py",
    title="Exploratory Data Analysis",
    icon=":material/query_stats:",
)
page_2 = st.Page(
    "pages/kmean_clustering.py",
    title="Kmean Cluster Modeling",
    icon=":material/model_training:",
)
page_3 = st.Page(
    "pages/output.py",
    title="Model Output",
    icon=":material/download:",
)
about_page = st.Page(
    "pages/about.py",
    title="About",
    icon=":material/account_circle:",
)

pg = st.navigation(
    {
        "Home": [home_page],
        "Projects": [page_1, page_2, page_3],
        "About": [about_page]
    }
)

pg.run()
