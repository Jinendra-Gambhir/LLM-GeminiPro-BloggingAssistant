
# LLM-GeminiPro-BloggingAssistant

This project aims to build a Blogging Assistant to help users effortlessly generate blog content and accompanying visuals. I have leveraged Google Gemini's API for natural language processing (NLP) tasks and integrated it with DALL·E-3, a model capable of generating images from textual descriptions.


## Acknowledgements

 - [Google AI Studio](https://aistudio.google.com/)
 - [OpenAI](https://openai.com/)

## Tech Stack

* **Google Gemini API:** For natural language understanding and generation.
* **DALL·E-3:** To generate images based on text prompts.
* **Python:** Programming language used for integrating and orchestrating the project.
* **Streamlit:** A web application framework for Python, ideal for creating interactive user interfaces.

## Installation

Important libraries for this project.

```bash
import streamlit as st
import google.generativeai as genai
from openai import OpenAI
from streamlit_carousel import carousel
```
    
## Project Steps

**1. Setting Up Google Gemini API**
- First, we'll obtain access to Google Gemini API and set up authentication. This will allow us to utilize its powerful NLP capabilities for generating blog content based on user prompts.

**2. Integrating DALL·E-3 for Image Generation**
- Next, we'll integrate DALL·E-3 to generate images that complement the generated blog content. DALL·E-3 excels at creating images from detailed textual descriptions, adding visual appeal to our blog posts.

**3. Building the Streamlit Interface**
- Using Streamlit, we'll create a user-friendly interface where users can input their blog content ideas. The interface will showcase the capabilities of our AI Blogging Assistant, providing a seamless experience from text input to content generation and image creation.

**4. Deploying the Application**
- Once the application is developed, we can explore options for deployment. Streamlit allows for easy deployment to various platforms, making it accessible to a wide audience.
## Google Gemini API Reference

**Overview**
- The Google Gemini API is utilized in this project for advanced natural language processing (NLP), facilitating the generation of blog content based on textual prompts. It incorporates Google Gemini 1.5 Pro settings with specific configurations for temperature and safety.

#### Endpoint

```http
  https://api.gemini.google.com/v1
  OAuth 2.0 token
```
#### Model Setup
```bash
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)
```

#### Request
```bash
generation_config = {
  "temperature": 1,
  "top_p": 0.94,
  "top_k": 60,
  "max_output_tokens": 8172,
  "response_mime_type": "text/plain",
}
```

#### Response
```bash
{
  "generated_content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce gravida..."
}
```

#### Error Handling
 HTTP Status Codes:
* 200 OK: Successful request.
* 400 Bad Request: Invalid parameters or request format.
* 401 Unauthorized: Authentication failure.
* 500 Internal Server Error: Server-side issues.


## OpenAI DALL·E 3 API Reference

**Overview**
- OpenAI's DALL·E 3 API is utilized in this project to generate images from textual descriptions. It employs advanced deep learning models to create high-quality visuals based on detailed input prompts.

#### Endpoint

```http
  https://api.openai.com/v1/dalle-3/images
  API key
```
#### Model Setup
```bash
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
```

#### Request
```bash
{
  "prompt": "A surreal landscape with floating islands and glowing plants",
  "num_images": 1,
  "size": "512x512"
}
```

#### Response
```bash
{
  "images": [
    {
      "image_url": "https://api.openai.com/v1/dalle-3/images/1234567890"
    }
  ]
}

```

#### Error Handling
 HTTP Status Codes:
* 200 OK: Successful request.
* 400 Bad Request: Invalid parameters or request format.
* 401 Unauthorized: Authentication failure.
* 429 Too Many Requests: Rate limit exceeded.
* 500 Internal Server Error: Server-side issues.

## Features

**1. Natural Language Processing (NLP) with Google Gemini API**

* Utilizes Google Gemini API for advanced natural language understanding (NLU) and generation.
* Generates blog content based on user prompts, ensuring relevant and coherent text output.
**2. Image Generation with DALL·E-3**

* Integrates DALL·E-3, a state-of-the-art model capable of generating high-quality images from textual descriptions.
* Enhances blog posts with visually appealing images that match the content created by the assistant.
**3. Interactive User Interface with Streamlit**

* Implements a user-friendly interface using Streamlit, a powerful web application framework for Python.
* Allows users to input blog topics or ideas and receive dynamically generated content and images in real-time.
**4. Automation of Content Creation**

* Automates the process of content creation by combining AI-driven text generation and image synthesis.
* Reduces manual effort in brainstorming and creating blog posts, making it ideal for content creators and bloggers.
**5. Customization and Personalization**

* Enables customization of generated content based on user preferences and input.
* Supports personalization through adjustable parameters or input variations to tailor content outputs.
**6. Deployment and Accessibility**

* Facilitates easy deployment of the application to various platforms, ensuring accessibility for a wide audience.
* Offers flexibility in deployment options, including local hosting or cloud-based solutions for scalability.
**7. Learning and Exploration**

* Provides a learning platform for exploring advanced AI models and their practical applications.
* Encourages experimentation with AI technologies in content creation, fostering creativity and innovation.
**8. Documentation and Support**

* Includes comprehensive documentation and guides for setup, usage, and customization.
* Offers support and community engagement through the project's GitHub repository and related forums.
**9. Scalability and Future Extensions**

* Designed with scalability in mind to handle increased user interactions and content demands.
* Supports future extensions and improvements, such as integrating additional AI models or enhancing user interface features.
**10. Educational and Portfolio Value**

* Serves as an educational project for developers and AI enthusiasts to gain hands-on experience.
* Enhances portfolio value by showcasing skills in AI development, application integration, and user interface design.

## Screenshots

![App Screenshot](https://github.com/Jinendra-Gambhir/LLM-GeminiPro-BloggingAssistant/blob/main/Images/Screenshot%202024-06-14%20021357.png)


# Usage
#### Benefits and Learning Outcomes
* Hands-on Experience: Gain practical experience with state-of-the-art AI models and tools.
* Creativity and Innovation: Explore new ways to automate content creation using AI.
* Portfolio Enhancement: Showcase your skills in AI development and application.


## Deployment

- [Streamlit](https://github.com/Jinendra-Gambhir/LLM-GeminiPro-BloggingAssistant/)

## Demo

- [Video](https://youtu.be/FaSianNVEV8)


## Feedback

Feedback is welcome! Feel free to open an issue for suggestions or bug reports.


## Authors

- [Jinendra Gambhir](https://www.github.com/Jinendra-Gambhir)



## 🔗 Links
[![GitHub](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](github.com/Jinendra-Gambhir/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jinendragambhir/)

## License

[MIT](https://choosealicense.com/licenses/mit/)

