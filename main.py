# Copyright (C) 2021 Aayla Semyonova
# 
# This file is part of SecureLetter.
# 
# SecureLetter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# SecureLetter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with SecureLetter.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import os
import sys
import yaml
import hashlib

# Set up argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", "-v", help="Increase output verbosity")
subparsers = parser.add_subparsers(dest="subparser_name", required=True)
# Arguments for "run" subcommand
run_subparser = subparsers.add_parser("create")
run_subparser.add_argument("source", help="YAML file to generate letter from")
# Arguments for "validate" subcommand
validate_subparser = subparsers.add_parser("validate")
arguments = parser.parse_args()

SCRIPT_PATH = os.path.split(__file__)[0]

def generate_letter(path):
    # Ensure the given path to YAML content exists
    if not os.path.exists(path):
        print(f"Path {path} does not exist!", file=sys.stderr)
        exit(1)
    # Ensure the given path to YAML content is a file
    if not os.path.isfile(path):
        print(f"Path {path} is not a file!", file=sys.stderr)
        exit(1)
    # Attempt to open the file as YAML
    with open(path, "r") as inputFile:
        yaml_content = yaml.load(inputFile, Loader=yaml.FullLoader)
    with open(f"{SCRIPT_PATH}/res/template.tex", "r") as file:
        final_output = file.read()
    
    content = ""
    sums = []
    firstitem = None

    # Add title to final output
    final_output = final_output.replace("!!!TITLE!!!", yaml_content["title"])
    # Create content from sections
    for section in yaml_content["content"]:
        content += "\section{" + section + "}\n"
        for item in yaml_content["content"][section]:
            if type(item) == str:
                if firstitem is None:
                    firstitem = item
                sha = hashlib.sha256((item + "\n").encode()).hexdigest()
                sums.append(sha)
                content += f"\para {item}"
                content += "\endnote{" + sha + "}\n"
            if type(item) == dict:
                for part in item:
                    if firstitem is None:
                        firstitem = part
                    sha = hashlib.sha256((part + "\n").encode()).hexdigest()
                    sums.append(sha)
                    content += f"\para {part}\endnote" + "{" + sha + "}\\begin{enumerate}\n"
                    for line in item[part]:
                        content += f"\item {line}"
                        sha = hashlib.sha256((line + "\n").encode()).hexdigest()
                        sums.append(sha)
                        content += "\endnote{" + sha + "}\n"
                content += "\\end{enumerate}\n"

    # Apply final_content to final_output
    final_output = final_output.replace("!!!CONTENT!!!", content)
    # Create FINALSUM
    finalsum = (",".join(sums) + ",").encode()
    finalsum = hashlib.sha256(finalsum).hexdigest()
    final_output = final_output.replace("!!!FINALSUM!!!", finalsum)
    # Create FINALSUM_AB
    finalsum_ab = finalsum[:4] + "..." + finalsum[-4:]
    final_output = final_output.replace("!!!FINALSUM_AB!!!", finalsum_ab)
    # Create FIRSTITEM
    final_output = final_output.replace("!!!FIRSTITEM!!!", firstitem)
    # Create FINGERPRINT
    final_output = final_output.replace("!!!FINGERPRINT!!!", yaml_content["fingerprint"])
    # Print final output
    print(final_output)
    # print(",".join(sums))

def validate_letter():
    pass

# Execute provided subcommand
if arguments.subparser_name == "create":
    generate_letter(arguments.source)
elif arguments.subparser_name == "validate":
    print("Letter validation is not yet implemented", file=sys.stderr)
else:
    print(f"{arguments.subparser_name} is not a valid command", file=sys.stderr)
    exit(1)