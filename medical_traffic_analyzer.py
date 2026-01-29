# BioCyberWall - Advanced MedTech Security
# Purpose: Analyze HL7 messages and verify TLS encryption status

def analyze_hl7_packet(packet_data, is_encrypted=False):
    print("--- Medical Device Traffic Analysis ---")
    
    # Check for Encryption (Security First)
    if not is_encrypted:
        print("[CRITICAL WARNING] Traffic is NOT ENCRYPTED (Missing TLS). Data exposure risk!")
    else:
        print("[OK] TLS Encryption detected. Secure connection.")

    # Simulating HL7 Message Parsing (MSH segment)
    if "MSH" in packet_data:
        print(f"[*] Valid HL7 Message Detected: {packet_data[:15]}...")
        # Check for Patient Data in the message
        if "PID" in packet_data:
            print("[!] Sensitive Patient ID (PID) found in packet.")
    else:
        print("[?] Unknown Protocol - Manual inspection required.")

if __name__ == "__main__":
    # Simulate an HL7 message from a Patient Monitor
    # MSH = Message Header, PID = Patient Identification
    sample_hl7 = "MSH|^~\\&|MONITOR|DEPT_A|HIS|HOSPITAL|20260129||ADT^A01|101|P|2.3| \nPID|||12345||DOE^JOHN"
    
    # Scenario: Unsecure transmission
    analyze_hl7_packet(sample_hl7, is_encrypted=False)
