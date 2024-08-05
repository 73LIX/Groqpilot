/Groqpilot_Directory
    ├── run_groqpilot.bat
    ├── requirements.txt
    ├── app.py

Contents
1.Introduction
2.Prerequisites
3.Installation Steps
4.Running the Application
5.UI(Learn more about UI from here)
6.Troubleshooting(Contact Support Included)


--->Introduction<---

The Groqpilot is designed to run Large Language Models (LLMs) through the Groq API with a custom UI using Gradio. Since it uses Groq-API the inference speend and the text generation speed
is really fast & aslo You don't need to download and store those large LLM models on your local machine, which can be impractical for many users due to storage and performance constraints.

Benefit of Using Groqpilot:

You don't need a (high-end) system configuration for using the Large Language Models, not even a GPU that you generally need run llm's, 
but here you get to run an llm with minimum resources used.


--->Prerequisites<---
**Before running the application, ensure you have the following:**

•Python installed on your system [If not then don't worry upon running the batch file it will set you up completely].
•An internet connection to install dependencies.
•Your Groq API key: This is important since you need your API key to run models. You can get the API key from here: https://console.groq.com/keys, Just remember to sign-up & create the key.

Files Included:

•run_groqpilot.bat: Batch file to set up the Python environment, install dependencies, and launch the Gradio app.
•requirements.txt: List of Python dependencies required by the application.
•app.py: Main application script to run the Gradio app.
•readme.txt: This guide.


--->Installation Steps<---
Check✅: Make sure you have the following files in the same directory:

•run_groqpilot.bat (the batch file to set up and run the application)
•requirements.txt (lists the necessary Python dependencies)
•app.py (the main application code)

Step 1:Run the Batch File:
•Execute run_groqpilot.bat to begin the setup process. This will:
   •Check for Python installation and install it if necessary.
   •Create a virtual environment.
   •Install required dependencies from requirements.txt.
   •Prompt for the Groq API key and save it in "secrets/api_key.txt" so that you don't need to enter it again & again.
   •Allow you to choose your preffered model to run or type in your own Model ID from Groq.

Step 2:Enter your API Key
When you run the batch file, during the setup you will be prompted to enter your Groq-API Key, just paste the API key that you created in your groq account. Don't worry it will just prompt
you for the first installation, after that it will be saved in your "api_key.txt" file for easy access.

Step 3:Choose your model
During the setup, you will be prompted to choose a model from a predefined list or enter your own model ID from Groq. If no choice is made,
the default model llama-3.1-70b-versatile will be used.


--->Running the Application<---
After the setup is complete, the App will be launched automatically and the URL will be opened in your default web browser.


--->UI(Learn more about UI from here)<---

Inputs->
•System_role: The system role sets the behaviour of the model for example

             "if you put "Talk as hulk" in the system_role then the llm
             will respond as hulk as if he is playing that character."
           
You can leave it empty for default behaviour.
•User_input: The user input is where your prompts/messages go.

Output->
•Response: The response is where you will get the generated content/text from the model.

Additional Features->
•Start New Chat(Option): When you toggle on this option, it creates a new chat different from your default or older one you have been using, its basically like entering a new empty chat.
•Select Chat(Dropdown): This is where all your recent chat's will be listed you can select one from the dropdown and continue it further.❗But remember to Untick❌ the Start New Chat
or else it will keep on creating new chat's, basically to continue the chat just select the chat from the List and Untick the Start new chat.

Buttons->
•Submit: The submit button is used to send your message/prompts to the model
•Update Chat List: This button refreshes/updates the chat history list .i.e When you create a new chat its doesn't automatically gets updated in the select_chat dropdown also known as
you chat history list, so to update/refresh the list you use the Update Chat List button.


**The UI comes with some handy features like**
     •Saving your chat history/content into a json file stored in ./chats.
     •Whenever you start a new chat, the application saves a json file and the filename is created with some texts picked up from your conversation using spacy(NLP).
     •You have the option to start a new chat or select from existing ones so that you can continue your topic/chat with the model without loosing any previous data or
      information you fed into it. Its basically like continuing your chat from wherever you left it off.


--->Troubleshooting<---

Common Issues:
•API Key not valid/not set: In this case delete your secretes folder and run the batch file again and then put your new API key.
•Dependencies Not Installed: Ensure that the requirements.txt file is in the same directory as the batch file, the dependencies are correctly listed and you have an internet connection.
•Python Installation Issues: If the batch script fails to install Python, please download and install it manually from the official Python website, You can download Python 3.10.12.

Error Logs:
If you encounter any errors, check the error_log.txt file in the application directory for detailed error messages.

Contact Support:
For any issues or questions, Dm me on Discord - here's my Discord ID: felix9009.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Thank you for using Groqpilot! If you have any questions or need further assistance, please refer to this readme file or contact support.

For better instructions and tips to use the application in the most efficient way refer to --------> Instructions.txt




