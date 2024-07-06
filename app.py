import streamlit as st
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Streamlit App
def main():
    st.title('Text Generation')
    st.write('Enter a prompt below to generate text:')

    # Input prompt from user
    prompt = st.text_area('Input Prompt')

    # Generate button
    if st.button('Generate Text'):
        if prompt:
            # Tokenize input text
            input_ids = tokenizer.encode(prompt, return_tensors='pt')

            # Generate output
            output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

            # Decode and display generated text
            generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
            st.write("Generated Text:")
            st.write(generated_text)
        else:
            st.warning('Please enter a prompt.')

if __name__ == '__main__':
    main()
