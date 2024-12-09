
# XML-to-Code Updater with Streamlit

This project provides a user-friendly Streamlit application to parse XML data and update code files dynamically based on the parsed data. Additionally, it offers support for manual editing using the XML Tools extension in Visual Studio Code for advanced use cases.

## Features

- **Dual Input Options**:
  - Upload XML and code files directly.
  - Paste XML and code content into text areas for quick processing.

- **Streamlit App**:
  - Parses XML content and identifies replacement values.
  - Applies replacements to placeholders in the target Python code file.
  - Displays and allows download of the updated code.

- **Visual Studio Code Support**:
  - Leverage the XML Tools extension for advanced XML parsing and editing.
  - Supports XPath evaluation, XML tree views, and formatting for efficient manual edits.

---

## Installation

### Prerequisites

- Python 3.10+
- Streamlit
- Visual Studio Code (optional, for manual editing with XML Tools)

### Setup

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Install Visual Studio Code and the XML Tools extension:
   - Open VS Code.
   - Go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X`).
   - Search for "XML Tools" and install it.

---

## Running the Streamlit Application

1. Start the Streamlit server:
   ```bash
   streamlit run streamlit_app.py
   ```

2. Open the provided URL in your browser (usually `http://localhost:8501`).

---

## Usage

### Streamlit App Workflow

1. **Provide XML Input**:
   - Choose "Paste XML Text" or "Upload a File".
   - Paste or upload the XML content containing replacement values.

2. **Provide Code Input**:
   - Choose "Paste Code Text" or "Upload a File".
   - Paste or upload the Python code file with placeholders.

3. **Apply Changes**:
   - Click "Apply Changes" to replace placeholders in the code.
   - Review the updated code in the app and download it.

---

### Example XML and Code Files

#### XML File
```xml
<root>
    <element name="variable_1">Value 1</element>
    <element name="variable_2">Value 2</element>
</root>
```

#### Code File
```python
variable_1 = "{{variable_1}}"
variable_2 = "{{variable_2}}"
```

#### Output
```python
variable_1 = "Value 1"
variable_2 = "Value 2"
```

---

## Advanced Editing with Visual Studio Code

For users who prefer manual editing or want advanced XML capabilities:

1. Install the XML Tools extension in VS Code.
2. Open your XML file and use features like:
   - **XML Formatting**: Auto-format the XML content for readability.
   - **Tree View**: Navigate the XML structure visually.
   - **XPath Evaluation**: Query specific XML elements or attributes.

---

## Project Structure

```
.
├── streamlit_app_updated.py   # Streamlit application
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker container setup
├── .dockerignore              # Docker ignored files
├── README.md                  # Documentation
└── prompt.md                  # Prompt for OpenAI o1 model
```

---

## Running in Docker (Optional)

1. Build the Docker image:
   ```bash
   docker build -t xml-to-code-updater .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8501:8501 xml-to-code-updater
   ```

3. Access the app at `http://localhost:8501`.

---

## Contributions

Contributions are welcome! Please follow these steps:

1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch:
   ```bash
   git push origin feature-name
   ```
4. Open a pull request.

---

## License

This project is licensed under the MIT License.

---

## Support

For questions or issues, please open an issue in this repository.
