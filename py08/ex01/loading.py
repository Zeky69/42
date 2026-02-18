import sys
import importlib


REQUIRED_PACKAGES = {
    "pandas": "pandas",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
}

OPTIONAL_PACKAGES = {
    "requests": "requests",
}


def check_dependencies():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    missing = []
    available = {}

    all_packages = {**REQUIRED_PACKAGES, **OPTIONAL_PACKAGES}

    for import_name, display_name in all_packages.items():
        try:
            module = importlib.import_module(import_name)
            version = getattr(module, "__version__", "unknown")
            label = {
                "pandas": "Data manipulation ready",
                "numpy": "Numerical computation ready",
                "matplotlib": "Visualization ready",
                "requests": "Network access ready",
            }.get(import_name, "Ready")
            print(f"  [OK] {display_name} ({version}) - {label}")
            available[import_name] = module
        except ImportError:
            if import_name in REQUIRED_PACKAGES:
                print(f"  [MISSING] {display_name} - not installed")
                missing.append(display_name)
            else:
                print(f"  [OPTIONAL] {display_name} - not installed (optional)")

    return available, missing


def show_versions(available):
    print("\nPackage manager comparison:")
    print("  pip:    managed via requirements.txt")
    print("  Poetry: managed via pyproject.toml")
    print("\nInstalled versions:")
    for name, module in available.items():
        version = getattr(module, "__version__", "unknown")
        print(f"  {name}: {version}")


def analyze_matrix_data(available):
    import matplotlib.pyplot as plt

    print("\nGenerating visualization...")
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 15, 30, 20]
    plt.bar(x, y)
    plt.title("Matrix Data")
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main():
    available, missing = check_dependencies()

    if missing:
        print(f"\nERROR: Missing required packages: {', '.join(missing)}")
        print("\nTo install with pip:")
        print("  pip install -r requirements.txt")
        print("\nTo install with Poetry:")
        print("  poetry install")
        sys.exit(1)

    show_versions(available)
    analyze_matrix_data(available)


if __name__ == "__main__":
    main()
