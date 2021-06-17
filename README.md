<!-- Add banner here -->

![image-20210617093944919](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20210617093944919.png)

# IconsReplace-Alfred

<!-- Add buttons here -->

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Jechin/IconsReplace-Alfred?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/Jechin/IconsReplace-Alfred)
![GitHub](https://img.shields.io/github/license/Jechin/IconsReplace-Alfred)

<!-- Describe your project in brief -->

This project can be used to simplify the process of custom replacement of application icons. It is convenient to replace again after the application is updated.

This pThis project is based on Alfred and workflow. The workflow depends on a well developed Open Source Shell program [***fileicon***](https://github.com/mklement0/fileicon), and specail thank to mklement0](https://github.com/mklement0). 

Users save the icon file (.icon or .png) needed for replacement in a separate folder, and the workflow will search for icons in the folder and find the corresponding app to replace it.

# Table of contents

After you have introduced your project, it is a good idea to add a **Table of contents** or **TOC** as **cool** people say it. This would make it easier for people to navigate through your README and find exactly what they are looking for.

Here is a sample TOC(*wow! such cool!*) that is actually the TOC for this README.

- [IconsReplace-Alfred](#IconsReplace-Alfred)
- [Demo-Preview](#demo-preview)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contribute](#contribute)
  - [Sponsor](#sponsor)
  - [Adding new features or fixing bugs](#adding-new-features-or-fixing-bugs)
- [License](#license)
- [Footer](#footer)

# Installation

[(Back to top)](#table-of-contents)

## Supported platform and environment:

* macOS
* Alfred with workflow

## Download and Installation

Just download and double click the [workflow file](https://github.com/Jechin/IconsReplace-Alfred/releases) Say "yes" to import it into Alfred. Done!

# Usage

[(Back to top)](#table-of-contents)

## Preparation

1. Create a new folder ( in anywhere you what) to store the icons needed for replacement

2. Save the icon file (.icon or .png) needed for replacement in a separate folder, and ***the icon file must be named after the exact name of named after the precise name of the app***.

3. Add Workflow Environment Variables

   <img src="https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20210617122057480.png" alt="image-20210617122057480" style="zoom:50%;" />

   * Copy the path of folder you just create and paste in `icons_filepath` Value

<img src="https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20210617122227124.png" alt="image-20210617122227124" style="zoom:50%;" />

## Usage

### Replace Icon

Use command `iconsse `, and choose one icon or all icons (the first option)

![image-20210617155936819](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20210617155936819.png)

### Remove Icon from App

Use command `iconsrm`, and choose one icon or all icons (the first option)

![image-20210617160007221](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20210617160007221.png)

# License

[(Back to top)](#table-of-contents)

Copyright (c) 2021 Jechin, release under [MIT License](https://spdx.org/licenses/MIT#licenseText).



<!-- Add the footer here -->

