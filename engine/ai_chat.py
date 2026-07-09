from engine.generator import generate
from engine.command_engine import execute_command


def ai_chat(project_name):

    print("\n==============================")
    print(f"      Genesis AI Chat ({project_name})")
    print("==============================")
    print("Type 'exit' to go back.\n")

    while True:

        prompt = input("You: ")

        if prompt.lower() == "exit":
            print("\nLeaving AI Chat...\n")
            break

        try:
            result = execute_command(project_name, prompt)

            if result:
                print("\nGenesis AI:")
                print(result)
                print()
                continue

            answer = generate(prompt)

            print("\nGenesis AI:\n")
            print(answer)
            print()

        except Exception as e:
            print(f"\nError: {e}\n")