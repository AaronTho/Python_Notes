from pathlib import Path

# Absolute path -the root of the drive
# Relative path -the current directory

path = Path("ecommerce")
for file in path.glob('*'):
    print(file)

# path.exists() returns boolean T/F
# path.mkdir() creates the directory
# pasth.rmdir() removes the directory
