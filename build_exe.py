"""
Build executable file using pyisntaller
"""

import PyInstaller.__main__

# 16 bytes
app_encrypt_key="MaZ1!-%!ls98A-2X"

PyInstaller.__main__.run([
    "ktxo/app/main_template.py",
    "--onefile",
    f"--key={app_encrypt_key}",
    "--clean"
])
