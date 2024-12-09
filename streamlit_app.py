import os
import xml.etree.ElementTree as ET
import streamlit as st
from pathlib import Path

def ensure_directory_exists(dir_path):
    os.makedirs(dir_path, exist_ok=True)

def apply_file_changes(changes, project_directory):
    for change in changes:
        file_operation = change.get("file_operation").upper()
        file_path = os.path.join(project_directory, change.get("file_path"))
        file_code = change.get("file_code", "")

        if file_operation == "CREATE" or file_operation == "UPDATE":
            ensure_directory_exists(os.path.dirname(file_path))
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(file_code)
        elif file_operation == "DELETE":
            if os.path.exists(file_path):
                os.remove(file_path)
        else:
            st.warning(f"Unknown operation: {file_operation}")

def parse_xml(xml_content):
    root = ET.fromstring(xml_content)
    changes = []
    for file in root.findall(".//file"):
        change = {
            "file_summary": file.findtext("file_summary", ""),
            "file_operation": file.findtext("file_operation", ""),
            "file_path": file.findtext("file_path", ""),
            "file_code": file.findtext("file_code", "")
        }
        changes.append(change)
    return changes

def main():
    st.title("XML to Code File Updater")

    # Project Directory Input
    project_directory = st.text_input("Project Directory:", "/path/to/project")

    # XML Input
    xml_content = st.text_area("Paste XML here:")

    if st.button("Apply"):
        if xml_content and project_directory:
            try:
                changes = parse_xml(xml_content)
                apply_file_changes(changes, project_directory)
                st.success("Changes applied successfully!")
            except Exception as e:
                st.error(f"Error applying changes: {e}")

if __name__ == "__main__":
    main()
