"""
IX-Secret-Fusion-Family-Recipe License Header Module

This module provides the IX-SFFR custom license header string for embedding in
all Python modules within the repository.

Author: Bryce W. Design
Date: July 2025
"""

IX_SFFR_LICENSE_HEADER = """
IX-Secret-Fusion-Family-Recipe

Open Source Civilian-Use License (IX-SFFR Custom License v1.0)

Copyright (c) 2025 Bryce W. Design

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, subject to the following conditions:

1. Civilian-Use Only: This Software is licensed strictly for non-military,
   non-defense, non-classified applications. Export-controlled technologies
   (TAR, EAR) are not included.

2. Educational Purpose: This Software is for educational, scientific
   research, and theoretical simulation use only. No real-world plasma
   reactors, ignition systems, or fusion devices are represented.

3. Software Limitations: The Software is provided "AS IS", without warranty
   of any kind, express or implied, including but not limited to the
   warranties of merchantability, fitness for a particular purpose, and
   noninfringement. In no event shall the authors or copyright holders be
   liable for any claim, damages, or other liability.

By using or modifying this Software, you agree to these license terms.
"""

def get_license_header():
    """
    Return the IX-SFFR license header string.
    """
    return IX_SFFR_LICENSE_HEADER

if __name__ == "__main__":
    print(get_license_header())
