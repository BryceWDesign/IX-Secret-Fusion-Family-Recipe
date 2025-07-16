"""
material_spec_validator.py

Utility module to validate material specifications against
IX-Secret-Fusion-Family-Recipe civilian-use structural requirements.

Author: Bryce W. Design
Date: July 2025
"""

APPROVED_MATERIALS = {
    "Core Containment Shell": [
        "Tungsten Carbide Alloy",
        "Carbon Fiber Reinforced Ceramic Composites",
        "High-purity Silica Aerogel Panels"
    ],
    "Coil and Field Lattice": [
        "OFHC Copper with Graphene Reinforcement",
        "Non-magnetic Superalloy Wires"
    ],
    "Structural Supports": [
        "Silicon Carbide Reinforced Polymers",
        "Boron Nitride Ceramic Panels",
        "Carbon-Carbon Composite Trusses"
    ]
}

def validate_material(category, material_name):
    """
    Validate if a given material is approved under IX-Secret-Fusion-Family-Recipe specifications.

    :param category: Material category (str).
    :param material_name: Material name (str).
    :return: Boolean value indicating validity.
    """
    return material_name in APPROVED_MATERIALS.get(category, [])

if __name__ == "__main__":
    test_cases = [
        ("Core Containment Shell", "Tungsten Carbide Alloy"),
        ("Coil and Field Lattice", "Aluminum Wire"),
        ("Structural Supports", "Boron Nitride Ceramic Panels")
    ]

    for category, material in test_cases:
        result = validate_material(category, material)
        status = "APPROVED" if result else "NOT APPROVED"
        print(f"Material: {material} | Category: {category} | Status: {status}")
