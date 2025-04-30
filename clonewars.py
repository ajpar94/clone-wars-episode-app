import streamlit as st
import pandas as pd
st.set_page_config(page_title='The Clone Wars | Viewing Order', layout="wide", page_icon="images/favicon.png")

css='''
<style>
    section.stMain > div {max-width:70rem}
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
This list also includes links to episode guides, fan-edits, and streaming options on Disney+ or YouTube.</p>
''', unsafe_allow_html=True)

arc = "Jedi Missions"

cw_header(arc)
tabA, tabB = st.tabs(["Original", "Fan-Edit"])

with tabA:
    with st.expander("Star Wars: The Clone Wars (Film)"):
        col1, col2 = st.columns([10,18])
        with col1:
            img = "images/pilot.png"
            st.image(img)
        row = cw.iloc[0]
        with col2:
            if (q := row['quote']) != ".":
                quote(q.upper())
            st.write(row['desc'])
            st.markdown(f"[Episode Guide]({row['url']}) | [Stream]({row['stream']})")

with tabB:
    with st.expander("Star Wars: The Clone Wars (Battle of Christophsis)"):
        col1, col2 = st.columns([10,18])
        with col1:
            img = "images/artwork.png"
            st.image(img)
        row = cw.iloc[0]
        with col2:
            if (q := row['quote']) != ".":
                quote(q.upper())
            st.write("The Clone Wars movie stripped down to a ~20 minute-long story that serves perfectly as the pilot episode. \n\nAnakin and Obi-Wan continue to fight on the frontlines in the Battle of Christophsis when they are surprised by a new visitor sent by the Jedi Council -- Padawan Ahsoka Tano.")
            st.markdown(f"[Fan-Edit](https://originaltrilogy.com/topic/The-Clone-Wars-S1E0-Battle-of-Christophsis-Released/id/134671)")

for i, row in cw[1:-4].iterrows():
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
    expander_title = prefix + row['title']
    with st.expander(expander_title):
        col1, col2 = st.columns([10,18])
        with col1:
            img = f"images/{row['title'].lower().replace(' ', '_')}.png"
            st.image(img)
        with col2:
            if (q := row['quote']) != ".":
                quote(q.upper())
            st.write(row['desc'])
            st.markdown(f"[Episode Guide]({row['url']}) | [Stream]({row['stream']})")


cw_header("Siege of Mandalore")
tab1, tab2 = st.tabs(["Original", "Fan-Edit"])

with tab2:
    with st.expander("Star Wars: The Clone Wars x Revenge of the Sith"):
        col1, col2 = st.columns([10,18])
        with col1:
            img = f"images/artwork2.png"
            st.image(img)
        with col2:
            quote(("It is in the darkest moments that the light within must shine the brightest").upper())
            st.write("A combination of the final arc (7_09 - 7_12) and Episode III - Revenge of the Sith, resulting in a 3.5h movie that concludes The Clone Wars.")
            st.markdown(f"[Fan-Edit](https://originaltrilogy.com/topic/The-Clone-Wars-Revenge-of-the-Sith-Extended-Edition-Released/id/124945)")
with tab1:
    for i, row in cw.tail(4).iterrows():
        if row['season'] != ".":
            prefix = f"{row['season']}_{str.zfill(str(row['episode']), 2)} | "
        else:
            prefix = ""
        expander_title = prefix + row['title']
        with st.expander(expander_title):
            col1, col2 = st.columns([10,18])
            with col1:
                img = f"images/{row['title'].lower().replace(' ', '_')}.png"
                st.image(img)
            with col2:
                if (q := row['quote']) != ".":
                    quote(q.upper())
                st.write(row['desc'])
                st.markdown(f"[Episode Guide]({row['url']}) | [Stream]({row['stream']})")


footer="""<style>
.footer {
position: relative;
width: 100%;
color: gray;
text-align: center;
margin-top: 140px;
margin-bottom: -180px;
}
</style>
<div class="footer">
<p style="font-size: 12px;">This website is a fanmade project and is not affiliated with any official brand, company, or copyright holder.<br/>
All images and media used on this site remain the property of their respective owners.<br/>
Please don't sue me - this is just for fun, not profit.</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
