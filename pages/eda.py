import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
import plotly.express as px
from statsmodels.stats.outliers_influence import variance_inflation_factor
import io


# Use the function in your Streamlit app
dataset_orig = pd.read_csv("cc_general_project.csv")

if dataset_orig is not None:
    st.write("Preview of the dataset:")

    # Display the dataset
    st.subheader("Dataset Overview")
    st.write(dataset_orig.head())
    # Since 'CUST_ID' is a unique identifier, we won't visualize it, but let's check for unique values
    total_customers = dataset_orig['CUST_ID'].nunique()

    st.subheader("Total Unique Customers")
    st.metric(label="", value=total_customers)
    # Display the dataset
    st.subheader("Dataset Info")
    # st.write(dataset.info())

    st.write(dataset_orig.describe())

    st.subheader("Check whether their is a Null Value")

    null_count = dataset_orig.isnull().sum()

    # Create a new DataFrame with custom column names
    null_df = pd.DataFrame({
        'Feature Name': null_count.index,
        'Missing Values Count': null_count.values
    })

    # Display the DataFrame in Streamlit
    st.write(null_df)

    # -----------------------Handling Missing Values------------------
    impute = SimpleImputer(strategy='mean')
    dataset_orig['CREDIT_LIMIT'] = impute.fit_transform(dataset_orig[['CREDIT_LIMIT']])
    dataset_orig['MINIMUM_PAYMENTS'] = impute.fit_transform(dataset_orig[['MINIMUM_PAYMENTS']])

    st.subheader("Converting the Null values instead of mean")
    null_count = dataset_orig.isnull().sum()

    # Create a new DataFrame with custom column names
    null_df = pd.DataFrame({
        'Feature Name': null_count.index,
        'Missing Values Count': null_count.values
    })
    st.write(null_df)

    #dataset_1 = dataset_orig.copy()
    dataset = dataset_orig.iloc[:, 1:18]
    st.session_state['shared_df_page_1'] = dataset
    st.session_state['shared_df_org_page_1'] = dataset_orig

    st.header("Exploratory Data Analysis")
    st.subheader("Histogram Analysis")
    # Get all column names
    columns = dataset.columns

    # Create a loop for 10 rows, 2 columns layout
    for i in range(0, len(columns), 2):
        # Create two columns
        col1, col2 = st.columns(2)

    # Plot first column's histogram
        with col1:
            if i < len(columns):  # Check if the index is within the column list
                fig1 = px.histogram(dataset, x=columns[i], nbins=30, title=f'Distribution of {columns[i]}', height=400)
                fig1.update_traces(marker_line_width=1, marker_line_color="black")
                st.plotly_chart(fig1)

        # Plot second column's histogram
        with col2:
            if i + 1 < len(columns):  # Check if the next index is within the column list
                fig2 = px.histogram(dataset, x=columns[i + 1], nbins=30, title=f'Distribution of {columns[i + 1]}',
                                height=400)
                fig2.update_traces(marker_line_width=1, marker_line_color="black")
                st.plotly_chart(fig2)


    # Correlation heatmap
    st.subheader("Correlation Matrix")
    corr_matrix = dataset.corr()
    fig = px.imshow(round(corr_matrix, 2), text_auto=True, aspect="auto",
                color_continuous_scale="Reds")
    fig.update_xaxes(tickvals=[], showticklabels=False)
    fig.update_layout(coloraxis_colorbar=dict(tickvals=[-0.25, 0, 0.25, 0.5, 0.75, 1]))
    st.plotly_chart(fig)

    # Scatter plots
    st.subheader('Scatter Plots')

    fig = px.scatter(dataset, x='BALANCE', y='PURCHASES', title='Balance vs Purchases')
    fig.update_traces(marker=dict(colorscale='Plasma'))
    st.plotly_chart(fig)

    fig = px.scatter(dataset, x='CREDIT_LIMIT', y='PAYMENTS', title='Credit Limit vs Payments')
    st.plotly_chart(fig)

    # Distribution of Purchase Frequency
    fig = px.histogram(dataset, x='PURCHASES_FREQUENCY', title='Distribution of Purchase Frequency', nbins=30)
    st.plotly_chart(fig)

    # Boxplot Payments vs Credit Limit
    fig = px.box(dataset, x='CREDIT_LIMIT', y='PAYMENTS', title='Payments vs Credit Limit')
    st.plotly_chart(fig)

    # Minimum payments vs full payment percentage
    fig = px.scatter(dataset, x='MINIMUM_PAYMENTS', y='PRC_FULL_PAYMENT',
                 title='Minimum Payments vs Percent of Full Payment')
    st.plotly_chart(fig)

    # PairPlot (scatter matrix)
    fig = px.scatter_matrix(dataset, dimensions=['BALANCE', 'PURCHASES', 'CREDIT_LIMIT', 'PAYMENTS', 'TENURE'],
                        color="ONEOFF_PURCHASES_FREQUENCY", title='Scatter Matrix of Credit Card Users')
    st.plotly_chart(fig)

    # Checking multi-collinearity using variance inflation factor (VIF)
    st.subheader("Checking multi-collinearity using variance inflation factor (VIF)")
    X = dataset[['BALANCE', 'PURCHASES', 'CREDIT_LIMIT', 'PAYMENTS', 'TENURE']]
    vif = pd.DataFrame()
    vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif["features"] = X.columns
    st.write(vif)

else:
    st.write("Please upload a CSV file.")
