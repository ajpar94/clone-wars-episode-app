import streamlit as st
import pandas as pd
st.set_page_config(page_title='The Clone Wars | Viewing Order', layout="wide", page_icon="images/favicon.png")

css='''
<style>
    section.main > div {max-width:70rem}
</style>
'''
st.markdown(css, unsafe_allow_html=True)

def cw_header(url):
    st.markdown(f'**<p style="color:#43a5cf;font-size:24px;border-radius:2%;">{url}</p>**', unsafe_allow_html=True)

def cw_header_faded(url):
    st.markdown(f'**<p style="color:#43a5cf;font-size:24px;border-radius:2%;opacity:0.5">{url}</p>**', unsafe_allow_html=True)

def quote(q):
    st.markdown(f'<p style="color:#43a5cf;">{q}</p>', unsafe_allow_html=True)


# -------------------------------------------- The Clone Wars -------------------------------------------
cw = pd.read_csv("cw_episodes.tsv", sep="\t")
cw.fillna("", inplace=True)

st.image("images/title.png")


st.markdown('''
<p align="center" style="color: #FFC62D;">
This is my personal <i>Star Wars: The Clone Wars</i> episode order that skips over weaker or less relevant episodes and includes additional material from story reels and comics.  
Episodes are grouped into story arcs and don't necessarily follow the chronological order, aiming to bring out the best of the series and make the story feel more cohesive and impactful.
This list also includes links to episode guides and streaming options on Disney+ or YouTube.</p>
''', unsafe_allow_html=True)

arc = ""

for i, row in cw.iterrows():
    if row["arc_name"] != arc:
        if row['arc_name'].endswith("*"):
            cw_header_faded(f"{row['arc_name'][:-1]}")
        else:
            cw_header(f"{row['arc_name']}")
    arc = row["arc_name"]

    if row['season'] != ".":
        prefix = f"{row['season']}_{str.zfill(str(row['episode']), 2)} | "
    else:
        prefix = ""
    with st.expander(prefix + row['title']):
        col1, col2 = st.columns([10,18])
        with col1:
            img = f"images/{row['title'].lower().replace(' ', '_')}.png"
            st.image(img)
        with col2:
            if (q := row['quote']) != ".":
                quote(q.upper())
            st.write(row['desc'])
            st.markdown(f"[Episode Guide]({row['url']}) | [Stream]({row['stream']})")