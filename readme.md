# Docset Builder

*If you don't know what docsets are, have a look at [Dash](https://kapeli.com/dash) (macOS) or [Zeal](https://zealdocs.org) (Linux, macOS, Windows) and prepare to increase your productivity tenfold!*

## Instructions

For each docset you want to create, you'll need the following:

- A subfolder within `config` to host the docset related files.
- A `download.sh` file that contains a Bash script (esentially calling `wget` to mirror the site).
- A `polish.py` Python file and corresponding `requirements.txt` file to clean up the mirrored files.
- A `icon.png` that will serve as the icon of your docset
- A `dashing.json` file that contains the instructions for [dashing](https://github.com/technosophos/dashing) to build your docset.

The resulting docset will be zipped and added to the workflow's artifacts.