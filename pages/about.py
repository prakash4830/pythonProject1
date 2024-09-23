import streamlit as st
from PIL import Image, ImageDraw


def make_circle(image):
    width, height = image.size
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)

    circular_image = Image.new("RGBA", (width, height))
    circular_image.paste(image, (0, 0), mask)
    return circular_image


# Developer information
developers = [
    {
        "name": "Jayaprakash S",
        "bio": "Brief bio or information about Jayaprakash S djbhgjkef jfgerkgjh ejfhgk",
        "image_path": "images/pic_1.png"
    },
    {
        "name": "Sandeep Murugasan",
        "bio": "Brief bio or information about Sandeep Murugasan jhfbgkjefh jegkjeh jkerhgkj",
        "image_path": "images/pic_2.png"
    }
]

st.markdown("<h3 style='text-align: center;'>About the Developers</h3>", unsafe_allow_html=True)

# Create two columns for the profiles
col1, col2 = st.columns(2, gap="large", vertical_alignment="center")
with col1:
    image = Image.open("images/pic_1.png")
    circular_image = make_circle(image.resize((230, 260)))
    st.image(circular_image)
    st.subheader("Jayaprakash S")
    st.write(
        "- MBA student at VIT BS"
    )
    st.write("\n")
    st.subheader("Contact Information", anchor=False)
    st.write(
        """ 
        - **Mobile:** +91-8754813384
        - **Email:** [prakash4830jp@gmail.com](mailto:prakash4830jp@gmail.com)
        - **LinkedIn:** [linkedin.com/in/jayaprakash-s/](https://www.linkedin.com/in/jayaprakash-s/)
        - **GitHub:** [github.com/prakash4830](https://github.com/prakash4830)
        """
    )

# --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Qualifications", anchor=False)
    st.write(
        """
        - Computer Science and Engineering 

        """
    )
    st.subheader("Experience", anchor=False)
    st.write(
        """
        - 18 months of Experience at Wipro Technologies as Analyst

        """
    )
    st.subheader("Internship", anchor=False)
    st.write(
        """
        - 3 Months internship at The Bank of New York Mellon
        
        - 6 Months internship at Wipro Technologies
        """
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Technical Skills", anchor=False)
    st.write(
        """
        - **Programming:** Python (Scikit-learn, Pandas, Numpy, Streamlit), R
        - **Data Visualization:** PowerBI, Plotly
        - **Modeling:** Logistic regression, linear regression, decision trees, K-Mean Clustering, Principal Component Analysis
        - **Databases:** MySQL
        - **RPA:** Automation Anywhere Developer
        - **Analytical Tool:** Altrix
        """
    )

    st.write("\n")
    st.subheader("Other Interest and Hobbies", anchor=False)
    st.write(
        """
                - Travelling and exploring new places
                - Learning new technologies
        """
    )

with col2:
    image = Image.open("images/pic_2.png")
    circular_image = make_circle(image.resize((230, 260)))
    st.image(circular_image)
    st.subheader("Sandeep Murugasan")
    st.write(
        "MBA student at VIT University"
    )

        # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications", anchor=False)
    st.write(
        """
        - 7 Years experience extracting actionable insights from data
        - Strong hands-on experience and knowledge in Python and Excel
        - Good understanding of statistical principles and their respective applications
        - Excellent team-player and displaying a strong sense of initiative on tasks
        """
    )
    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills", anchor=False)
    st.write(
        """
        - Programming: Python (Scikit-learn, Pandas), SQL, VBA
        - Data Visualization: PowerBi, MS Excel, Plotly
        - Modeling: Logistic regression, linear regression, decision trees
        - Databases: Postgres, MongoDB, MySQL
        """
    )
