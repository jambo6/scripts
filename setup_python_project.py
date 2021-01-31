"""
setup_python_project.py
=====================================
For setting up a new blank project. Includes conda environment creation, a standard gitignore, basic requirements
installation, and black/flake8 with pre-commits if specified.
"""
import os
import pathlib
import argparse
import shutil
import subprocess

# Args
parser = argparse.ArgumentParser(description="Creation of a new python project.")
parser.add_argument('foldername', type=str, help='The name of the folder to create.')
parser.add_argument('--pyversion', type=str, default=3.8, help="The python version to use.")
parser.add_argument('-r', '--requirements', action='store_true', help="Flag to install a basic set of requirements.")
parser.add_argument('-pre', '--pre_commit', action='store_true', help="Adds black, flake8, pytest precommits.")
args = parser.parse_args()

# Get the script location and the run location
script_path = pathlib.Path(__file__).parent.absolute()
assets_path = pathlib.Path(script_path) / 'assets'
folder = args.foldername
true_location = os.getcwd() + '/' + folder

# Get folder, ensure does not exists
if not os.path.isdir(folder):
    os.mkdir(folder)
else:
    raise FileNotFoundError("Folder at {} already exists, it needs to be deleted first.".format(folder))

# Run conda with python
subprocess.check_call(
    'cd {};'.format(folder)
    +
    'conda create -p env python=={} -y'.format(args.pyversion),
    shell=True
)

# Copy over the gitignore
shutil.copy('{}/simple_gitignore.txt'.format(assets_path), '{}/.gitignore'.format(folder))

# If pre-commit, add all those bells and whistles
if args.pre_commit:
    files = os.listdir(assets_path / 'pre-commit')
    for file in files:
        shutil.copy(assets_path / 'pre-commit/{}'.format(file), '{}/{}'.format(folder, file))

# Add requirements if specified, else an empty requirements file
if args.requirements:
    shutil.copy(assets_path / 'requirements.txt', '{}/requirements.txt'.format(true_location))
    subprocess.check_call(
        'source ~/opt/miniconda3/etc/profile.d/conda.sh;' +
        'cd {};'.format(true_location) +
        'conda activate ./env;' +
        'pip install -r requirements.txt',
    shell=True)
else:
    subprocess.check_call('touch {}/requirements.txt'.format(folder), shell=True)
