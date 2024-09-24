import streamlit as st
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Check if the DataFrame exists in session state
if 'shared_df_page_1' and 'shared_df_org_page_1' in st.session_state:
    df = st.session_state['shared_df_page_1']
    df_org = st.session_state['shared_df_org_page_1']
    st.write("DataFrame from Page 1:")
    st.write(df)

# Your code to process the DataFrame further...


    dataset_orig = df_org

    dataset = df

# KMeans Clustering
    st.subheader("KMeans Clustering")

# Finding KValue by using Elbow Method
    st.header('Finding Optimal Number of Clusters')
    k_value = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
        kmeans.fit(dataset)
        k_value.append(kmeans.inertia_)

    fig = px.line(x=range(1, 11), y=k_value, title='Credit Card Users - Elbow Method',
              labels={'x': 'Number of clusters', 'y': 'WACC'})
    st.plotly_chart(fig)

# Select number of clusters
    st.write("### Select Number of Clusters:")
    n_clusters = st.slider("Choose the number of clusters:", 2, 10, 3)

# Applying KMeans Clustering
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=300, n_init=10, random_state=42)
    y_kmeans = kmeans.fit_predict(dataset)
    dataset['Cluster'] = y_kmeans
    dataset_orig['Cluster'] = y_kmeans

# Store the DataFrame in session state
    st.session_state['shared_df_org_page_2'] = dataset_orig

# Visualize the clusters
    fig = px.scatter(dataset, x='PURCHASES', y='PAYMENTS', color='Cluster', title='KMeans Clustering', color_continuous_scale='Plasma')
    st.plotly_chart(fig)

# Plotting Cluster Analysis
    st.subheader('Cluster Analysis')
    fig = px.histogram(dataset, x='Cluster', title='Number of Credit Card Customers in Different Clusters', color='Cluster')
    st.plotly_chart(fig)

    fig = px.scatter(dataset, x='PURCHASES', y='PAYMENTS', color='Cluster', size='CREDIT_LIMIT',
                 title='Payments vs Purchases by Cluster', color_continuous_scale='Plasma')
    st.plotly_chart(fig)

    fig = px.scatter(dataset, x='CREDIT_LIMIT', y='PURCHASES', color='Cluster',
                 title='Credit Limit vs Purchases by Cluster', color_continuous_scale='Plasma')
    st.plotly_chart(fig)

    fig = px.scatter(dataset, x='BALANCE', y='ONEOFF_PURCHASES', color='Cluster',
                 title='Balance vs One-Off Purchases by Cluster', color_continuous_scale='Plasma')
    st.plotly_chart(fig)

# Calculate Silhouette Scores
    silhouette_scores = []
    for i in range(2, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
        kmeans.fit(dataset)
        score = silhouette_score(dataset, kmeans.labels_)
        silhouette_scores.append(score)

    fig = px.line(x=range(2, 11), y=silhouette_scores, title='Silhouette Score for Each Cluster Number',
              labels={'x': 'Number of Clusters', 'y': 'Silhouette Score'})
    st.plotly_chart(fig)

else:
    st.write("No DataFrame found. Please upload the dataset in Exploratory data analysis🙂.")