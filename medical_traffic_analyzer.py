
# BioCyberWall - HL7 Message Analyzer
# Educational healthcare IT security prototype
# Uses fictional patient data only.

def analyze_hl7_message(message):
    print("\n--- HL7 Message Analysis ---")

    # HL7 v2 segments are usually separated by carriage returns.
    # This demo also accepts newline characters.
    lines = message.replace("\r", "\n").split("\n")

    segments = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        segment_name = line.split("|", 1)[0]
        segments.append(segment_name)

    print("Detected segments:", ", ".join(segments))

    # Check message header
    if segments and segments[0] == "MSH":
        print("[OK] MSH header detected.")
        print("[INFO] HL7-like message structure found.")
    else:
        print("[WARNING] Missing or misplaced MSH header.")

    # Check for patient identification segment
    if "PID" in segments:
        print("[INFO] PID segment detected.")
        print("[INFO] Patient identification data may be present.")
    else:
        print("[INFO] No PID segment detected.")

    # Transport encryption cannot be determined
    # from the HL7 message content alone.
    print("[INFO] TLS encryption status: NOT CHECKED.")
    print("[INFO] TLS requires network or configuration inspection.")

    print("[INFO] This is not a complete HL7 validator.")


def main():
    print("BioCyberWall - HL7 Message Analyzer")
    print("=" * 45)

    # Fictional HL7 v2 test message
    sample_hl7 = (
        "MSH|^~\\&|MONITOR|DEPT_A|HIS|HOSPITAL|"
        "20261014||ADT^A01|101|P|2.3\r"
        "PID|||TEST001||DOE^JANE"
    )

    print("\nTEST 1: HL7 sample message")
    analyze_hl7_message(sample_hl7)

    print("\nTEST 2: Message without MSH")
    invalid_sample = "PID|||TEST002||DOE^JOHN"
    analyze_hl7_message(invalid_sample)

    print("\nAll demo checks completed.")


if __name__ == "__main__":
    main()
