import hashlib

# BioCyberWall - MedTech Security
# Purpose: Verify integrity of medical records using SHA-256 hashing

def verify_file_integrity(original_hash, current_data):
    current_hash = hashlib.sha256(current_data.encode()).hexdigest()
    
    if original_hash == current_hash:
        print("✅ Data Integrity Verified: No changes detected.")
    else:
        print("❌ WARNING: Data Mismatch! Possible unauthorized modification.")

if __name__ == "__main__":
    original = "73ec78..." # Example hash
    data = "Patient_Report_v1"
    verify_file_integrity(original, data)
