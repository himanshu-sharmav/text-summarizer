
---

# Text Summarizer CLI Tool

This command-line tool summarizes text provided either directly or from a text file using the Ollama API and Qwen2 0.5B model. The tool is built with Python and utilizes the Click library for the command-line interface.

## Features

- Summarize text provided as a direct input
- Summarize text from a file
- Integration with Ollama API and qwen2 0.5b model

## Prerequisites

- Python 3.7+
- Pip

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/text-summarizer-cli.git
   cd text-summarizer
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```
3. **To install model:**
    '''sh
    ollama run qwen2:0.5b
    '''

## Usage

You can use the tool to summarize text either from a direct input or from a file.

### Summarize Text from a File

```sh
python summarizer.py -f path/to/your/textfile.txt
```

### Summarize Direct Text Input

```sh
python summarizer.py -t "The quick brown fox jumped over the lazy dog."
```

## Example

### File Input

```sh
python summarizer.py -f book.txt
```

**Output:**

```
Summary of book.txt:
[Generated summary of the text file]
```

### Direct Text Input

```sh
python summarizer.py -t "The quick brown fox jumped over the lazy dog."
```

**Output:**

```
Summary of provided text:
[Generated summary of the text]
```

## Project Structure

```
text-summarizer/
│
├── summarizer.py          # Main script for the CLI tool
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.


## Contact

For any questions or suggestions, please contact [Himanshu Sharma](mailto:himan9506492198@gmail.com).

---
.
