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

# Execute provided subcommand
if arguments.subparser_name == "create":
    # Create letter
    pass
elif arguments.subparser_name == "validate":
    print("Letter validation is not yet implemented", file=sys.stderr)
else:
    print(f"{arguments.subparser_name} is not a valid command", file=sys.stderr)
    exit(1)