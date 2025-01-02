# Import required libraries for the DeepSeek LLM model
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

# Specify the model name/path for the DeepSeek 7B chat model
model_name = "deepseek-ai/deepseek-llm-7b-chat"

# Initialize the tokenizer for text preprocessing
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create cache directory for model weights offloading to manage memory usage
cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "deepseek_llm")
os.makedirs(cache_dir, exist_ok=True)

# Load the DeepSeek LLM model with optimized settings:
# - Using float16 for reduced memory usage
# - Auto device mapping for optimal hardware utilization
# - Offloading to disk cache to handle large model size
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.float16,
    device_map="auto",
    offload_folder=cache_dir
)

def run_deepseek_inference(prompt: str) -> str:
    """Run inference using DeepSeek-LLM model.
    
    Args:
        prompt (str): The input text prompt to generate a response for
        
    Returns:
        str: The generated text response from the model
        
    The function handles:
    1. Tokenization of input prompt
    2. Moving tensors to appropriate device
    3. Text generation with specified parameters
    4. Decoding the output tokens to readable text
    """
    # Convert prompt to model input format and move to same device as model
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    # Generate text with the following parameters:
    # - max_length: Maximum number of tokens in the output
    # - temperature: Controls randomness (higher = more random)
    # - do_sample: Enable sampling for more diverse outputs
    outputs = model.generate(
        **inputs,
        max_length=2048,
        temperature=0.7,
        do_sample=True
    )
    
    # Decode the generated tokens back to text, removing special tokens
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response 