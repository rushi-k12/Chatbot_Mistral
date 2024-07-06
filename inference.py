import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from fastapi import FastAPI, Query

# Initialize FastAPI
app = FastAPI()

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Define endpoint for generating text
@app.get("/generate/")
def generate_text(prompt: str = Query(..., description="The input prompt for generating text")):
    # Tokenize input text
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate output
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    # Decode and return generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"generated_text": generated_text}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
