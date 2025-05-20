import streamlit as st
import pandas as pd
import json

# --- Data ---
# Use the provided JSON data directly as a Python dictionary
data = {
    "career": [
        {
            "position": "Direktör",
            "start_year": 1904,
            "end_year": None,
            "organization": None,
            "location": {
                "name": "Norrviken, Båstad",
                "latitude": 56.4459664,
                "longitude": 12.7979674,
                "formatted_address": "Norrviken Gardens, Kattviksvägen 233, 269 91 Båstad, Sweden"
            }
        }
    ],
    "person": {
        "first_name": "Rudolf",
        "last_name": "Abelin",
        "middle_name": None,
        "gender": "Male",
        "birth_date": "30-05-1904", # Assuming YYYY-MM-DD might be intended, but using as given
        "birth_place": {
            "name": "Malmö",
            "latitude": 55.604981,
            "longitude": 13.003822,
            "formatted_address": "Malmö, Sweden"
        },
        "death_date": None,
        "death_place": None,
        "occupation": {
            "occupation": "Direktör",
            "occupation_english": "Director",
            "hisco_code_swedish": "21110.0",
            "hisco_description_swedish": "General Manager",
            "hisco_code_english": "21000.0",
            "hisco_description_english": "Manager, Specialisation Unknown"
        },
        "parents": [
            {
                "first_name": "G.R.A.",
                "last_name": "Abelin",
                "middle_name": None,
                "gender": "Male",
                "occupation": {
                    "occupation": "Generallöjtnant",
                    "occupation_english": "Lieutenant General",
                    "hisco_code_swedish": "58320.0",
                    "hisco_description_swedish": "Officer",
                    "hisco_code_english": "58320.0",
                    "hisco_description_english": "Officer"
                }
            },
            {
                "first_name": "Charlotta",
                "last_name": "Zethelius",
                "middle_name": "E.",
                "gender": "Female",
                "occupation": None
            }
        ]
    },
    "academic_positions": None,
    "achievements": [
        {
            "title": "Anlade Norrvikens fruktträdgård vid Bråviken och Norrviken vid Båstad",
            "field": "Trädgårdsarkitektur",
            "year": None,
            "significance": "Banbrytare för rationell fruktodling i Sverige",
            "recognized_by": None
        }
    ],
    "awards": [
        "Flera högsta pris i in- och utländska fruktutställningar"
    ],
    "board_memberships": None,
    "committee_memberships": None,
    "community_involvement": None,
    "current_location": {
        "name": "Norrviken, Båstad",
        "latitude": 56.4459664,
        "longitude": 12.7979674,
        "formatted_address": "Norrviken Gardens, Kattviksvägen 233, 269 91 Båstad, Sweden"
    },
    "education": [
        {
            "degree": "Studier",
            "degree_level": "Schooling",
            "year": "None", # Handling string "None"
            "institution": "Rosenborgs slottsträdgård, Danmark"
        }
    ],
    "family": {
        "spouse": {
            "first_name": "Signe",
            "last_name": "Ziedner",
            "middle_name": "Margareta Kristina",
            "gender": "Female",
            "birth_date": None,
            "birth_place": None,
            "death_date": None,
            "death_place": None,
            "occupation": None,
            "parents": [
                {
                    "first_name": "Edvard",
                    "last_name": "Ziedner",
                    "middle_name": None,
                    "gender": "Male",
                    "occupation": {
                        "occupation": "Redaktör",
                        "occupation_english": "Editor",
                        "hisco_code_swedish": "15920.0",
                        "hisco_description_swedish": "Editor, Newspapers and Periodicals",
                        "hisco_code_english": "15120.0",
                        "hisco_description_english": "Author"
                    }
                }
                # Potentially missing mother data here
            ]
        },
        "marriage_year": "1909",
        "divorce_year": None,
        "children": None
    },
    "hobbies": None,
    "honorary_titles": None,
    "honors": None,
    "languages_spoken": None,
    "leadership_roles": None,
    "military_service": None,
    "political_positions": None,
    "publications": [
        {
            "title": "Den mindre trädgården",
            "year": "1902",
            "type": "book",
            "editions": [
                {
                    "edition_number": "upplaga 6",
                    "year": "None",
                    "publisher": None,
                    "notes": None
                }
            ],
            "publisher": None,
            "reception": None,
            "signature": None,
            "volumes": None
        },
        {
            "title": "Om frukt och fruktträdsodling",
            "year": "1902",
            "type": "book",
            "editions": [
                {
                    "edition_number": "upplaga 2",
                    "year": "None",
                    "publisher": None,
                    "notes": None
                }
            ],
            "publisher": None,
            "reception": None,
            "signature": None,
            "volumes": None
        },
        {
            "title": "Villaträdgården",
            "year": "1903",
            "type": "book",
            "editions": [
                {
                    "edition_number": "upplaga 2",
                    "year": "None",
                    "publisher": None,
                    "notes": None
                }
            ],
            "publisher": None,
            "reception": None,
            "signature": None,
            "volumes": None
        },
        {
            "title": "Lekstugans trädgård",
            "year": "1906",
            "type": "book",
            "editions": None,
            "publisher": None,
            "reception": None,
            "signature": None,
            "volumes": None
        },
        {
            "title": "Trädgård inomhus",
            "year": "None",
            "type": "book",
            "editions": [
                {
                    "edition_number": "upplaga 2",
                    "year": "None",
                    "publisher": None,
                    "notes": None
                }
            ],
            "publisher": None,
            "reception": None,
            "signature": None,
            "volumes": None
        },
        {
            "title": "Privatträdgårds kalender",
            "year": "1911",
            "type": "book",
            "editions": None,
            "publisher": None,
            "reception": None,
            "signature": None,
            "volumes": None
        },
        {
            "title": "Herrgårdsträdgården",
            "year": "1915",
            "type": "book",
            "editions": None,
            "publisher": None,
            "reception": None,
            "signature": None,
            "volumes": None
        }
    ],
    "travels": None
}

