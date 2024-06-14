import streamlit as st
import os
import google.generativeai as genai
from apikey import google_gemini_api_key, openai_api_key
from openai import OpenAI
from streamlit_carousel import carousel

#client = OpenAI(api_key=os.environ.get(openai_api_key),)
client = OpenAI(api_key=openai_api_key)
genai.configure(api_key=google_gemini_api_key)

single_image=dict(
    title="",
    text="",
    interval=None,
    img="",
    )

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

#setting up our model
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

#layout
st.set_page_config(layout="wide")
with st.sidebar:
    st.text("Jinendra's Project")
    st.title("Input your blog details")
    st.subheader("Enter details of the blog you want to generate")
    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (Comma-Separated)")
    num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=50)
    num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)
    submit_button = st.button("Generate Blog")

    promt_parts =[
        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the Comtent is original. informative, and maintains a consistant tone throughout.",
    ]
    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "Generate a comprehensive, engaging blog post relevant to the given title \"Effects of Generative AI\" and keywords. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the Comtent is original. informative, and maintains a consistant tone throughout.",
            "Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the Comtent is original. informative, and maintains a consistant tone throughout.",
        ],
        },
        {
        "role": "model",
        "parts": [
            "## The Unleashing of Artificial Creativity: Exploring the Ripple Effects of Generative AI\n\nThe realm of science fiction is steadily bleeding into reality. We're no longer just marveling at machines that can compute at lightning speeds; we're witnessing the rise of a new era – one where Artificial Intelligence (AI) transcends mere logic and ventures into the uncharted territory of **artificial creativity**.  This is the domain of **Generative AI**, a subset of AI with the astonishing ability to generate new content – be it text, images, music, or even code – that mimics and often rivals human ingenuity. \n\nBut this brave new world comes with its own set of tremors, sending ripples across various facets of our lives. Let's delve into the profound **effects of generative AI**, exploring its potential to revolutionize industries, blur ethical lines, and redefine our understanding of creativity itself.\n\n**A Catalyst for Innovation:**\n\nImagine a world where tedious tasks are automated, freeing up human potential for higher pursuits. This is the promise of Generative AI. From writing compelling marketing copy to composing personalized music tracks, the **technology innovation**  fueled by generative AI is transforming industries at an unprecedented pace. Businesses can leverage these tools to streamline workflows, optimize processes, and unlock new levels of efficiency.  The creative industries, too, are experiencing a paradigm shift. Graphic designers can now use AI tools to generate unique visuals, while musicians can collaborate with AI algorithms to compose intricate melodies. This fusion of human and artificial creativity opens up exciting new avenues for artistic expression.\n\n**Navigating the Ethical Labyrinth:**\n\nHowever, this technological leap comes hand-in-hand with complex **ethical implications**.  The ability of generative AI to create hyper-realistic deepfakes raises concerns about misinformation and its potential to erode trust in digital content.  Moreover, questions surrounding copyright and ownership of AI-generated content are still murky, demanding careful consideration and robust legal frameworks. The potential displacement of human jobs by AI also requires a proactive approach, focusing on reskilling and adapting to the evolving job market. \n\n**The Evolving Canvas of Society:**\n\nThe **AI impact on society** extends far beyond the professional sphere.  Generative AI has the potential to personalize education, making learning more engaging and accessible. Imagine AI tutors crafting customized learning plans or generating interactive educational materials tailored to individual student needs. This technology also holds immense promise in healthcare, aiding in drug discovery, medical imaging analysis, and even providing companionship to the elderly.\n\n**The Future Unfolds:**\n\nAs we stand at the cusp of this new frontier, it's crucial to approach generative AI with a sense of cautious optimism. While embracing the immense potential of **machine learning applications** to enhance our lives, we must also be vigilant in addressing the ethical dilemmas it presents. By fostering open dialogues, implementing responsible regulations, and prioritizing ethical considerations, we can harness the power of generative AI to shape a future where human creativity and artificial intelligence coexist and flourish.\n\nThe story of generative AI is still being written.  It's a story brimming with both promise and uncertainty, demanding our active participation in shaping its narrative.  The choices we make today will determine whether this powerful technology becomes a force for good, propelling us towards a brighter future. \n",
        ],
        },
    ]
    )

#Title of app
st.title("✍️🤖 BlogCraft: Your Digital Writing Assistant")

#Subheading
st.subheader("Transforming Words into Wonders with Advanced AI")

if submit_button:
    response = chat_session.send_message(promt_parts)
    images=[]
    images_gallery=[]

    for i in range(num_images):
        image_response = client.images.generate(
            model="dall-e-3",
            prompt=f"Generate a Blog Post Image on the title:{blog_title}",
            size="1024x1024",
            quality="standard",
            n=1,
        )
        new_image = single_image.copy()
        new_image["title"]=f"Image {i+1}"
        new_image["text"]=f"{blog_title}"
        new_image["img"]=image_response.data[0].url
        images_gallery.append(new_image)
    
    st.title("Your blog images are here:")
    carousel(items=images_gallery, width=1)

    st.title("Your blog post is here:")
    st.write(response.text)
    
