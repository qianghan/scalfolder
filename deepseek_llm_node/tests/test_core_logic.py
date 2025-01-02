import pytest  # noqa: F401
from src.deepseek_llm_node.core_logic.deepseek_utils import run_deepseek_inference

def test_run_deepseek_inference(mocker):
    # Mock the transformers calls to avoid loading model
    mock_model = mocker.patch('deepseek_llm_node.core_logic.deepseek_utils.AutoModelForCausalLM')
    mock_tokenizer = mocker.patch('deepseek_llm_node.core_logic.deepseek_utils.AutoTokenizer')
    
    # Configure mocks
    mock_tokenizer.from_pretrained().return_value.decode.return_value = "Mocked response"
    
    result = run_deepseek_inference("Test prompt")
    assert result == "Mocked response"
