#!/bin/bash

echo "🔍 Checking Django Project Structure for LibraryProject..."

# 1️⃣ Check for non-empty README.md inside LibraryProject
if [ -s "Introduction_to_Django/LibraryProject/README.md" ]; then
  echo "✅ README.md exists and is not empty"
else
  echo "❌ README.md missing or empty (expected: Introduction_to_Django/LibraryProject/README.md)"
fi

# 2️⃣ Check for manage.py
if [ -f "Introduction_to_Django/LibraryProject/manage.py" ]; then
  echo "✅ manage.py found in correct location"
else
  echo "❌ manage.py not found in Introduction_to_Django/LibraryProject/"
fi

# 3️⃣ Check for settings.py
if [ -f "Introduction_to_Django/LibraryProject/LibraryProject/settings.py" ]; then
  echo "✅ settings.py found in correct location"
else
  echo "❌ settings.py not found in Introduction_to_Django/LibraryProject/LibraryProject/"
fi

# 4️⃣ Check if settings.py contains INSTALLED_APPS (to confirm valid content)
if grep -q "INSTALLED_APPS" "Introduction_to_Django/LibraryProject/LibraryProject/settings.py"; then
  echo "✅ settings.py has Django configuration (INSTALLED_APPS found)"
else
  echo "❌ settings.py may be incomplete or corrupted (INSTALLED_APPS missing)"
fi

echo "✅ Verification completed!"
