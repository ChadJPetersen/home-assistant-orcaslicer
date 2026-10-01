# OrcaSlicer

Runs the official LinuxServer.io OrcaSlicer image as a Home Assistant App.

- Browser-accessible through Home Assistant Ingress
- Persistent OrcaSlicer profiles and settings
- Home Assistant `/share` folder mounted at `/share`
- LinuxServer.io upstream release tracking
- Manual version pinning / rollback workflow
- Supports `amd64` and `aarch64`

The app intentionally does not update itself in the background. When this repository
advertises a newer image tag, Home Assistant presents the update and the user chooses
when to install it.
