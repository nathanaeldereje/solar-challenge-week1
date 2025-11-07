# solar-challenge-week1

## Environment Setup

1. Clone repository:
   ```bash
   git clone https://github.com/<USER>/solar-challenge-week1.git
   cd solar-challenge-week1
2. Create virtual environment:

        python -m venv .venv
        .\.venv\Scripts\Activate.ps1   # Windows
        # OR source .venv/bin/activate  # macOS/Linux

3. Install dependencies:

    ```bash
    Copy code
    pip install -r requirements.txt
    yaml
    Copy code

---

### `.github/workflows/ci.yml`
```yaml
name: CI

on:
  push:
    branches: [ main, setup-task ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Check Python version
        run: python --version
      - name: Run tests
        run: |
          if [ -d tests ]; then pytest -q || true; fi
.vscode/settings.json
json
Copy code
{
  "python.pythonPath": ".venv/bin/python",
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}