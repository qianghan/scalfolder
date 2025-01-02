from ..core_logic.deepseek_utils import run_deepseek_inference

class DeepSeekLLMNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING",),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Custom/LLM"
    DESCRIPTION = "A ComfyUI node that calls DeepSeek-LLM for text generation."

    def execute(self, prompt: str):
        # Use the core logic from deepseek_infer
        result = run_deepseek_inference(prompt)
        return (result,)

# Node class mapping for ComfyUI to discover and register the node
NODE_CLASS_MAPPINGS = {
    "DeepSeekLLMNode": DeepSeekLLMNode
}

# Optional display name mapping
NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekLLMNode": "DeepSeek LLM"
}