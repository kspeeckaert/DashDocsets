# Docset Builder

*If you don't know what docsets are, have a look at [Dash](https://kapeli.com/dash) (macOS) or [Zeal](https://zealdocs.org) (Linux, macOS, Windows) and prepare to increase your productivity tenfold!*

## Instructions

For each docset you want to create, you'll need the following:

- `config` subfolder – hosts the docset related files.
- `download.sh` – Bash script to mirror the site (esentially calling `wget` ).
- `polish.py` – Python script and corresponding `requirements.txt` file to clean up the mirrored files.
- `icon.png` –  the icon of your docset (don't forget to reference this in `dashing.json`).
- `dashing.json` – contains the instructions for [dashing](https://github.com/technosophos/dashing) to build your docset.

> [!IMPORTANT]
> Make sure the `package` key in `dashing.json` is set to the same value as the name of the `config` subfolder.

The resulting docset will  added to the workflow's artifacts.

## Building

The repo contains 2 workflows:

- Build Docset (`build-docset.yml`) – Performs the heavy lifting and generates the docset.
- Build Orchestrator (`build-orchestrator.yml`) – The orchestrator that calls the `build-docset.yml` workflow (by passing the docset name).

The *Build Orchestrater* will gather all docsets created by the individual *Build Docset* jobs, and publish them as a new release.