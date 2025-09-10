import streamlit as st
from dotenv import load_dotenv
import os
from chains import init_llm, get_post_chain
from utilis import check_media_relevance


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("❌ GOOGLE_API_KEY not found in .env or Streamlit Secrets")
    st.stop()


llm = init_llm()
post_chain = get_post_chain(llm)


st.set_page_config(page_title="LinkedIn Post Generator", layout="wide")
st.title("LinkedIn Post Generator - AI Writer")
st.write("Generate LinkedIn posts")

# Inputs
writing_samples = st.text_area("✍️ Paste your LinkedIn posts or writing samples here:", height=200)
topic = st.text_input("💡 What’s the topic/idea for your new LinkedIn post? (Eg AI_music maker )")
uploaded_file = st.file_uploader("📎 Upload Image or Video", type=["png", "jpg", "jpeg", "mp4", "mov"])

if st.button("🚀 Generate Post"):
    if topic and writing_samples:
        # Generate post
        output = post_chain.run({"samples": writing_samples, "topic": topic})
        st.subheader("📝 Generated LinkedIn Post")
        st.write(output)

        # Check relevance of media if uploaded
        if uploaded_file:
            st.subheader("📎 Uploaded Media")
            relevance = check_media_relevance(llm, output, uploaded_file.name)

            if relevance == "Relevant":
                if uploaded_file.type.startswith("image"):
                    st.image(uploaded_file)
                else:
                    st.video(uploaded_file)
                st.success("✅ Media is relevant to the post.")
            else:
                st.warning("⚠️ Media seems not relevant to the post. Consider uploading another file.")
    else:
        st.warning("Please enter both writing samples and a topic.")
