import argparse

from src.agent import TaskPlannerAgent


def parse_args():
    parser = argparse.ArgumentParser(description="Run a simple agent-style task planner.")
    parser.add_argument("--goal", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    agent = TaskPlannerAgent()
    result = agent.run(args.goal)

    print("Goal:")
    print(result["goal"])
    print()

    print("Tools used:")
    for tool in result["tools_used"]:
        print("-", tool)
    print()

    print("Plan:")
    for index, step in enumerate(result["plan"], start=1):
        print(f"{index}. {step}")

    if result["notes"]:
        print()
        print("Relevant notes:")
        for note in result["notes"]:
            print("-", note)


if __name__ == "__main__":
    main()

