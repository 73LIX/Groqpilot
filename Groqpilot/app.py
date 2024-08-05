import os
import sys
import spacy
import gradio as gr
from groq import Groq
import json
import re

nlp = spacy.load("en_core_web_sm")

# Get the prompted API key and model from user
if len(sys.argv) != 3:
    print("Usage: python app.py <API_KEY> <MODEL_NAME>")
    sys.exit(1)

api_key = sys.argv[1]
model_name = sys.argv[2]

# Set up the API key
os.environ["GROQ_API_KEY"] = api_key

client = Groq(api_key=api_key)

chat_directory = "./chats"  # Directory to store chat history files
log_file = "./error_log.txt"  # Log file for errors
os.makedirs(chat_directory, exist_ok=True)  # Ensure chat directory exists


# Log an error message to the log file.
def log_error(message):
    with open(log_file, "a") as f:
        f.write(message + "\n")


# Save the chat history to a file.
def save_chat_history(chat_history, file_name):
    try:
        with open(file_name, "w") as file:
            json.dump(chat_history, file)
        print(f"Chat history saved to {file_name}")
    except Exception as e:
        log_error(f"Error saving chat history: {e}")


# Load the chat history from a file.
def load_chat_history(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                return json.load(file)
        else:
            log_error(f"File {file_name} does not exist")
            return []
    except Exception as e:
        log_error(f"Error loading chat history: {e}")
        return []


def extract_keywords(system_role: str, user_input: str) -> str:
    combined_text = f"{system_role} {user_input}" if system_role else user_input
    doc = nlp(combined_text)

    # Extract named entities
    entities = [ent.text for ent in doc.ents]

    # Extract nouns and verbs
    nouns_and_verbs = [token.text for token in doc if token.pos_ in ["NOUN", "VERB"]]

    # Combine entities and nouns/verbs to create a file name
    keywords = entities + nouns_and_verbs
    keywords = [keyword.lower() for keyword in keywords]
    keywords = [re.sub(r"\W+", "_", keyword) for keyword in keywords]

    # Remove duplicates and join keywords with underscores
    keywords = list(set(keywords))
    filename = "_".join(keywords)

    return filename


# Get a list of available chat files.
def get_available_chats():
    try:
        files = os.listdir(chat_directory)
        return [f for f in files if f.endswith(".json")]
    except Exception as e:
        log_error(f"Error getting available chats: {e}")
        return []


# Chat with the Llama model.
def chat_with_llm(system_role, user_input, new_chat, selected_chat):
    try:
        if new_chat:
            chat_history = []
            chat_history.append({"role": "system", "content": system_role})
            keywords = extract_keywords(system_role, user_input)
            unique_file_name = os.path.join(chat_directory, f"{keywords}.json")
            save_chat_history(chat_history, unique_file_name)
        elif selected_chat:
            unique_file_name = (
                os.path.join(chat_directory, selected_chat)
                if isinstance(selected_chat, str)
                else os.path.join(chat_directory, selected_chat[0])
            )
            chat_history = load_chat_history(unique_file_name)
        else:
            unique_file_name = os.path.join(chat_directory, "chat_history.json")
            chat_history = load_chat_history(unique_file_name)

        messages = chat_history + [
            {
                "role": "user",
                "content": user_input,
            }
        ]

        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model_name,
        )
        reply = chat_completion.choices[0].message.content

        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": reply})

        save_chat_history(chat_history, unique_file_name)
        return reply
    except Exception as e:
        log_error(f"Error in chat_with_llm function: {e}")
        return f"Error: {e}"


# Update the dropdown list of available chats.
def update_dropdown():
    try:
        choices = get_available_chats()
        return gr.update(choices=choices)
    except Exception as e:
        log_error(f"Error updating dropdown: {e}")
        return gr.update(choices=[])


# Gradio interface
with gr.Blocks() as GradioUI:
    gr.Markdown(
        """
    <div style="text-align: center;">
        <h1>Groqpilot</h1>
        <h4><a href='https://github.com/73LIX/Groqpilot' target='_blank'>Github</a> repository</h4>
    </div>
        <p>AI can make mistakes. Check for important info..</p>
    """
    )

    system_role = gr.Textbox(label="System Role")
    user_input = gr.Textbox(label="User Input")
    new_chat = gr.Checkbox(label="Start New Chat", value=False)
    selected_chat = gr.Dropdown(
        choices=get_available_chats(), label="Select Chat", interactive=True
    )
    chat_output = gr.Textbox(label="Response")

    submit_button = gr.Button("Submit")
    update_button = gr.Button("Update Chat List")

    submit_button.click(
        chat_with_llm,
        inputs=[system_role, user_input, new_chat, selected_chat],
        outputs=chat_output,
    )
    update_button.click(fn=update_dropdown, outputs=selected_chat)

GradioUI.launch()
