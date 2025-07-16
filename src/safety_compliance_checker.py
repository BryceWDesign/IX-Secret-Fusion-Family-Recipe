"""
safety_compliance_checker.py

Utility module for validating civilian-use compliance across IX-Secret-Fusion-Family-Recipe components.

This module provides static checks to ensure no restricted terms, isotopic materials, or prohibited operations are present in user-submitted extensions.

Author: Bryce W. Design
Date: July 2025
"""

PROHIBITED_TERMS = [
    "deuterium",
    "tritium",
    "uranium",
    "plutonium",
    "ignition",
    "reactor",
    "breeder",
    "classified",
    "military",
    "defense",
    "TAR",
    "EAR",
    "export control"
]

def check_file_for_prohibited_terms(file_path):
    """
    Scan a file for prohibited terms defined in PROHIBITED_TERMS list.

    :param file_path: Path to the file to check.
    :return: List of prohibited terms found.
    """
    detected_terms = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            for term in PROHIBITED_TERMS:
                if term.lower() in content:
                    detected_terms.append(term)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return detected_terms

if __name__ == "__main__":
    # Example static check:
    sample_file = "docs/10_Safety_and_Compliance.md"
    flagged_terms = check_file_for_prohibited_terms(sample_file)

    if flagged_terms:
        print(f"⚠️ Prohibited terms detected in {sample_file}: {flagged_terms}")
    else:
        print(f"✅ {sample_file} passed compliance check.")
