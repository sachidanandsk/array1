def main():
    scores = [10, 20, 30, 50]
    total = sum(scores)
    average = total / len(scores)

    print("=== main/master branch output ===")
    print(f"Scores = {scores}")
    print(f"Average = {average}")
    print("\n=== local branch output (max & min) ===")
    print(f"Maximum: {max(scores)}")
    print(f"Minimum: {min(scores)}")



if __name__ == "__main__":
    main()
