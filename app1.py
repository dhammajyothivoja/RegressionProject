import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def edaPage():
    st.title("Step-by-step Data Analysis")

    upload_file = st.sidebar.file_uploader("Upload your csv file", type=["csv"])
    if upload_file:
        df = pd.read_csv(upload_file)
        st.success("File uploaded successfully!")

        # Step 1: Basic info
        st.header("1. Dataset Overview")
        st.write("shape:", df.shape)
        st.write("Columns:", df.columns.tolist())
        st.dataframe(df.head())

        # Step 2: Missing values
        st.header("2. Missing Values")
        st.write(df.isnull().sum())

        # Step 3: Descriptive statistics
        st.header("3. Descriptive Statistics")
        st.dataframe(df.describe(include="all"))

        # Step 4: Column types
        st.header("4. Data Types")
        num_col = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        cat_cols = df.select_dtypes(include=["object"]).columns.tolist()
        st.write("Numerical Columns:", num_col)
        st.write("Categorical Columns:", cat_cols)

        # Step 5: Univariate plots
        st.header("5. Univariate Analysis")
        col = st.selectbox("select a column to plot", df.columns)
        if col in num_col:
            fig = plt.figure()
            sns.histplot(df[col].dropna(), kde=True)
            st.pyplot(fig)
        else:
            fig = plt.figure()
            df[col].value_counts().plot(kind='bar')
            plt.title(col)
            st.pyplot(fig)

        # Step 7: Correlation
        if num_col:
            st.header("7. Correlation Matrix")
            corr = df[num_col].corr()
            fig = plt.figure(figsize=(10, 6))
            sns.heatmap(corr, annot=True, cmap='coolwarm')
            st.pyplot(fig)

# To run the function if this file is executed directly
if __name__ == "__main__":
    edaPage()
