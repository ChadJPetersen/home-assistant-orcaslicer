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
