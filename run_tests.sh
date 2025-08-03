#!/bin/bash

# Aktifkan virtual environment
source .venv/Scripts/activate  # Untuk Windows (Git Bash)


# Jalankan pytest
pytest test_app.py

# Cek apakah tes sukses (exit code 0 = sukses)
if [ $? -eq 0 ]; then
  echo "All tests passed."
  exit 0
else
  echo "Some tests failed."
  exit 1
fi
