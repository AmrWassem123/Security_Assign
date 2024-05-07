import hashlib
import os

def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read in 64k chunks
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def verify_integrity(file_path, expected_hash):
    """Verify the integrity of a file."""
    calculated_hash = calculate_hash(file_path)
    if calculated_hash == expected_hash:
        print("File integrity is valid.")
    else:
        print("File integrity is compromised.")

if __name__ == "__main__":
    # Prompt user for file path
    file_path = input("Enter the file path: ")

    # Calculate and print hash
    calculated_hash = calculate_hash(file_path)
    print("SHA-256 Hash:", calculated_hash)

    # Option to verify integrity
    verify = input("Do you want to verify the integrity of the file? (y/n): ").lower()
    if verify == 'y':
        expected_hash = input("Enter the expected hash value: ")
        verify_integrity(file_path, expected_hash)