# --- Helper Functions ---
def display_location(location_data, label="Location"):
    """Displays location name, address, and map if available."""
    if location_data:
        st.markdown(f"**{label}:** {location_data.get('name', 'N/A')}")
        if location_data.get('formatted_address'):
            st.caption(f"Address: {location_data['formatted_address']}")
        if location_data.get('latitude') and location_data.get('longitude'):
            loc_df = pd.DataFrame({
                'lat': [location_data['latitude']],
                'lon': [location_data['longitude']]
            })
            st.map(loc_df, zoom=10)
        else:
             st.caption("(Map data not available)")

def format_name(person_dict):
    """Formats a person's full name."""
    parts = [
        person_dict.get('first_name'),
        person_dict.get('middle_name'),
        person_dict.get('last_name')
    ]
    return " ".join(part for part in parts if part)

def display_occupation(occupation_data, label="Occupation"):
     """Displays occupation details."""
     if occupation_data:
        st.markdown(f"**{label}:** {occupation_data.get('occupation', 'N/A')} ({occupation_data.get('occupation_english', 'N/A')})")
        if occupation_data.get('hisco_description_swedish'):
            st.caption(f"HISCO (SV): {occupation_data.get('hisco_code_swedish', '')} - {occupation_data.get('hisco_description_swedish', '')}")
        if occupation_data.get('hisco_description_english'):
            st.caption(f"HISCO (EN): {occupation_data.get('hisco_code_english', '')} - {occupation_data.get('hisco_description_english', '')}")

def safe_get(data, key, default="N/A"):
    """Safely get a value from a dict, returning default if None or key missing."""
    value = data.get(key)
    return value if value is not None else default

# --- Streamlit App Layout ---

st.set_page_config(layout="wide")
st.title("Biographical Explorer")

# --- Person Section ---
person_info = data.get("person")
if person_info:
    full_name = format_name(person_info)
    st.header(full_name)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Personal Information")
        st.markdown(f"**Full Name:** {full_name}")
        st.markdown(f"**Gender:** {safe_get(person_info, 'gender')}")

        # Dates and Places
        if person_info.get('birth_date'):
            st.markdown(f"**Born:** {person_info['birth_date']}")
            display_location(person_info.get('birth_place'), label="Birth Place")
        else:
            st.markdown("**Born:** N/A")

        if person_info.get('death_date'):
            st.markdown(f"**Died:** {person_info['death_date']}")
            display_location(person_info.get('death_place'), label="Death Place")
        # else: # Optional: Display if still alive or date unknown
        #     st.markdown("**Died:** N/A")

        # Occupation
        display_occupation(person_info.get('occupation'))

    with col2:
        st.subheader("Family")
        # Parents
        parents = person_info.get("parents")
        if parents:
            with st.expander("Parents"):
                for parent in parents:
                    parent_name = format_name(parent)
                    st.markdown(f"**{parent.get('gender', 'Parent')}:** {parent_name}")
                    display_occupation(parent.get('occupation'), label="Parent's Occupation")
                    st.divider()

        # Spouse and Marriage
        family_info = data.get("family")
        if family_info:
            spouse = family_info.get("spouse")
            if spouse:
                st.markdown(f"**Spouse:** {format_name(spouse)}")
                if family_info.get('marriage_year'):
                    st.markdown(f"**Married:** {family_info['marriage_year']}")
                if family_info.get('divorce_year'):
                    st.markdown(f"**Divorced:** {family_info['divorce_year']}")

                with st.expander("Spouse Details"):
                    st.markdown(f"**Gender:** {safe_get(spouse, 'gender')}")
                    # Add more spouse details if needed (birth/death, etc.)
                    display_occupation(spouse.get('occupation'), label="Spouse's Occupation")
                    spouse_parents = spouse.get("parents")
                    if spouse_parents:
                        st.markdown("**Spouse's Parents:**")
                        for sp_parent in spouse_parents:
                            st.markdown(f"- {format_name(sp_parent)}")
                            display_occupation(sp_parent.get('occupation'), label="Occupation")


            # Children
            children = family_info.get("children")
            if children: # Assuming children would be a list if present
                st.markdown("**Children:**")
                # Logic to display children if data format was known
                # Example: for child in children: st.write(f"- {format_name(child)}")
            # else:
            #     st.markdown("**Children:** N/A") # Or None specified

        # Current Location (if different from last known career location)
        current_loc = data.get("current_location")
        if current_loc:
            st.subheader("Current Known Location")
            display_location(current_loc)


