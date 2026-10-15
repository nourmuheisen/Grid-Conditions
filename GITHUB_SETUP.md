# Put GRID / CONDITIONS on GitHub

The site is already built. You do not need npm, a framework, a database, API keys, a custom domain or a build workflow.

## 1. Extract and inspect

Extract `Grid-Conditions-GitHub.zip`. Open `index.html` to review the website. Keep every file and the `src` and `scripts` folders together. This package preserves the national 12-case research snapshot; it does not refresh the underlying research.

## 2. Create a repository and upload

On GitHub, create a repository, for example `grid-conditions`. For a public portfolio, choose a public repository. Leave automatic README and license creation unchecked because the package contains a README and no license choice has been made.

Use the repository's upload-files option. Upload the **extracted files and folders**, not the ZIP and not an enclosing folder. Commit the upload to `main`. Check that `index.html`, `README.md` and `evidence.json` appear directly at the repository root. Include `.nojekyll` and `.gitignore`; if your file picker hides them, show hidden files or create them in GitHub using the contents in this package. `.nojekyll` is intentionally empty.

You can stop here if you only want the files on GitHub. Enabling Pages in the next step publishes the website.

## 3. Publish only when ready

In repository **Settings → Pages**, under **Build and deployment**, choose **Deploy from a branch**. Select branch **main**, folder **/(root)**, then save. GitHub will display the site address once deployment succeeds. Use that address; a project site normally includes the repository name after your username's github.io domain. A custom domain is optional; leave the custom-domain field empty unless you own one and want to configure it.

Official instructions (checked 15 October 2026):
- [Configure the publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Create a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

## 4. Review the published version

Check the mobile and desktop layouts, case filters, comparison, evidence links, scenario notes, note export and research downloads. Notes are session-only and disappear on reload unless exported. The hosting path can include a repository name; the package uses relative links to support this.

## Updating later

Edit `evidence.json` for evidence, `src/template.html` for the design, and Markdown documents for narrative changes. From the repository folder run:

```sh
python3 scripts/build.py
node scripts/check.mjs
```

Python and Node.js are needed only for these optional maintenance commands, not to view or initially host the site. The Python builder uses only the standard library; the Node check uses built-in modules. Commit the regenerated `index.html` and exports alongside your source changes. Keep source dates and uncertainty labels intact.

## Common issues

- **404 at the site URL:** confirm Pages is enabled and `index.html` is at the selected branch's root. Check deployment status in GitHub.
- **Research links fail:** upload all accompanying files, not just the HTML.
- **Edits do not appear:** rebuild after editing the template or JSON, then upload the generated files too.

This package creates no GitHub repository and publishes nothing by itself.
