from engine.memory_engine import load_project_data


def continue_project(project_name):

    data = load_project_data(project_name)

    print("\n==============================")
    print("PROJECT INFORMATION")
    print("==============================")

    print(f"Project : {data.get('project_name', '')}")
    print(f"Idea    : {data.get('idea', '')}")
    print(f"Story   : {data.get('story', '')}")
    print(f"Version : {data.get('version', '')}")

    print("==============================")