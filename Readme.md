## Academic GitHub IO Page Markdown Style

## Important Files

* `./src/mainstructure.html` serves as the basis for each page. In there, the navigation bar's links and portrait as well as the footer can be edited in there.

* `src/styles.css` defines the page's style. Page layout is mainly inherited from w3.css, while text styling is modified from markdown-to-html-github-style.

* Referenced images are stored in `img`. You may want to copy this folder into `src` for local preview.

* `src/build.py` parses the template and markdown files defining content and generates static single file pages. 

* `src` contains markdown files that define the content of each page
  - `cv.md`: Curriculum Vitae
  - `mainpage.md`: Landing Page
  - `projects.md`: Practical Projects 
  - `teaching_experience.md`: List of conducted lectures
  - `publications/`: Directory containing markdown files defining publications. However, each publication must be explicitly configured with metadata in `build.py`. The subpage listing all publications is generated automatically from the metadata.

## Template Usage - Add Content

1. Fill in personal information in `./src/mainstructure.html`
2. Fill in markdown pages for static subpages
3. Create a markdown file for each publication page
4. Add each publication's metadata in `build.py`
5. Run `./build.py` to generate static single-file pages

