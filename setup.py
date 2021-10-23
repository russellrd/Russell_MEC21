import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

cx_Freeze.setup(
    name="VSVS",
    options={"build_exe": {"packages": ["tkinter", "cv2", "PIL"]}},
    version="0.01",
    description="Very Secure Voting System",
    executables=[cx_Freeze.Executable(
        "app.py", base=base, targetName="VSVS")]
)
