import shutil
import subprocess
import sys

# Each tool and the command that prints its version
tools = {
    "uv": ["uv", "--version"],
    "VS Code": ["code", "--version"],
    "Git": ["git", "--version"],
    "Ollama": ["ollama", "--version"],
    "Claude Code": ["claude", "--version"],
}


def get_version(command):
    path = shutil.which(command[0])
    if path is None:
        return "not installed"
    result = subprocess.run([path, *command[1:]], capture_output=True, text=True)
    # Some tools print several lines; the first line holds the version
    return result.stdout.strip().splitlines()[0]


My_toolkit = {"Python": sys.version.split()[0]}
for name, command in tools.items():
    My_toolkit[name] = get_version(command)

print("My toolkit includes:")
for name, version in My_toolkit.items():
    print(f"  {name}: {version}")
