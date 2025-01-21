# Fold - ComfyUI Custom Node Scaffolder

A command-line tool that generates a complete project structure for ComfyUI custom nodes, including testing, CI/CD, and development tools.

## Features

- 🏗️ Complete project structure with src layout
- 🐳 Docker support
- 🔄 GitHub Actions CI
- ✨ Pre-commit hooks for linting & formatting
- 🧪 Test infrastructure (pytest)
- 📦 Virtual environment management
- 📝 Documentation templates

## Quick Start

```bash
# Basic usage
python fold.py my_custom_node

# Create with virtual environment
python fold.py my_custom_node --venv

# Create with requirements.txt
python fold.py my_custom_node --requirements

# Force overwrite existing directory
python fold.py my_custom_node --force
```

## Command Line Options

- `project_name`: Name of your custom node project
- `-v, --venv`: Create and initialize a virtual environment
- `-r, --requirements`: Generate a requirements.txt file
- `-f, --force`: Overwrite existing project directory

## Generated Structure

```
PROJECT_NAME/
├─ venv/              # Virtual environment (optional)
├─ Dockerfile         # Docker configuration
├─ pyproject.toml     # Project metadata and dependencies
├─ requirements.txt   # (optional) Direct dependencies
├─ .pre-commit-config.yaml
├─ .github/workflows/ci.yml
├─ src/
│   └─ package_name/
│       ├─ core_logic/        # Core business logic
│       │   └─ video_utils.py
│       └─ comfyui_nodes/    # ComfyUI node interfaces
│           └─ example_node.py
├─ tests/
│   ├─ test_core_logic.py    # Unit tests
│   └─ test_integration.py   # Integration tests
├─ .gitignore
├─ LICENSE
└─ README.md
```

## Development Workflow

1. Generate the scaffold:
   ```bash
   python fold.py my_node --venv --requirements
   ```

2. Activate the virtual environment:
   ```bash
   source my_node/venv/bin/activate  # Unix/MacOS
   .\my_node\venv\Scripts\activate   # Windows
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Initialize pre-commit:
   ```bash
   pre-commit install
   ```

5. Start developing your custom node in `src/package_name/comfyui_nodes/`

## Features Included

- 🔧 **Project Structure**: Organized src layout with separate core logic and node interfaces
- 📊 **Testing**: Pytest setup with example unit and integration tests
- 🔍 **Code Quality**: 
  - Black for formatting
  - Flake8 for linting
  - MyPy for type checking
- 🚀 **CI/CD**: GitHub Actions workflow for automated testing
- 🐳 **Docker**: Dockerfile for containerized development/deployment
- 📝 **Documentation**: README template with usage instructions

## Best Practices

- Keep core logic separate from ComfyUI node interfaces
- Write tests for both core logic and node integration
- Use type hints and docstrings
- Follow the pre-commit hooks guidelines
- Keep dependencies up to date

## License

MIT License - feel free to use and modify as needed! 