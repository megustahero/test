import os

# Step 1: Initialize an empty Git repository
def initialize_git_repo():
    os.system("git init")
    # Add an initial commit so the Java check won't fail
    with open('initial.txt', 'w') as f:
        f.write('initial commit file')
    os.system("git add initial.txt")
    os.system("git commit -m 'Initial commit'")

# Step 2: Create a pre-commit hook to validate coverage
pre_commit_script = '''#!/bin/sh
COVERAGE=$(cat coverage-report.txt)
if [ "$COVERAGE" -lt 80 ]; then
    echo "Commit rejected: Coverage is too low ($COVERAGE%)"
    exit 1
fi
'''

def create_pre_commit_hook():
    hook_path = os.path.join('.git', 'hooks', 'pre-commit')
    with open(hook_path, 'w') as f:
        f.write(pre_commit_script)
    os.chmod(hook_path, 0o775)

# Step 3: Create the coverage-report.txt file with a default value
def create_coverage_report():
    with open('coverage-report.txt', 'w') as f:
        f.write('100')  # Starting with a high number to ensure the first commit passes

# Execute the setup steps
initialize_git_repo()
create_pre_commit_hook()
create_coverage_report()