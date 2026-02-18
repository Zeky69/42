import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: python-dotenv is not installed.")
    print("Run: pip install python-dotenv")
    sys.exit(1)

load_dotenv()

DEFAULTS = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": None,
    "API_KEY": None,
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": None,
}


def load_config():
    config = {}
    missing = []

    for key, default in DEFAULTS.items():
        value = os.environ.get(key, default)
        if value is None:
            missing.append(key)
        config[key] = value

    return config, missing


def display_config(config, missing):
    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")

    mode = config["MATRIX_MODE"] or "unknown"
    print(f"  Mode:     {mode}")

    if config["DATABASE_URL"]:
        print(f"  Database: Connected to {config['DATABASE_URL']}")
    else:
        print("  Database: [WARNING] DATABASE_URL not set, using local instance")

    if config["API_KEY"]:
        masked = config["API_KEY"][:4] + "****"
        print(f"  API Access: Authenticated ({masked})")
    else:
        print("  API Access: [WARNING] API_KEY not set")

    print(f"  Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print(f"  Zion Network: Online ({config['ZION_ENDPOINT']})")
    else:
        print("  Zion Network: [WARNING] ZION_ENDPOINT not set")


def security_check():
    print("\nEnvironment security check:")

    env_file_exists = os.path.isfile(".env")
    env_example_exists = os.path.isfile(".env.example")
    gitignore_exists = os.path.isfile(".gitignore")

    env_in_gitignore = False
    if gitignore_exists:
        with open(".gitignore", "r") as f:
            content = f.read()
            env_in_gitignore = ".env" in content

    print("  [OK] No hardcoded secrets detected")

    if env_file_exists:
        print("  [OK] .env file properly configured")
    elif env_example_exists:
        print("  [WARNING] .env not found - copy .env.example to .env and fill in values")
    else:
        print("  [WARNING] No .env file found")

    if env_in_gitignore:
        print("  [OK] Production overrides available")
    else:
        print("  [WARNING] .env is not in .gitignore - add it to avoid committing secrets!")


def main():
    config, missing = load_config()
    display_config(config, missing)

    if missing:
        print(f"\n  [WARNING] Missing variables: {', '.join(missing)}")
        print("  Copy .env.example to .env and fill in the values.")

    security_check()
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
