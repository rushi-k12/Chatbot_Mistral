# Example: Loading a pre-trained GPT-2 model and saving its weights
from transformers import GPT2LMHeadModel

# Load pre-trained GPT-2 model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Save the model weights
model.save_pretrained('model/pytorch_model.bin')
