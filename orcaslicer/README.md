# OrcaSlicer

Runs the official LinuxServer.io OrcaSlicer image as a Home Assistant App.

- Browser-accessible through Home Assistant Ingress
- Direct STL/3MF upload from the browser through the Selkies Files sidebar
- Persistent OrcaSlicer profiles, settings, and uploaded files
- Home Assistant `/share` folder mounted at `/share`
- LinuxServer.io upstream release tracking
- Manual version pinning / rollback workflow
- Supports `amd64` and `aarch64`

Browser uploads are enabled by default and are stored in `/config/Desktop`.

The app intentionally does not update itself in the background. When this repository
advertises a newer image tag, Home Assistant presents the update and the user chooses
when to install it.
