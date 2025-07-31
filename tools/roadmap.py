# from agents import function_tool

# @function_tool
# def get_career_roadmap(field: str) -> str:
#     """Returns a roadmap of skills for a given career field."""
#     field = field.strip().lower()
#     print(f"DEBUG: get_career_roadmap called with field = '{field}'")

#     maps = {
#         "data science": "1. Python\n2. Statistics\n3. Machine Learning\n4. SQL\n5. Data Visualization",
#         "data analyst": "1. Excel\n2. SQL\n3. Data Cleaning\n4. Data Visualization (Tableau/Power BI)\n5. Basic Statistics",
#         "cybersecurity": "1. Linux\n2. Networking\n3. Penetration Testing\n4. Cryptography\n5. Incident Response",
#         "web development": "1. HTML/CSS\n2. JavaScript\n3. React\n4. Node.js\n5. APIs",
#         "it": "1. Networking Basics\n2. System Administration\n3. Cloud Computing\n4. Security Fundamentals\n5. Virtualization",
#         "information technology": "1. Networking Basics\n2. System Administration\n3. Cloud Computing\n4. Security Fundamentals\n5. Virtualization",
#         "machine learning engineer": "1. Python\n2. Statistics\n3. Machine Learning Algorithms\n4. Deep Learning\n5. Data Engineering",
#     }
#     return maps.get(field, "No roadmap available for this field.")


from agents import function_tool  # Import decorator to convert Python functions into tools usable by agents

# Define the tool function with decorator
@function_tool
def get_career_roadmap(field: str) -> str:
    """Returns a roadmap of skills for a given career field."""
    
    # Normalize input: remove extra spaces and convert to lowercase for matching keys
    field = field.strip().lower()
    print(f"DEBUG: get_career_roadmap called with field = '{field}'")  # Debug print to trace calls and inputs

    # Dictionary containing skill roadmaps for various career fields
    maps = {
        "data science": "1. Python\n2. Statistics\n3. Machine Learning\n4. SQL\n5. Data Visualization",
        "data analyst": "1. Excel\n2. SQL\n3. Data Cleaning\n4. Data Visualization (Tableau/Power BI)\n5. Basic Statistics",
        "cybersecurity": "1. Linux\n2. Networking\n3. Penetration Testing\n4. Cryptography\n5. Incident Response",
        "web development": "1. HTML/CSS\n2. JavaScript\n3. React\n4. Node.js\n5. APIs",
        "it": "1. Networking Basics\n2. System Administration\n3. Cloud Computing\n4. Security Fundamentals\n5. Virtualization",
        "information technology": "1. Networking Basics\n2. System Administration\n3. Cloud Computing\n4. Security Fundamentals\n5. Virtualization",
        "machine learning engineer": "1. Python\n2. Statistics\n3. Machine Learning Algorithms\n4. Deep Learning\n5. Data Engineering",
    }

    # Return the roadmap if field matches; otherwise return default message
    return maps.get(field, "No roadmap available for this field.")
