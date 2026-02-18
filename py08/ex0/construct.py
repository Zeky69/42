import sys
import os
import site


def main():
    venv_path = os.environ.get("VIRTUAL_ENV")

    if venv_path:
        venv_name = os.path.basename(venv_path)
        packages = site.getsitepackages()
        package_path = packages[0] if packages else "N/A"

        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(package_path)
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("    python -m venv matrix_env")
        print("    source matrix_env/bin/activate  # On Unix")
        print(r"    matrix_env\Scripts\activate     # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
