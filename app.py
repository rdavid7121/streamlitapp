import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":white_check_mark:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_tfb3estd.json")
img_contact_form = Image.open("images/ied.jpg")
img_lottie_animation = Image.open("images/wdm.jpeg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am David :wave:")
    st.title("Aspiring Python Developer")
    st.write(
        "Carrying passion in every line of code | Self learner."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Being a fresher, I think I am very flexible and adaptive to learning new things.
            I wish to Secure a responsible career opportunity to fully utilize my training and skills and improve them, 
            while making a significant contribution to organizational goals and mine. 
            I am sure I will be able to contribute something capable for the growth of the company.
            I can also understand and implement processes easily as I have a good grasping quality.
            If I am hired, I will do my best to benefit the company and add value to it. 
            I would also like to learn and sharpen my skills under the guidance of professionals working with your team. 
            Love to learn and work in new technology.
            """
        )
        st.write("[LinkedIn >](https://www.linkedin.com/in/rdavid7121/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("DESIGN AND FABRICATION OF WEEDING MACHINE")
        st.write(
            """
            Removing weeds in agricultural field becomes a costlier affair. 
            In order to address this problem, 
            this project proposes a simple, economical and efficient machine to remove the weed, 
            which would be operated by a single person savings of labor as well as time.
            """
        )
        st.markdown("[Watch Video...](https://drive.google.com/file/d/1uzhQaXPQkiQ9Zf5aQUapi60wAyA-H-oH/view?usp=sharing)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("IMPROVISED SURVEILLANCE AND EXPLOSIVE DETECTIVE USING ROBOTIC CRAWLER")
        st.write(
            """
            In the exact scenario, there are lots of attacks and it results in major of loss of lives 
            so there is a plan to create an Improvised Explosive Detective (IED) Robotic Crawler that may identify the explosives 
            that were present on the surface as well as buried underground.
            """
        )
        st.markdown("[Watch Video...]()")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/rdavid7121@gmail.com" 
    method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


