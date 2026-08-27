import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Bird Monitoring Dashboard",
    page_icon="🐦",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    forest = pd.read_excel("Bird_Monitoring_Data_FOREST.XLSX")
    grassland = pd.read_excel("Bird_Monitoring_Data_GRASSLAND.XLSX")

    forest["Habitat"] = "Forest"
    grassland["Habitat"] = "Grassland"

    data = pd.concat([forest, grassland], ignore_index=True)

    return data


df = load_data()

# ---------------- TITLE ----------------
st.title("🐦 Bird Monitoring Dashboard")
st.markdown(
    "### Forest & Grassland Bird Observation Analysis"
)

st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔎 Filters")

# Year
years = sorted(df["Year"].dropna().unique())

selected_year = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

# Habitat
selected_habitat = st.sidebar.multiselect(
    "Select Habitat",
    df["Habitat"].unique(),
    default=df["Habitat"].unique()
)

# Sex
if "Sex" in df.columns:
    sex_values = df["Sex"].dropna().unique()

    selected_sex = st.sidebar.multiselect(
        "Select Sex",
        sex_values,
        default=sex_values
    )
else:
    selected_sex = []


# ---------------- FILTER DATA ----------------
filtered_df = df[
    (df["Year"].isin(selected_year)) &
    (df["Habitat"].isin(selected_habitat))
]

if "Sex" in df.columns and selected_sex:
    filtered_df = filtered_df[
        filtered_df["Sex"].isin(selected_sex)
    ]


# ---------------- KPI CALCULATIONS ----------------
total_records = len(filtered_df)

total_species = filtered_df["Scientific_Name"].nunique()

forest_records = len(
    filtered_df[filtered_df["Habitat"] == "Forest"]
)

grassland_records = len(
    filtered_df[filtered_df["Habitat"] == "Grassland"]
)


# ---------------- KPI CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🐦 Total Observations",
    f"{total_records:,}"
)

col2.metric(
    "🦜 Total Species",
    f"{total_species:,}"
)

col3.metric(
    "🌳 Forest Records",
    f"{forest_records:,}"
)

col4.metric(
    "🌾 Grassland Records",
    f"{grassland_records:,}"
)

st.divider()


# ==================================================
# ROW 1
# ==================================================

col1, col2 = st.columns(2)


# ---------------- TOP SPECIES ----------------
with col1:

    st.subheader("🐦 Top 10 Bird Species")

    species = (
        filtered_df["Common_Name"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    species.columns = ["Bird Species", "Observations"]

    fig1 = px.bar(
        species,
        x="Observations",
        y="Bird Species",
        orientation="h",
        title="Most Observed Bird Species"
    )

    fig1.update_layout(
        yaxis=dict(autorange="reversed"),
        height=450
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )


# ---------------- HABITAT ----------------
with col2:

    st.subheader("🌳 Habitat Comparison")

    habitat = (
        filtered_df["Habitat"]
        .value_counts()
        .reset_index()
    )

    habitat.columns = ["Habitat", "Observations"]

    fig2 = px.pie(
        habitat,
        names="Habitat",
        values="Observations",
        hole=0.45,
        title="Forest vs Grassland"
    )

    fig2.update_layout(height=450)

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ==================================================
# ROW 2
# ==================================================

col1, col2 = st.columns(2)


# ---------------- YEAR ANALYSIS ----------------
with col1:

    st.subheader("📈 Year-wise Observations")

    yearly = (
        filtered_df["Year"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    yearly.columns = ["Year", "Observations"]

    fig3 = px.line(
        yearly,
        x="Year",
        y="Observations",
        markers=True,
        title="Bird Observations by Year"
    )

    fig3.update_layout(height=400)

    st.plotly_chart(
        fig3,
        use_container_width=True
    )


# ---------------- SEX DISTRIBUTION ----------------
with col2:

    st.subheader("⚥ Sex Distribution")

    if "Sex" in filtered_df.columns:

        sex_data = (
            filtered_df["Sex"]
            .value_counts()
            .reset_index()
        )

        sex_data.columns = ["Sex", "Count"]

        fig4 = px.pie(
            sex_data,
            names="Sex",
            values="Count",
            hole=0.4,
            title="Bird Sex Distribution"
        )

        fig4.update_layout(height=400)

        st.plotly_chart(
            fig4,
            use_container_width=True
        )


# ==================================================
# ROW 3
# ==================================================

st.subheader("🌳 Bird Species by Habitat")

habitat_species = (
    filtered_df
    .groupby(["Habitat", "Common_Name"])
    .size()
    .reset_index(name="Observations")
)

top_habitat_species = (
    habitat_species
    .sort_values("Observations", ascending=False)
    .head(15)
)

fig5 = px.bar(
    top_habitat_species,
    x="Common_Name",
    y="Observations",
    color="Habitat",
    title="Bird Species Observations by Habitat"
)

fig5.update_layout(
    xaxis_title="Bird Species",
    yaxis_title="Observations",
    height=500
)

st.plotly_chart(
    fig5,
    use_container_width=True
)


# ==================================================
# ROW 4
# ==================================================

col1, col2 = st.columns(2)


# ---------------- LOCATION TYPE ----------------
with col1:

    st.subheader("📍 Location Type")

    if "Location_Type" in filtered_df.columns:

        location_data = (
            filtered_df["Location_Type"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        location_data.columns = [
            "Location Type",
            "Observations"
        ]

        fig6 = px.bar(
            location_data,
            x="Location Type",
            y="Observations",
            title="Observations by Location Type"
        )

        fig6.update_layout(height=400)

        st.plotly_chart(
            fig6,
            use_container_width=True
        )


# ---------------- DISTANCE ----------------
with col2:

    st.subheader("📏 Observation Distance")

    if "Distance" in filtered_df.columns:

        distance_data = pd.to_numeric(
            filtered_df["Distance"],
            errors="coerce"
        ).dropna()

        fig7 = px.histogram(
            distance_data,
            x=distance_data,
            nbins=20,
            title="Distance Distribution"
        )

        fig7.update_layout(
            xaxis_title="Distance",
            yaxis_title="Number of Observations",
            height=400
        )

        st.plotly_chart(
            fig7,
            use_container_width=True
        )


# ==================================================
# DATA TABLE
# ==================================================

st.divider()

st.subheader("📋 Bird Monitoring Data")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)

st.caption(
    f"Showing {len(filtered_df):,} observations"
)