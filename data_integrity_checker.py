
import hashlib


def calculate_sha256(data):
    """
    Calculate the SHA-256 hash of a text string.
    """
    return hashlib.sha256(
        data.encode("utf-8")
    ).hexdigest()


def verify_file_integrity(expected_hash, data):
    """
    Compare the expected SHA-256 hash with
    the hash calculated from the current data.
    """
    current_hash = calculate_sha256(data)

    print("\n--- Integrity Check ---")
    print("Expected SHA-256:", expected_hash)
    print("Current SHA-256: ", current_hash)

    if current_hash == expected_hash:
        print("[OK] Integrity verified. Data is unchanged.")
        return True
    else:
        print("[WARNING] Integrity check failed. Data has changed!")
        return False


def main():
    print("BioCyberWall - Healthcare Data Integrity Checker")
    print("=" * 50)

    # Original sample data
    original_data = "Patient_Report_v1"

    # Generate the original SHA-256 hash
    original_hash = calculate_sha256(original_data)

    print("\nOriginal data:", original_data)
    print("Original hash:", original_hash)

    # TEST 1: Unmodified data
    print("\nTEST 1: Checking original data")
    verify_file_integrity(original_hash, original_data)

    # TEST 2: Modified data
    modified_data = "Patient_Report_v2"

    print("\nTEST 2: Checking modified data")
    verify_file_integrity(original_hash, modified_data)

    print("\nAll tests completed.")


if __name__ == "__main__":
    main()
