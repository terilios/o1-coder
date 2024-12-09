import os
import shutil
import xml.etree.ElementTree as ET
import streamlit as st

# Backup File Function
def backup_file(file_path):
    backup_path = f"{file_path}.bak"
    shutil.copy(file_path, backup_path)
    return backup_path

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def parse_xml(xml_content):
    root = ET.fromstring(xml_content)
    extracted_data = {}
    for element in root.findall(".//element"):
        key = element.get("name")
        value = element.text
        extracted_data[key] = value
    return extracted_data

def apply_changes_to_code(file_content, changes):
    updated_content = file_content
    for key, value in changes.items():
        updated_content = updated_content.replace(f"{{{{{key}}}}}", value)
    return updated_content

def main():
    st.title("XML to Code File Updater")
    st.markdown(
        '''
        This app allows you to:
        - Upload or paste an XML file containing replacement values.
        - Upload or paste a code file with placeholders.
        - Apply the XML values to the placeholders in the code file.
        '''
    )

    # Step 1: XML Input (File Upload or Text Area)
    st.header("Step 1: Provide XML Input")
    xml_option = st.radio(
        "Choose how to provide XML input:",
        ("Paste XML Text", "Upload a File"),
        index=0  # Default to "Paste XML Text"
    )
    xml_content = None

    if xml_option == "Upload a File":
        xml_file = st.file_uploader("Upload an XML file", type=["xml"])
        if xml_file:
            xml_content = xml_file.read().decode("utf-8")
    elif xml_option == "Paste XML Text":
        xml_content = st.text_area("Paste your XML content here")

    if xml_content:
        st.subheader("Parsed XML Content")
        try:
            parsed_data = parse_xml(xml_content)
            st.json(parsed_data)
            st.session_state["parsed_data"] = parsed_data
        except ET.ParseError as e:
            st.error(f"Error parsing XML: {e}")

    # Step 2: Code Input (File Upload or Text Area)
    st.header("Step 2: Provide Code Input")
    code_option = st.radio(
        "Choose how to provide code input:",
        ("Paste Code Text", "Upload a File"),
        index=0  # Default to "Paste Code Text"
    )
    code_content = None

    if code_option == "Upload a File":
        code_file = st.file_uploader("Upload a Python code file", type=["py"])
        if code_file:
            code_content = code_file.read().decode("utf-8")
    elif code_option == "Paste Code Text":
        code_content = st.text_area("Paste your code content here")

    if code_content:
        st.subheader("Uploaded/Pasted Code")
        st.code(code_content, language="python")
        st.session_state["code_content"] = code_content

    # Step 3: Apply Changes
    if "parsed_data" in st.session_state and "code_content" in st.session_state:
        st.header("Step 3: Apply Changes")
        if st.button("Apply Changes"):
            updated_content = apply_changes_to_code(
                st.session_state["code_content"], st.session_state["parsed_data"]
            )
            st.subheader("Updated Code")
            st.code(updated_content, language="python")
            st.download_button(
                label="Download Updated Code",
                data=updated_content,
                file_name="updated_code.py",
                mime="text/plain",
            )

if __name__ == "__main__":
    main()