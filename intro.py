"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st

# --- PAGE SETUP ---
home = st.Page(
    "pages/home.py",
    title="Home",
    icon=":material/cottage:",
    default=True,
)
meet = st.Page(
    "pages/meet.py",
    title="Meet",
    icon=":material/groups:",
)
chatbot = st.Page(
    "pages/YCP_Bot.py",
    title="YCP Bot",
    icon=":material/robot_2:",
)
partnerApps = st.Page(
    "pages/partnerApplication.py",
    title="Partner Application",
    icon=":material/article_shortcut:",
)
partners = st.Page(
    "pages/partners.py",
    title="Partners",
    icon=":material/handshake:",
)
makepost = st.Page(
    "pages/posts.py",
    title="Create Post",
    icon=":material/forum:",
)
sign_in = st.Page(
    "pages/sign_in.py",
    title="Sign In",
    icon=":material/login:",
)
account = st.Page(
    "pages/account.py",
    title="Account",
    icon=":material/account_circle:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Navigation": [home, meet, makepost, partners, partnerApps, chatbot],
        "Account": [account, sign_in],
    }
)



pg.run()
