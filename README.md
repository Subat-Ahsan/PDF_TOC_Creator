# Pdf Table of Content Creator

**Tech Used:** Python

## Description

CLI application used to to create or modify the table of content (outline) of a pdf. Uses pymupdf to edit pdf. 

## How to Use

Run the command with the pdf file path as well as the input_data file path. 

```
python TOC.py [pdf_file_path.pdf] -i [input_data_path.txt] [other options]
```

**Input File Format**

Input file needs to be a .txt file with each line defining a heading for the outline. Use `>`s to indicate the heading level, follow it with the name of the heading. Place a comma and the page number after. `>Name|PageNum`

E.G:

```
>Heading 1| 1
>>Sub-Heading 1| 2
>>Sub-Heading 2| 20
>>>Sub-Sub-Heading 1| 45
>Heading 2| 60
```

Lines that do not start with '>' or that contain invalid data will be ignored. The headings also get auto sorted, so if headings with lower page numbers appear later, they will be placed in the correct order.

**Options**

| Option        | Description                                                                                                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| file_path     | The first and only positional arugment. Defines the name of the pdf to use.                                                                                                                       |
| --input, -i   | Defines the input data file to use to input outline headings from. Also where headings are outputted to when using display mode option. **[Required]**                                            |
| --offset, -s  | The amount of offset the heading placement by. E.G: If a heading is supposed to be on page 1, but is on page 21 of the pdf, set `-s 20`, and then input 1 for the heading in the 'input_data.txt' |
| --remove, -r  | Add `-r` flag to command to clear previous table of contents in pdf and only have inputted one.                                                                                                   |
| --output, -o  | Output location of file. If not set, overwrites the input file when saving pdf.                                                                                                                   |
| --display, -d | Stores the pdf's current table of content in the file defined by `-i`. Does not use offset, remove, or output options                                                                             |

**Full Example:** `python TOC.py input.pdf -o output.pdf -s 30 -i a.txt -r`
