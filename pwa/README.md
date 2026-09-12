# Progressive Web App

This edition adds an application manifest, service worker, install icons and offline application-shell caching.

## Requirements

- Publish the complete `pwa` directory.
- Use HTTPS in production.
- Keep relative paths unchanged.
- Open the hosted page in a browser that supports PWA installation.

The Install button becomes available when the browser reports that the application is eligible for installation. The browser menu or address-bar installation control can also be used.

## Updating

Change `CACHE_NAME` in `service-worker.js` when releasing updated application files. Test first load, update, offline launch, uninstall and reinstall before publishing a release.
