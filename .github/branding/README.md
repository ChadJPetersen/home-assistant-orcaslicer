# App branding source

The file `orcaslicer-mark.svg` was copied from the upstream OrcaSlicer project:
[OrcaSlicer/OrcaSlicer — resources/images/studio_logo.svg](https://github.com/OrcaSlicer/OrcaSlicer/blob/main/resources/images/studio_logo.svg).

The GitHub Actions branding workflow runs `scripts/generate_branding.py` to create
the Home Assistant app's `orcaslicer/icon.png` (128 × 128) and
`orcaslicer/logo.png` (250 × 100). It preserves the proportions and artwork
of the official logo, adding only contrast backplates and an OrcaSlicer wordmark
for Home Assistant light/dark themes.

These images are **repository metadata**, not part of the LinuxServer.io OrcaSlicer
container. They are refreshed by reloading the app repository in Home Assistant;
no container update, new image version, or loss of profiles is required.

OrcaSlicer artwork belongs to its upstream copyright/trademark holders.
This independent Home Assistant wrapper is not an official OrcaSlicer release.
