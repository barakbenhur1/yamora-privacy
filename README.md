# Publish the Yamora privacy site

This folder is a standalone static site. It contains no Yamora source code and
no credentials.

## Recommended GitHub Pages setup

1. Sign in to GitHub and create a new **public** repository named
   `yamora-privacy`. Do not initialize it with a README.
2. In Terminal, run the commands supplied with this package to push these files.
3. In the new repository, open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch **main**, folder **/(root)**, and click **Save**.
6. Wait for the Pages deployment to finish, then open:
   `https://barakbenhur1.github.io/yamora-privacy/`
7. Confirm that the privacy page opens at:
   `https://barakbenhur1.github.io/yamora-privacy/privacy.html`

Use the privacy-page URL in the Chrome Web Store Developer Dashboard.

## Important

- Do not add passwords, MongoDB connection strings, collector tokens, signing
  keys, or other secrets to this repository.
- The policy reflects Yamora v0.15.0, the Frankfurt Render services, MongoDB
  Atlas, GitHub Actions, Ko-fi/PayPal voluntary support, 730-day export
  retention, and the current explicit opt-in model-improvement flow.
- Obtain jurisdiction-appropriate legal review before a broad public launch.
