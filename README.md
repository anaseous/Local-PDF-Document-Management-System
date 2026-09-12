# PDF Document Workspace

A browser-based workspace for viewing, merging, splitting, rearranging, rotating, annotating, signing, editing and exporting PDF documents. Document processing remains in the browser.

## Editions

- **Single-page web app:** `single-page/index.html` contains the application and embedded libraries in one file. It can be opened directly or hosted as a static page.
- **Progressive Web App:** `pwa/` adds an application manifest, install icons, service worker and offline application-shell cache. Host this edition over HTTPS for installation.

## Publish with GitHub Pages

1. Create a repository and upload the contents of this archive, not the outer folder.
2. Open **Settings > Pages**.
3. Under **Build and deployment**, choose **GitHub Actions**.
4. Push to the `main` branch. The included workflow publishes the repository.
5. Open the deployed `/pwa/` path in a supported browser to install the PWA.

GitHub Pages project paths are supported because all application assets use relative URLs.

## Local test

```bash
python3 -m http.server 8080
```

Open `http://localhost:8080/`. Do not test PWA installation by opening `index.html` through a `file://` URL.

## Privacy

PDF documents are processed locally by the browser. The service worker caches application files only. Saved signatures use browser local storage.

## Security

Review `SECURITY.md` before publishing. Test changes with representative PDF files before release.
