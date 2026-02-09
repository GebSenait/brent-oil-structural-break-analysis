"""
Verify that the current Python environment has all packages required to run
notebooks/task-2-change-point-analysis.ipynb. Run from repo root with the
project venv activated:  python scripts/verify_task2_env.py
"""
import sys

REQUIRED = [
    ("pandas", "pandas"),
    ("numpy", "numpy"),
    ("pymc", "pymc"),
    ("arviz", "arviz"),
    ("matplotlib", "matplotlib"),
    ("seaborn", "seaborn"),
    ("pytensor", "pytensor"),
]

def main():
    missing = []
    for mod_name, pkg_name in REQUIRED:
        try:
            __import__(mod_name)
        except ImportError as e:
            missing.append((pkg_name, str(e)))
    if missing:
        print("Missing or broken packages (install with: pip install -r requirements.txt):")
        for pkg, err in missing:
            print(f"  - {pkg}: {err}")
        sys.exit(1)
    print("All packages required for Task-2 notebook are present.")
    print("Python:", sys.executable)
    print("You can run notebooks/task-2-change-point-analysis.ipynb with this environment.")

if __name__ == "__main__":
    main()
