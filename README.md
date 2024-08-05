# Groqpilot

Groqpilot is an application which uses Groq-API to help you run Large language models, on your local computer without a gpu or a high end system requirement. This application will save you tons of storage space and since all the inference is handled through Groq-API, so its really really fast in terms of content/text generation.

This repository primarily provides a Gradio GUI and additional features to run Groq Models.

## Contents
• [Groqpilot](https://github.com/73LIX/Groqpilot?tab=readme-ov-file#groqpilot)
* [Why Use Groqpilot?](https://github.com/73LIX/Groqpilot?tab=readme-ov-file#why-use-groqpilot)
* [Google Colab](https://github.com/73LIX/Groqpilot?tab=readme-ov-file#colab)
* [Installation](https://github.com/73LIX/Groqpilot?tab=readme-ov-file#installation)
     * [Windows](https://github.com/73LIX/Groqpilot?tab=readme-ov-file#installation)

## Why Use Groqpilot?
Groqpilot is a very useful tool to run the Groq-API for seamless inference and management, It offers:
*  User-Friendly Interface: Groqpilot offers a clean, intuitive, and user-friendly interface powered by Gradio. This ensures that users can interact with the chatbot effortlessly, without any steep learning curve.
*  Chat History Management: Groqpilot allows users to start new chats or continue existing conversations easily. With features like saving and loading chat history, users can pick up right where they left off
*  Unqiue file naming using NPL: The application includes a sophisticated keyword extraction feature that helps categorize and name chat sessions based on their content. This makes it easier to organize and 
   retrieve past conversations.
*  Multi-Model Support: Users can use multiple models in a single application allowing them to explore and try out different models.
*  Adaptable for Various Use Cases: Whether for customer support, educational purposes, or personal use, Groqpilot can be adapted to various scenarios, making it a versatile tool for different applications.
*  Open Source and Extensible: Groqpilot is designed to be open-source, allowing users and developers to modify and extend its functionality. This ensures that the application can evolve with the community's 
   needs and stay up-to-date with the latest advancements.   

With detailed documentation and a helpful readme.txt file, users can easily understand how to set up and use Groqpilot, making it accessible to a wide audience.

## 🤝Colab

Here's a colab notebook to try out the app. You can run the notebook on the free tier with a CPU runtime.

| |Google Colab|
|:--|:-:|
| **Groqpilot** |  [![Open in Colab](https://github.com/73LIX/Meta-Llama-3.1-8BxColab/blob/main/asset/colab_logo.svg)](https://colab.research.google.com/drive/1_B3vedI7H994TIm8w0f82Meguj-TtJt0?usp=sharing)

## Installation

### Windows
**Prerequisites**
1. Install [Python 3.10.11](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe) <br>
2. Install [Git](https://git-scm.com/download/win). <br>
3. Install the [Microsoft Visual Studio](https://aka.ms/vs/17/release/vc_redist.x64.exe).
4. GroqAPI Key [here](https://console.groq.com/keys).

**Setup**
1. Clone the repository by running this command:

   ```bash
   git clone https://github.com/73LIX/Groqpilot.git

2. Run the batch file: The batch file will execute and complete the installation automatically.

   ```bash
   run_groqpilot.bat

3. Enter your API Key:
   When you run the batch file for the first time you will be prompted for the GroqAPI Key.

4. Choose your model:
   During the setup, you will be prompted to choose a model from a predefined list or enter your own model ID from Groq. If no choice is made,
   the default model llama-3.1-70b-versatile will be used.

      After the setup is complete, the App will be launched automatically and the Gradio URL will be opened in your default web browser.

## Upgrading->Updating

### Windows
If a new release comes out you can upgrade by using the command:
*   Pull the latest changes from the repository
    ```bash
    git pull
