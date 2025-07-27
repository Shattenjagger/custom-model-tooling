import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("file-storage")

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

os.makedirs(BASE_DIR, exist_ok=True)

@mcp.tool()
def create_text_file(name: str, content: str):
    """
    Creates a text file with the given name and content in the BASE_DIR directory.
    If the file already exists, it will be overwritten.
    """
    if not name.endswith(".txt"):
        name += ".txt"
    file_path = os.path.join(BASE_DIR, name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return {"status": "success", "file": file_path}

@mcp.tool()
def list_files():
    """
    Lists all files in the BASE_DIR directory.
    Returns a list of file names.
    """
    try:
        files = os.listdir(BASE_DIR)
        return {"files": files}
    except Exception as e:
        return {"error": str(e)}
    
@mcp.tool()
def get_file(name: str):
    """
    Retrieves the content of a specified file from the BASE_DIR directory.
    Args:
        name (str): The name of the file to retrieve.
    Returns:
        dict: A dictionary containing the file content or an error message.
    """
    if not name.endswith(".txt"):
        name += ".txt"
    file_path = os.path.join(BASE_DIR, name)
    if not os.path.isfile(file_path):
        return {"error": f"File '{name}' does not exist."}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"file": name, "content": content}
    except Exception as e:
        return {"error": str(e)}
    
if __name__ == "__main__":
    mcp.run(transport="stdio")