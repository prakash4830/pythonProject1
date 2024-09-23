import streamlit as st

st.header("What is K-Means Clustering")

st.write('''
        K-Means Clustering is an Unsupervised Learning algorithm, which groups the unlabeled dataset into different 
        -clusters.
        ''')
st.write('''
        K-means clustering is a way of grouping data based on how similar or close the data points are to each other.
        -Imagine you have a bunch of points, and you want to group them into clusters. The algorithm works by first 
        -randomly picking some central points (called centroids) and then assigning every data point to the nearest 
        -centroid.
        ''')
st.write('''
        Once that’s done, it recalculates the centroids based on the new groupings and repeats the process until the
        -clusters make sense. It’s a pretty fast and efficient method, but it works best when the clusters are distinct 
        -and not too mixed up. One challenge, though, is figuring out the right number of clusters (K) beforehand. Plus, 
        -if there’s a lot of noise or overlap in the data, K Means might not perform as well.
        ''')

st.subheader("How Does K-Means Clustering Work")
st.image("images/k_steps.png")
st.subheader("Step 1:")
st.write('''
        The Elbow method is the best way to find the number of clusters. The elbow method constitutes running  K-Means 
        -clustering on the dataset. 
        ''')
st.write('''
        Next, we use within-sum-of-squares as a measure to find the optimum number of clusters that can be formed for 
        -a given data set. Within the sum of squares (WSS) is defined as the sum of the squared distance between each 
        -member of the cluster and its centroid.
        ''')
st.image("images/s_1.png")

st.write('''
        Here, WSS is on the y-axis and number of clusters on the x-axis.
        ''')

st.subheader("Step 2:")
st.write('''
        We can randomly initialize two points called the cluster centroids. 
        Here, C1 and C2 are the centroids assigned randomly.
        ''')
st.image("images/s_2.png")

st.subheader("Step 3:")
st.write('''
        Now the distance of each location from the centroid is measured, and each data point is assigned to the centroid
        , which is closest to it. 
        ''')
st.image("images/s_3.png", width=400, use_column_width=False)

st.subheader("Step 4:")
st.write('''
        Compute the actual centroid of data points for the first group. 
        ''')

st.subheader("Step 5:")
st.write('''
        Reposition the random centroid to the actual centroid. 
        ''')
st.image("images/s_4.png", width=400, use_column_width=False)

st.subheader("Step 6:")
st.write('''
        Compute the actual centroid of data points for the second group. 
        ''')

st.subheader("Step 7:")
st.write('''
        Reposition the random centroid to the actual centroid. 
        ''')
st.image("images/s_5.png", width=400, use_column_width=False)

st.subheader("Step 8:")
st.write('''
        Once the cluster becomes static, the k-means algorithm is said to be converged. 
        The final cluster with centroids c1 and c2 is as shown below:
        ''')
st.image("images/s_6.png", width=400, use_column_width=False)

st.header("Following is the Data Dictionary for Credit Card dataset")
st.markdown("""

- **Source:** This is based on Credit Card Dataset for Clustering from Kaggle.

- **Problem:** This is a clustering problem. Here goal is to understand customer segments of credit card usage for defining marketing strategy.

- **Info:** The sample Dataset summarizes the usage behavior of about 8950 active credit card holders during the last 6 months. The file is at a customer level with 18 behavioral variables.

**Feature Explanation:**

- **CUSTID:** Identification of Credit Card holder (Categorical).

- **BALANCE:** Balance amount left in their account to make purchases.

- **BALANCEFREQUENCY:** How frequently the Balance is updated, score between 0 and 1 (1 = frequently updated, 0 = not frequently updated).

- **PURCHASES:** Amount of purchases made from account.

- **ONEOFFPURCHASES:** Maximum purchase amount done in one-go.

- **INSTALLMENTSPURCHASES:** Amount of purchase done in installment.

- **CASHADVANCE:** Cash in advance given by the user.

- **PURCHASESFREQUENCY:** How frequently the Purchases are being made, score between 0 and 1 (1 = frequently purchased, 0 = not frequently purchased).

- **ONEOFFPURCHASESFREQUENCY:** How frequently Purchases are happening in one-go (1 = frequently purchased, 0 = not frequently purchased).

- **PURCHASESINSTALLMENTSFREQUENCY:** How frequently purchases in installments are being done (1 = frequently done, 0 = not frequently done).

- **CASHADVANCEFREQUENCY:** How frequently the cash in advance being paid.

- **CASHADVANCETRX:** Number of Transactions made with "Cash in Advanced.

- **PURCHASESTRX:** Numbe of purchase transactions made.

- **CREDITLIMIT:** Limit of Credit Card for user.

- **PAYMENTS:** Amount of Payment done by user.

- **MINIMUM_PAYMENTS:** Minimum amount of payments made by user.

- **PRCFULLPAYMENT:** Percent of full payment paid by user.

- **TENURE:** Tenure of credit card service for user.
""")
