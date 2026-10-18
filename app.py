
import streamlit as st
import pandas as pd

# Configure the dashboard page
st.set_page_config(
    page_title="EV Market Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Keep the dashboard design consistent


st.markdown("""
<style>
    /* Dark dashboard background */
    .stApp {
        background-color: #0b1220;
        color: #e5e7eb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Headings */
    h1, h2, h3 {
        color: #f8fafc !important;
    }

    /* KPI cards */
    [data-testid="stMetric"] {
        background-color: #17251f;
        border: 1px solid #285943;
        padding: 20px;
        border-radius: 14px;
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricValue"],
    [data-testid="stMetricDelta"] {
        color: #f8fafc !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111b2b;
    }

    /* General text */
    .stMarkdown p,
    label,
    [data-testid="stCaptionContainer"] {
        color: #cbd5e1 !important;
    }

    /* Filter controls */
    [data-baseweb="select"] > div {
        background-color: #1e293b;
        border-color: #475569;
    }

    /* Separators */
    hr {
        border-color: #334155;
    }
</style>
""", unsafe_allow_html=True)




# Load the cleaned dataset and cache it
@st.cache_data
def load_data():
    return pd.read_csv("data/clean/ev_population_clean.csv")


df = load_data()

# Prepare the model-year column for filtering
df["Model Year"] = pd.to_numeric(
    df["Model Year"], errors="coerce"
)

# Show the dashboard heading
st.title("⚡ EV Market Intelligence")
st.caption(
    "Explore electric vehicle records and manufacturer trends."
)

# Add navigation to the sidebar
st.sidebar.title("⚡ EV Explorer")

page = st.sidebar.radio(
    "Navigate",
    ["Overview", "Manufacturer Analysis", "Data Explorer"]
)

# Build interactive filters in the sidebar
st.sidebar.divider()
st.sidebar.subheader("Data Filters")

counties = sorted(df["County"].dropna().unique().tolist())
makes = sorted(df["Make"].dropna().unique().tolist())
vehicle_types = sorted(
    df["Electric Vehicle Type"].dropna().unique().tolist()
)

selected_counties = st.sidebar.multiselect(
    "County",
    options=counties,
    placeholder="All counties"
)

selected_makes = st.sidebar.multiselect(
    "Manufacturer",
    options=makes,
    placeholder="All manufacturers"
)

selected_types = st.sidebar.multiselect(
    "Vehicle Type",
    options=vehicle_types,
    placeholder="All vehicle types"
)

# Create a slider for the available model years
valid_years = df["Model Year"].dropna()

if not valid_years.empty:
    min_year = int(valid_years.min())
    max_year = int(valid_years.max())

    selected_years = st.sidebar.slider(
        "Model Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        step=1
    )
else:
    selected_years = None

# Apply the selected filters to the dataset
filtered_df = df.copy()

if selected_counties:
    filtered_df = filtered_df[
        filtered_df["County"].isin(selected_counties)
    ]

if selected_makes:
    filtered_df = filtered_df[
        filtered_df["Make"].isin(selected_makes)
    ]

if selected_types:
    filtered_df = filtered_df[
        filtered_df["Electric Vehicle Type"].isin(selected_types)
    ]

if selected_years is not None:
    filtered_df = filtered_df[
        filtered_df["Model Year"].between(
            selected_years[0], selected_years[1]
        )
    ]

# Display metrics based on the filtered data
st.subheader("Market Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Filtered Records", f"{len(filtered_df):,}")
col2.metric("Manufacturers", f"{filtered_df['Make'].nunique():,}")
col3.metric("Vehicle Models", f"{filtered_df['Model'].nunique():,}")
col4.metric("Counties", f"{filtered_df['County'].nunique():,}")

st.caption(
    "Counts reflect the selected records, not necessarily EV sales "
    "or registrations during each model year."
)

st.divider()

# Display charts for the selected dashboard page
if page == "Overview":

    left, right = st.columns(2, gap="large")

    with left:
        st.subheader("Vehicle Type Distribution")
        type_counts = filtered_df["Electric Vehicle Type"].value_counts()
        st.bar_chart(type_counts, color="#23866b")

    with right:
        st.subheader("Records by Model Year")
        year_counts = (
            filtered_df["Model Year"]
            .dropna()
            .astype(int)
            .value_counts()
            .sort_index()
        )
        st.line_chart(year_counts, color="#2675b8")

    st.subheader("Top 10 Manufacturers")

    top_makes = (
        filtered_df["Make"]
        .value_counts()
        .head(10)
        .sort_values()
    )

    st.bar_chart(
        top_makes,
        horizontal=True,
        color="#23866b"
    )

elif page == "Manufacturer Analysis":

    st.subheader("Manufacturer Analysis")

    top_makes = (
        filtered_df["Make"]
        .value_counts()
        .head(10)
        .sort_values()
    )

    st.bar_chart(
        top_makes,
        horizontal=True,
        color="#23866b"
    )

    st.subheader("Top 10 EV Models")

    top_models = (
        filtered_df["Model"]
        .value_counts()
        .head(10)
        .sort_values()
    )

    st.bar_chart(
        top_models,
        horizontal=True,
        color="#2675b8"
    )

elif page == "Data Explorer":

    st.subheader("Explore Vehicle Records")

    st.write(
        f"Your filters currently match **{len(filtered_df):,} records**."
    )

    # Prepare a CSV file from the filtered records
    csv_data = filtered_df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label="⬇️ Download Filtered Data (CSV)",
        data=csv_data,
        file_name="filtered_ev_data.csv",
        mime="text/csv"
    )

    # Display a manageable preview of the filtered data
    st.dataframe(
        filtered_df.head(1000),
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "The table previews up to 1,000 rows. "
        "The CSV download contains all matching rows."
    )
