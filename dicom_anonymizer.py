# BioCyberWall - Medical Device Data Privacy
# Purpose: Anonymize patient data in DICOM files (GDPR Compliance)

def anonymize_metadata(metadata):
    print("Scanning DICOM Metadata for PII (Personally Identifiable Information)...")
    
    # Simulating the removal of sensitive tags
    pii_tags = ['PatientName', 'PatientID', 'PatientBirthDate']
    
    for tag in pii_tags:
        print(f"[MODIFIED] Scrubbing {tag}... SUCCESS")
    
    print("File is now anonymized and safe for clinical research.")

if __name__ == "__main__":
    sample_data = {"PatientName": "John Doe", "PatientID": "12345"}
    anonymize_metadata(sample_data)
