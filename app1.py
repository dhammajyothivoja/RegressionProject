import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def edaPage():
    st.title("Step-by-Step Data Analysis")

    upload_file=st.sidebar.file_uploader("Upload your csv file", type=["csv"])
    if upload_file:
        df= pd.read_csv(upload_file)
        st.success("File uploaded successfully!")

        st.header("1. Dataset Overview")
        st.write("shape :",df.shape)
        st.write("columns :",df.columns.tolist())
        st.dataframe(df.head())

        st.header("2. Missing Values")
        st.write(df.isnull().sum())

        st.header("3. Descriptive Statistics")
        st.dataframe(df.describe(include="all"))

        st.header("4. Data Types")
        num_col=df.select_dtypes(include=['int64', 'float64']).column.tolist()
        cat_cols=df.select_dtypes(include=["object"]).columns.tolist()
        st.write("Numerical Columns: ",num_col)
        st.write("Categorical Columns: ",cat_cols)

        st.header("5. Univariate Analysis")
        col=st.selectbox("select a column to plot",df.colums)
        if col in num_col:
            fig=pit.figure()
            sns.histplot(df[col].dropna(),kde=True)
            st.pyplot(fig)
        else:
            fig=plt.figure()
            df[col].value_counts().plot(kind='bar')
            plt.title(col)
            st.pyplot(fig)

        if num_col:
            st.header("7. corelation Matrix")
            corr = df[num_col].corr()
            fig = plt.figure(figsize=(10,6))
            sns.heatmap(corr,annot=True,cmap='coolwarm')
            st.pyplot(fig)
