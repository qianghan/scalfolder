# Import the core inference function from our utilities
from ..core_logic.deepseek_utils import run_deepseek_inference

class DeepSeekLLMNode:
    """
    A ComfyUI custom node that provides an interface to the DeepSeek-LLM model.
    This node allows users to generate text using DeepSeek-LLM directly within ComfyUI.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Defines the input parameters that this node accepts.
        Returns a dictionary specifying required and optional inputs.
        """
        return {
            "required": {
                "prompt": ("STRING",),  # The input prompt for text generation
            }
        }

    # Define the type of data this node outputs
    RETURN_TYPES = ("STRING",)
    # Specify which method will be called when the node executes
    FUNCTION = "execute"
    # Define where this node appears in the ComfyUI menu
    CATEGORY = "Custom/LLM"
    # Provide a description of what this node does
    DESCRIPTION = "A ComfyUI node that calls DeepSeek-LLM for text generation."

    def execute(self, prompt: str):
        """
        Main execution function called by ComfyUI when the node is run.
        Takes a text prompt as input and returns the generated response.
        
        Args:
            prompt (str): The input text prompt for generation
            
        Returns:
            tuple[str]: A single-element tuple containing the generated text
        """
        # Call our core inference logic and wrap the result in a tuple
        result = run_deepseek_inference(prompt)
        return (result,)

# Register the node class with ComfyUI so it can be discovered
NODE_CLASS_MAPPINGS = {
    "DeepSeekLLMNode": DeepSeekLLMNode
}

# Define a user-friendly display name for the node in the UI
NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekLLMNode": "DeepSeek LLM"
}