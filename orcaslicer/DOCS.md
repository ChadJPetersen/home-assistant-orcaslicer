# OrcaSlicer Home Assistant App

## Normal use

Open OrcaSlicer through the Home Assistant sidebar or **Open Web UI**.

OrcaSlicer configuration is persisted under `/config`.

The Home Assistant `/share` directory is available inside OrcaSlicer at `/share`.

## Updates

When LinuxServer.io publishes a new OrcaSlicer image, this repository automatically
updates the version it advertises to Home Assistant.

Home Assistant will then show an **Update available** notification for the app.

The running app does **not** update itself automatically. It remains on the installed
version until you explicitly choose **Update** in Home Assistant.

## Selecting a different version

The repository owner can run:

**GitHub → Actions → Set OrcaSlicer version → Run workflow**

Supply an exact LinuxServer.io image tag, for example `v2.4.2-ls42`.

The workflow verifies that the image exists for both supported CPU architectures and
then changes the version advertised by this repository.

## Loading models from your phone

Use the Selkies file-transfer interface to upload STL/3MF files, or place models in
Home Assistant's `/share` directory.

## Klipper printers

Configure Moonraker / Klipper print-host addresses inside OrcaSlicer normally. The
container can make outbound connections to printers on your LAN.
