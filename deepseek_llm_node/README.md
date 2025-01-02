# deepseek_llm_node

An advanced scaffold for a ComfyUI custom-node project.  
This structure includes:
- Docker support
- GitHub Actions for CI
- pre-commit for linting & type checking
- Example Node with separate core logic
- Unit & Integration tests

## Quickstart

1. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install**:
   ```bash
   pip install -e .[dev]
   pre-commit install
   ```

3. **Run Tests**:
   ```bash
   pytest
   ```

4. **Lint & Format**:
   ```bash
   black .
   flake8 .
   mypy .
   ```

5. **Try Docker**:
   ```bash
   docker build -t deepseek_llm_node:latest .
   docker run -p 8188:8188 deepseek_llm_node:latest
   ```

## Using the Node with ComfyUI

- You can copy or symlink `src/deepseek_llm_node/comfyui_nodes` into your ComfyUI `custom_nodes` folder.
- Or, run ComfyUI in an environment where this project is installed (so ComfyUI can discover the custom node).

## Project Layout

```
deepseek_llm_node/
├─ Dockerfile
├─ pyproject.toml
├─ .pre-commit-config.yaml
├─ .github/workflows/ci.yml
├─ src/
│   └─ deepseek_llm_node/
│       ├─ core_logic/
│       │   └─ video_utils.py
│       └─ comfyui_nodes/
│           └─ example_node.py
├─ tests/
│   ├─ test_core_logic.py
│   └─ test_integration.py
├─ .gitignore
├─ LICENSE
└─ README.md
```

Modify and expand as needed!
