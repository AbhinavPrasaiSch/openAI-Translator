import tkinter as tk
import openai
import time

def translate():
    input_text = input_entry.get()
    input_lang = input_lang_entry.get()
    output_lang = output_lang_entry.get()
    translated_text = translate_text(input_text, input_lang, output_lang)
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", translated_text)
    output_text.config(state="disabled")

# Use the API key to authenticate with OpenAI
openai.api_key = "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"

# Function to translate text using GPT-3
def translate_text(input_text, input_lang, output_lang):
    model_engine = "text-davinci-002"
    prompt = (f"translate {input_text} from {input_lang} to {output_lang}"
             )

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

root = tk.Tk()
root.title("Text Translator")

input_text_label = tk.Label(root, text="Enter the text to translate:")
input_text_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

input_lang_label = tk.Label(root, text="Enter the input language:")
input_lang_label.pack()

input_lang_entry = tk.Entry(root)
input_lang_entry.pack()

output_lang_label = tk.Label(root, text="Enter the output language:")
output_lang_label.pack()

output_lang_entry = tk.Entry(root)
output_lang_entry.pack()

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

output_text = tk.Text(root, height=10, width=50, state="disabled")
output_text.pack()

root.mainloop()
