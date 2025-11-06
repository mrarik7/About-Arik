import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "quiz"
def go_to(page):
    st.session_state.page = page

if st.session_state.page == "quiz":
    a = 'zoro'
    st.header("welcome to 'ABOUT ARIK'")
    st.text('if you want to know about my details.you have to answer a simple question:)')
    b = st.text_input('what is my favourite anime charecter ?')
    b = b.lower()
    if b:
        if b == a:
            st.success('you are right buddy:')
            if st.button('click me for more details:)'):
                go_to('page2')

elif st.session_state.page == "page2":
    st.title("🎉here you can find all about me:)")
    st.text('Heyooo 👋😄\nI’m Arik 🌙✨ (aka nothing… cuz I’m mysterious like that 👀)\nI made this lil web app so you can know me a tiny bit 💗\nFor now, my socials are here 📱💬\nMore cool stuff coming soon… maybe 😌💫')
    s1='📸instagram'
    s2='📘facebook'
    s3='📞whatsapp'
    s4='✈️telegram'
    x=st.selectbox('my social media accounts',('🖲️click👇',s1,s2,s3,s4))
    if s1:
        if x == s1:
            st.markdown("[📸instagram:tarek amin arik](https://www.instagram.com/mr.arik7/?hl=en)")
    if s2:
        if x == s2:
            st.text('my fb account is currently deactivated:)')
    if s3:
        if x == s3:
            st.markdown('[📞whatsapp:01327329596(arik)](https://wa.me/01327329596)')
    if s4:
        if x == s4:

            st.markdown('[✈️telegram:tarek amin arik](http://t.me/mr_arik7)')
