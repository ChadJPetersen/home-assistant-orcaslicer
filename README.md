# OrcaSlicer for Home Assistant

A Home Assistant App wrapper around LinuxServer.io's web-accessible OrcaSlicer image.

## Update philosophy

This repository intentionally separates **publishing an update** from **installing an update**.

When LinuxServer.io publishes a new OrcaSlicer image:

1. GitHub Actions notices the new upstream release.
2. This repository updates `orcaslicer/config.yaml` to advertise that exact new tag.
3. Home Assistant sees that the repository's latest app version is newer than the
   installed version.
4. Home Assistant shows **Update available**.
5. The installed OrcaSlicer app remains on its current version until the user chooses
   to install the update.

The workflow does **not** pull or restart the running Home Assistant app.

## Version pinning

The repository always uses an explicit LinuxServer.io image tag, for example:

`v2.4.2-ls42`

If you want to advertise a different version:

**GitHub → Actions → Set OrcaSlicer version → Run workflow**

Enter the exact LinuxServer.io tag. The workflow verifies that the image exists for
both `amd64` and `arm64`, then updates the repository metadata.

This makes upgrades, downgrades, and temporary version pins deliberate and reversible.

## Dependabot

Dependabot is enabled for the GitHub Actions used by this repository.

OrcaSlicer itself is tracked by the purpose-built upstream release workflow rather than
Dependabot, because Home Assistant's app `version:` must exactly match the external
container image tag.

## Install

1. Add this GitHub repository URL to the Home Assistant app repository list.
2. Install **OrcaSlicer**.
3. Open the app through Home Assistant Ingress.

## Persistent data

The app maps Home Assistant persistent app data to LinuxServer's `/config`, so profiles
and settings survive image upgrades.

The Home Assistant `/share` folder is also mounted at `/share`.

## Monthly Home Assistant feature compatibility agent

This repository includes a separate **monthly Codex coding agent** (on the **4th day of each month**) that reviews Home Assistant Core/Supervisor releases and app developer documentation for improvements relevant to the OrcaSlicer app. If it finds a justified improvement, it proposes changes in a **pull request**; nothing merges or installs automatically. If no changes are relevant, it leaves the repository untouched. The existing app linter/validation workflow runs on changed app files.

### Enable it

1. Go to **Settings → Secrets and variables → Actions → New repository secret** and create `OPENAI_API_KEY` using a paid OpenAI Platform API key. A ChatGPT subscription alone does not include API credits.
2. Under **Settings → Actions → General**, enable **Allow GitHub Actions to create and approve pull requests** so the bot can propose reviewed changes.
3. Optionally test with **Actions → Monthly Home Assistant compatibility agent → Run workflow**.

The scheduled workflow runs without changes if no relevant feature is identified or if the API key is not configured. API use may incur separate charges. Its AI editing job has no repository write credentials, and a separate job limits file changes and opens a reviewable PR.

See [workflow](.github/workflows/monthly-home-assistant-agent.yml) and [agent instructions](.github/prompts/monthly-ha-compatibility.md). Existing OrcaSlicer upstream image update tracking continues to operate independently.
