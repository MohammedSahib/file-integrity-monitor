
import hashlib
import json
import argparse
from pathlib import Path

BASELINE_FILE = Path(__file__).with_name("destination.json")

parser = argparse.ArgumentParser(description="File Integrity Monitor")
parser.add_argument("operation", choices=["init", "check", "update"])
parser.add_argument("filename", help="File to monitor")
args = parser.parse_args()


def load_json():
    if not BASELINE_FILE.exists():
        return {}

    with open(BASELINE_FILE, "r") as pointer:
        return json.load(pointer)

def save_json(file_data):
    with open(BASELINE_FILE, "w") as pointer:
        json.dump(file_data, pointer, indent=4)

def compute_hash(filename):
    with open(filename, "rb") as pointer:
        file_hash = hashlib.file_digest(pointer, "sha256")
        return file_hash.hexdigest()


def main():
    try:
        file_data = load_json()
        filename = str(Path(args.filename).resolve())

        if not Path(filename).is_file():
            print("Error: File does not exist or is not a regular file.")
            return

        if args.operation == "init":
            if filename in file_data:
                print("This file already has a snapshot.")
                return

            file_data[filename] = compute_hash(filename)
            save_json(file_data)
            print("Snapshot created successfully.")

        elif args.operation == "check":
            if filename not in file_data:
                print("No snapshot exists for this file.")
                return

            original_hash = file_data[filename]
            current_hash = compute_hash(filename)

            if original_hash == current_hash:
                print("File integrity verified.")
            else:
                print("File has been modified!")

        elif args.operation == "update":
            if filename not in file_data:
                print("No snapshot exists. Use init first.")
                return

            file_data[filename] = compute_hash(filename)
            save_json(file_data)
            print("Snapshot updated successfully.")

    except json.JSONDecodeError:
        print("Error: Baseline JSON file is invalid.")
    except OSError as error:
        print(f"File operation failed: {error}")


if __name__ == "__main__":
    main()
