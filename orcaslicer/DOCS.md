# OrcaSlicer Home Assistant App

## Normal use

Open OrcaSlicer through the Home Assistant sidebar or **Open Web UI**.

OrcaSlicer configuration is persisted under `/config`.

The Home Assistant `/share` directory is available inside OrcaSlicer at `/share`.

## Configuration

The Home Assistant **Configuration** tab exposes a small set of settings that map
directly to LinuxServer.io / Selkies environment variables:

- **Container user ID (PUID)** and **group ID (PGID)** default to LinuxServer's
  Selkies defaults of 911.
- **Use Wayland** selects Wayland or the X11 fallback.
- **Initial stream frame rate** controls browser-stream smoothness.
- **Stream quality (CRF)** controls streamed desktop image quality; lower is higher
  quality.

Because this app uses Home Assistant's `legacy: true` mode for a third-party image,
Supervisor passes scalar app options into the container as environment variables.

Home Assistant itself supplies the container timezone, so a separate timezone option is
not needed.

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

## Troubleshooting installation

The LinuxServer OrcaSlicer image is large (roughly 1.6 GB compressed on amd64), so the
first install can take a while even before the app is started.

If the Install button returns immediately or the app never becomes installed, open:

**Settings → System → Logs → Supervisor**

and look for messages containing `orcaslicer`, `lscr.io`, `docker`, or `pull`.
Those messages identify registry, disk-space, architecture, or Docker errors that are
not visible from the repository itself.