st.divider() # Visually separate sections

# --- Career Section ---
career_info = data.get("career")
if career_info:
    st.subheader("Career")
    # Prepare data for DataFrame
    career_data_for_df = []
    for entry in career_info:
        loc_name = entry.get('location', {}).get('name', 'N/A') if entry.get('location') else 'N/A'
        career_data_for_df.append({
            "Position": safe_get(entry, 'position'),
            "Start Year": safe_get(entry, 'start_year'),
            "End Year": safe_get(entry, 'end_year', '-'), # Use '-' for ongoing/unknown
            "Organization": safe_get(entry, 'organization'),
            "Location": loc_name
        })

    if career_data_for_df:
        df_career = pd.DataFrame(career_data_for_df)
        st.dataframe(df_career, hide_index=True)

    # Optionally display map for the first/last career location with coordinates
    first_career_loc_with_coords = next((entry['location'] for entry in career_info if entry.get('location') and entry['location'].get('latitude')), None)
    if first_career_loc_with_coords:
         with st.expander("Career Location Map (Example: First Entry with Coords)"):
              display_location(first_career_loc_with_coords)


st.divider()

# --- Education Section ---
education_info = data.get("education")
if education_info:
    st.subheader("Education")
    edu_data_for_df = []
    for entry in education_info:
         # Handle year being 'None' string
         year = safe_get(entry, 'year')
         if isinstance(year, str) and year.lower() == 'none':
             year = "N/A"

         edu_data_for_df.append({
            "Degree/Level": f"{safe_get(entry, 'degree')} ({safe_get(entry, 'degree_level')})",
            "Institution": safe_get(entry, 'institution'),
            "Year": year,
         })

    if edu_data_for_df:
        df_edu = pd.DataFrame(edu_data_for_df)
        st.dataframe(df_edu, hide_index=True)

st.divider()

# --- Achievements Section ---
achievements_info = data.get("achievements")
if achievements_info:
    st.subheader("Achievements")
    for ach in achievements_info:
        with st.container(border=True): # Use border for visual separation
            st.markdown(f"**Title:** {safe_get(ach, 'title')}")
            st.markdown(f"**Field:** {safe_get(ach, 'field')}")
            st.markdown(f"**Significance:** {safe_get(ach, 'significance')}")
            if ach.get('year') and str(ach.get('year')).lower() != 'none':
                 st.markdown(f"**Year:** {ach['year']}")
            if ach.get('recognized_by'):
                 st.markdown(f"**Recognized By:** {ach['recognized_by']}")
        # st.divider() # Use divider or border within container

st.divider()

# --- Awards Section ---
awards_info = data.get("awards")
if awards_info:
    st.subheader("Awards")
    for award in awards_info:
        st.markdown(f"- {award}")

st.divider()

# --- Publications Section ---
publications_info = data.get("publications")
if publications_info:
    st.subheader("Publications")
    pub_data_for_df = []
    for pub in publications_info:
        year = safe_get(pub, 'year')
        if isinstance(year, str) and year.lower() == 'none':
             year = "N/A"

        edition_info = ""
        if pub.get('editions'):
             editions = []
             for ed in pub['editions']:
                 ed_year = safe_get(ed, 'year')
                 if isinstance(ed_year, str) and ed_year.lower() == 'none':
                     ed_year = "" # Don't show 'None' year for edition
                 ed_str = safe_get(ed, 'edition_number')
                 if ed_year:
                     ed_str += f" ({ed_year})"
                 editions.append(ed_str)
             edition_info = "; ".join(editions)


        pub_data_for_df.append({
            "Title": safe_get(pub, 'title'),
            "Year": year,
            "Type": safe_get(pub, 'type'),
            "Editions": edition_info if edition_info else "N/A",
            "Publisher": safe_get(pub, 'publisher')
        })

    if pub_data_for_df:
        df_pub = pd.DataFrame(pub_data_for_df)
        st.dataframe(df_pub, hide_index=True, use_container_width=True)

st.divider()

# --- Displaying Other Sections (if they exist and are simple lists/values) ---
# Example for a simple list section (like hypothetical 'languages_spoken')
# languages = data.get("languages_spoken")
# if languages:
#     st.subheader("Languages Spoken")
#     for lang in languages:
#         st.markdown(f"- {lang}")

# Example for simple key-value pairs (like hypothetical 'honorary_titles')
# titles = data.get("honorary_titles")
# if titles:
#     st.subheader("Honorary Titles")
#     if isinstance(titles, list): # Check if it's a list
#         for title in titles:
#              st.markdown(f"- {title}")
#     elif isinstance(titles, str): # Check if it's just a string
#          st.markdown(titles)
#     # Add more type checks if needed


# --- Optional: Raw Data Viewer ---
with st.expander("View Raw JSON Data"):
    st.json(data)