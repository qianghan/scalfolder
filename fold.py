#!/usr/bin/env python3

import os
import sys
import textwrap
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Create an advanced ComfyUI custom-node project scaffold with Docker, GitHub Actions, pre-commit, tests, etc.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Generated project structure:
            PROJECT_NAME/
            ├─ venv/              # Virtual environment (optional)
            ├─ Dockerfile
            ├─ pyproject.toml
            ├─ requirements.txt (optional)
            ├─ .pre-commit-config.yaml
            ├─ .github/workflows/ci.yml
            ├─ src/
            │   └─ package_name/
            │       ├─ core_logic/
            │       │   └─ video_utils.py
            │       └─ comfyui_nodes/
            │           └─ example_node.py
            ├─ tests/
            │   ├─ test_core_logic.py
            │   └─ test_integration.py
            ├─ .gitignore
            ├─ LICENSE
            └─ README.md""")
    )
    
    parser.add_argument(
        "project_name",
        help="Name of the project to create. Will be used as the root directory name."
    )
    
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Overwrite existing project directory if it exists"
    )

    parser.add_argument(
        "-r", "--requirements",
        action="store_true",
        help="Generate a requirements.txt file in addition to pyproject.toml"
    )

    parser.add_argument(
        "-v", "--venv",
        action="store_true",
        help="Create and initialize a virtual environment"
    )

    args = parser.parse_args()

    # Check if directory exists and handle force flag
    if os.path.exists(args.project_name) and not args.force:
        print(f"Error: Directory '{args.project_name}' already exists. Use --force to overwrite.")
        sys.exit(1)
    
    create_scaffold(args.project_name, 
                   include_requirements=args.requirements,
                   create_venv=args.venv)

def create_scaffold(project_name: str, include_requirements: bool = False, create_venv: bool = False):
    """
    Create an advanced ComfyUI custom-node project scaffold
    with Docker, GitHub Actions, pre-commit, tests, etc.
    """
    # 1. Normalize the project name
    safe_name = project_name.lower().replace("-", "_").replace(" ", "_")

    # 2. Create directory structure
    os.makedirs(project_name, exist_ok=True)
    src_dir = os.path.join(project_name, "src", safe_name)
    node_dir = os.path.join(src_dir, "comfyui_nodes")
    logic_dir = os.path.join(src_dir, "core_logic")
    tests_dir = os.path.join(project_name, "tests")
    gh_actions_dir = os.path.join(project_name, ".github", "workflows")

    for d in [src_dir, node_dir, logic_dir, tests_dir, gh_actions_dir]:
        os.makedirs(d, exist_ok=True)

    # 3. Create files
    create_pyproject_toml(project_name, safe_name)
    if include_requirements:
        create_requirements_txt(project_name)
    create_dockerfile(project_name)
    create_gitignore(project_name)
    create_precommit_config(project_name)
    create_readme(project_name, safe_name)
    create_license(project_name)
    create_example_core_logic(logic_dir)
    create_example_node_wrapper(node_dir, safe_name)
    create_unit_test(tests_dir, safe_name)
    create_integration_test(tests_dir, safe_name)
    create_github_actions_ci(gh_actions_dir, safe_name)

    if create_venv:
        setup_virtual_environment(project_name)

    print(f"Project scaffold '{project_name}' created successfully.")
    if create_venv:
        print("\nTo activate the virtual environment:")
        print(f"  source {project_name}/venv/bin/activate  # For Unix/MacOS")
        print(f"  .\\{project_name}\\venv\\Scripts\\activate  # For Windows")

def setup_virtual_environment(project_name: str):
    """
    Creates and initializes a virtual environment for the project
    """
    import subprocess
    import platform

    venv_path = os.path.join(project_name, "venv")
    
    # Create virtual environment
    subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
    
    # Determine the pip path based on the platform
    if platform.system() == "Windows":
        pip_path = os.path.join(venv_path, "Scripts", "pip")
    else:
        pip_path = os.path.join(venv_path, "bin", "pip")
    
    # Upgrade pip
    subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
    
    # Install dependencies if requirements.txt exists
    requirements_path = os.path.join(project_name, "requirements.txt")
    if os.path.exists(requirements_path):
        subprocess.run([pip_path, "install", "-r", requirements_path], check=True)
    
    # Install the project in editable mode
    subprocess.run([pip_path, "install", "-e", project_name], check=True)

def create_requirements_txt(project_name: str):
    """
    Creates a requirements.txt file with common dependencies
    """
    content = textwrap.dedent("""\
    # Core dependencies
    torch>=2.0.0
    numpy>=1.22.0
    pillow>=9.0.0
    
    # Development dependencies
    pytest>=7.0.0
    pytest-mock>=3.10.0
    flake8>=6.0.0
    black>=23.7.0
    mypy>=1.5.0
    pre-commit>=3.3.0
    
    # Type stubs
    types-Pillow>=9.0.0
    """)
    
    file_path = os.path.join(project_name, "requirements.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_pyproject_toml(project_name: str, package_name: str):
    """
    Creates a pyproject.toml with:
    - basic project metadata
    - pinned dev dependencies for linting, testing, etc.
    """
    content = textwrap.dedent(f"""\
    [build-system]
    requires = ["setuptools>=42", "wheel"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "{package_name}"
    version = "0.1.0"
    description = "Advanced scaffold for a ComfyUI custom-node project."
    authors = [{{ name = "Your Name", email = "you@example.com" }}]
    readme = "README.md"
    license = {{ file = "LICENSE" }}
    requires-python = ">=3.8"
    keywords = ["comfyui", "nodes", "example"]

    [project.optional-dependencies]
    dev = [
      "pytest",
      "pytest-mock",
      "flake8",
      "black",
      "mypy",
      "pre-commit"
    ]

    [tool.black]
    line-length = 88
    target-version = ['py38', 'py39', 'py310', 'py311']

    [tool.flake8]
    max-line-length = 88
    extend-ignore = ["E203", "W503"]
    """)
    file_path = os.path.join(project_name, "pyproject.toml")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_dockerfile(project_name: str):
    """
    Creates a Dockerfile that installs Python, dependencies,
    and the local custom node code.
    """
    content = textwrap.dedent("""\
    FROM python:3.10-slim

    # Install system deps (if needed)
    # RUN apt-get update && apt-get install -y ...

    # Create a working directory
    WORKDIR /app

    # Copy project files
    COPY . /app

    # Install dependencies
    # This will install both the main project and the dev deps
    RUN pip install --upgrade pip && pip install -e .[dev]

    # Expose ComfyUI's default port (if you run it inside Docker)
    EXPOSE 8188

    # Optionally, you can run ComfyUI as an entrypoint
    # but that depends on how you structure your environment
    # ENTRYPOINT ["python", "run.py"]
    """)
    file_path = os.path.join(project_name, "Dockerfile")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_gitignore(project_name: str):
    content = textwrap.dedent("""\
    # Python
    __pycache__/
    *.py[cod]
    .pytest_cache/

    # Virtual env
    venv/
    .venv/
    env/
    .env/

    # Distribution / packaging
    build/
    dist/
    *.egg-info/

    # MyPy
    .mypy_cache/

    # Docker
    .dockerignore

    # IDE / Editor settings
    .vscode/
    .idea/
    """)
    file_path = os.path.join(project_name, ".gitignore")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_precommit_config(project_name: str):
    """
    Configures pre-commit hooks to run black, flake8, mypy
    before each commit.
    """
    content = textwrap.dedent("""\
    repos:
      - repo: https://github.com/psf/black
        rev: 23.7.0
        hooks:
          - id: black
            language_version: python3

      - repo: https://github.com/pycqa/flake8
        rev: 6.1.0
        hooks:
          - id: flake8

      - repo: https://github.com/pre-commit/mirrors-mypy
        rev: v1.5.1
        hooks:
          - id: mypy
    """)
    file_path = os.path.join(project_name, ".pre-commit-config.yaml")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_readme(project_name: str, package_name: str):
    content = textwrap.dedent(f"""\
    # {project_name}

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
       docker build -t {package_name}:latest .
       docker run -p 8188:8188 {package_name}:latest
       ```

    ## Using the Node with ComfyUI

    - You can copy or symlink `src/{package_name}/comfyui_nodes` into your ComfyUI `custom_nodes` folder.
    - Or, run ComfyUI in an environment where this project is installed (so ComfyUI can discover the custom node).

    ## Project Layout

    ```
    {project_name}/
    ├─ Dockerfile
    ├─ pyproject.toml
    ├─ .pre-commit-config.yaml
    ├─ .github/workflows/ci.yml
    ├─ src/
    │   └─ {package_name}/
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
    """)
    file_path = os.path.join(project_name, "README.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_license(project_name: str):
    """
    A simple MIT license placeholder.
    """
    content = textwrap.dedent("""\
    MIT License

    Copyright (c) 2023

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """)
    file_path = os.path.join(project_name, "LICENSE")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_example_core_logic(logic_dir: str):
    """
    Creates an example "video_utils.py" in core_logic to simulate
    the logic separate from ComfyUI node code.
    """
    content = textwrap.dedent("""\
    import os

    def process_video(input_path: str) -> str:
        \"\"\"Pretend to process a video, returning some result.\"\"\"
        # For demonstration, we just echo the path. You'd place
        # real video processing logic here.
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Video file not found: {input_path}")
        return f"Processed: {input_path}"
    """)
    file_path = os.path.join(logic_dir, "video_utils.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_example_node_wrapper(node_dir: str, package_name: str):
    """
    Creates a ComfyUI node that wraps the core_logic function.
    """
    content = textwrap.dedent(f"""\
    from {package_name}.core_logic.video_utils import process_video

    class ExampleVideoNode:
        @classmethod
        def INPUT_TYPES(cls):
            return {{
                "required": {{
                    "video_path": ("STRING",),
                }}
            }}

        RETURN_TYPES = ("STRING",)
        FUNCTION = "execute"
        CATEGORY = "Custom/Video"
        DESCRIPTION = "Example node that processes a video using core logic."

        def execute(self, video_path: str):
            # Use the core logic
            result = process_video(video_path)
            return (result,)
    """)
    file_path = os.path.join(node_dir, "example_node.py")
    init_file = os.path.join(node_dir, "__init__.py")

    # Ensure we have __init__.py
    with open(init_file, "w", encoding="utf-8") as f:
        f.write("# ComfyUI Node package\n")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_unit_test(tests_dir: str, package_name: str):
    """
    Creates a sample unit test for the core logic in 'video_utils'.
    """
    content = textwrap.dedent(f"""\
    import pytest
    import os
    from {package_name}.core_logic.video_utils import process_video

    def test_process_video(tmp_path):
        # Create a fake video file
        dummy_video = tmp_path / "test.mp4"
        dummy_video.write_text("fake video data")

        # Test the process_video function
        result = process_video(str(dummy_video))
        assert "Processed:" in result
        assert str(dummy_video) in result

        # Check error handling
        with pytest.raises(FileNotFoundError):
            process_video("non_existent.mp4")
    """)
    file_path = os.path.join(tests_dir, "test_core_logic.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_integration_test(tests_dir: str, package_name: str):
    """
    Creates a minimal integration test that tests the ExampleVideoNode
    in the context of ComfyUI-like usage. 
    We won't fully spin up ComfyUI, but we can mock or stub as needed.
    """
    content = textwrap.dedent(f"""\
    import pytest
    from {package_name}.comfyui_nodes.example_node import ExampleVideoNode

    def test_example_node_integration(tmp_path):
        # Create a fake video file
        dummy_video = tmp_path / "test.mp4"
        dummy_video.write_text("fake video data")

        node = ExampleVideoNode()
        result = node.execute(str(dummy_video))
        assert "Processed: " in result[0]
    """)
    file_path = os.path.join(tests_dir, "test_integration.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_github_actions_ci(gh_actions_dir: str, package_name: str):
    """
    Creates a basic GitHub Actions workflow (CI) that:
    - Checks out code
    - Sets up Python
    - Installs dependencies
    - Runs lint & tests
    """
    content = textwrap.dedent(f"""\
    name: CI

    on:
      push:
        branches: [ "main" ]
      pull_request:
        branches: [ "main" ]

    jobs:
      build-test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3

          - name: Set up Python
            uses: actions/setup-python@v4
            with:
              python-version: "3.10"

          - name: Install dependencies
            run: |
              pip install --upgrade pip
              pip install -e .[dev]

          - name: Lint (black, flake8, mypy)
            run: |
              black --check .
              flake8 .
              mypy .

          - name: Run tests
            run: |
              pytest --maxfail=1 --disable-warnings -q
    """)
    file_path = os.path.join(gh_actions_dir, "ci.yml")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()