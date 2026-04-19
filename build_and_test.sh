#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "--- STARTING SYSTEM BUILD ---"

# 1. Install Python dependencies
echo "Step 1: Installing Python dependencies..."
pip install -r requirements.txt

# 2. Compile C++ Core Logic
echo "Step 2: Compiling C++ Core Logic..."
g++ src/core_logic.cpp -o src/core_logic

# 3. Compile C Integrity Check
echo "Step 3: Compiling C Integrity Check..."
gcc tests/logic_integrity_check.c -o tests/integrity_check

# 4. Run All Tests
echo "Step 4: Running Test Suite..."
python3 -m pytest tests/test_logic.py
./tests/integrity_check

echo "--- ALL SYSTEMS SECURE AND VERIFIED ---"