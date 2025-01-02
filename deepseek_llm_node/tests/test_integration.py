import pytest
from src.deepseek_llm_node.comfyui_nodes.deepseek_llm_node import DeepSeekLLMNode

def test_deepseek_node():
    node = DeepSeekLLMNode()
    assert node.CATEGORY == "Custom/LLM"
    assert "prompt" in node.INPUT_TYPES()["required"]