# Groqpilot

Groqpilot is an application which uses Groq-API to help you run Large language models, on your local computer without a gpu or a high end system requirement. This application will save you tons of storage space and since all the inference is handled through Groq-API, so its really really fast in terms of content/text generation.

This repository primarily provides a Gradio GUI and additional features to run Groq Models.

## Contents



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

      After the setup is complete, the App will be launched automatically and the URL will be opened in your default web browser.

## Upgrading->Updating

### Windows
If a new release comes out you can upgrade by using the command:

   ```bash
    git pull

