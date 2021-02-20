[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg?style=flat-square)](https://opensource.org/licenses/)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/NbAayla/SecureLetter?style=flat-square)
# SecureLetter
While returning from a protest that was more dangerous than I was expecting, I decided it was important to convey my last wishes in a letter. However, this lead to a critical question that I had to answer.
> With traditional digital files, it's trivial to cryptographically sign a PDF with GPG. However, digital files are ephemeral. If I'm dead, any files I host online are gone as soon as I stop paying rent. How can I get the same assurances of mathematically provable authenticity and authorship on a printed document?

After struggling with this question for 4 days, I finally reached a format that proves the authorship and authenticity of every character of a letter in a way that can be independently verified without any guesswork about formatting. This project, SecureLetter, is about making verifiable printed letters easy to make for anyone with GPG and Python installed on a Linux machine.

## Usage
To create a crpyotgraphically signed and tamper-evident letter, create an appropriately formatted YAML file and run `python main.py create example.yaml`. The output **MUST** be rendered with XeLaTeX.
### Example Letter
The `letter.yaml` file is included as an example letter.
```yaml
title: Important Letter

content:
  Section 1:
    - Important Declaration
    - Second Important Declaration
  Section 2:
    - Third Important Declaration
    - Fourth Impotant Declaration
  Section 3:
    - Fifth Declaration with enumeration:
      - Item 1
      - Item 2
```
## Rendering
I suggest using [Overleaf](https://overleaf.com) to render the output TeX code paired with the other content in `/res`.
## Credit
The LaTeX template used to make these letters is a heavily modified version of Rob Oakes's Memo class.
