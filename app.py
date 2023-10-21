from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Jillian Wangari CV.pdf"
profile_pic = current_dir / "assets" / "profile.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jillian Wangari Mwangi"
PAGE_ICON = ":wave:"
NAME = "Jillian Wangari Mwangi"
DESCRIPTION = """
Geospatial specialist, GIS and remote sensing expert.
"""
EMAIL = "jillianwangari98@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "http://linkedin.com/in/jillian-mwangi-wangari",
    "GitHub": "https://github.com/Jillian-glitch",
}
PROJECTS = {
    "🏆 CHIRTS temperature data cleaning and analysis": "https://github.com/Jillian-glitch/CHIRTS-Temperature-data-analysis",
    "🏆 Hyacinth biomass analysis - area calculation and analysis of hyacinth area in Lake victoria using GEE": "https://github.com/Jillian-glitch/Hyacinth_biomassarea-",
    "🏆 LULC classification analysis - lulc classification for upper tana catchment area in GEE": "https://github.com/Jillian-glitch/LULC-Classification-Google-Earth-Engine",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic )


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 2 Years expereince extracting actionable insights from spatial data.
- ✔️ Strong hands on experience and knowledge in various GIS software such as ArcGIS products, QGIS, python and GEE.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
- ✔️ Excellent communication skills to effectively communicate technical jargons to both non-technical and technical people.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (numpy, geopandas, gdal, geemap, rasterio, tensorflow), SQL, notebooks, R
- 📊 Software: ArcGIS products, QGIS, ERDAS Imagine, SNAP, Google earth engine, Geoserver
- 🗄️ Databases: Postgres
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("EXPERIENCE")
st.write("---")

# --- JOB 1
st.write("🚧", "**GIS Specialist | Kulea Limited**")
st.write("05/2023 - 06/2023")
st.write(
    """
- ► Developed and implemented a crop mapping model using machine learning algorithm and vegetation indices to accurately map crop types and, estimate production and acreage on an annual basis thereby significantly improving the company’s market intelligence by providing accurate and timely information for commodity trading purposes and reduce financial risk while increasing profitability.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**GIS Consultant/ Project manager | Sacchi and Partners**")
st.write("04/2021 - 03/2023")
st.write(
    """
- ► Regularly involved in company business meetings to outsource for new clients and seal deals that brought in almost 80% of company revenue. 
- ► Reduced rework by 40%, increasing customer satisfaction and streamlining project management processes. 
- ► Facilitated GIS education to colleagues, thus increasing the companies use of GIS tools amongst workers by more than half. 
- ► Successfully managed over 2 projects utilizing project management tools and integrating GIS solutions to ensure successful delivery of client requirements. 
- ► Increased project completion rate by 60%, reducing cost and project timeline from 6 weeks to 4 weeks. 
- ► Reviewed customer data and used classification algorithms such as decision tree to produce high accuracy predictive analysis of 78% and made recommendations for business strategies. 
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**GIS Intern | The Kenya Meteorological Department**")
st.write("08/2019 - 10/2019")
st.write(
    """
- ► Performed daily rainfall and temperature data recording so as to perform data analysis for flood forecasting. 
- ► Assisted in the generation of daily weather forecast maps 
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")