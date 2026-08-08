
def get_scores():
    """
    Get valid scores from the user.
    
    """
    scores = []
    user_input = input("Enter scores (separate with spaces :\n")

    for item  in user_input.split():
        try :
            score = float(item)

            if 0 <= score<= 20:
                scores.append(score)
            else:
                print(f"Invalid score: {item} Score must be between 0 and 20")

        except ValueError:
            print(f"'{item } ' is not a valid number.")

    return scores


def show_results(scores):
    
    mean = sum(scores) /len(scores)

    print(f"Mean: {mean:.2f}")
    print(f"Maximum:{max(scores):.2f}")
    print(f"Minimum : {min(scores):.2f}")


def main():
    
    
    print("Welcome to the Grade Manager!")
    print('This is a fun and simple project')

    while True:
        scores = get_scores()

        if not scores:
            print("No valid scores were entered.\n")
            continue

        show_results(scores)

        again = input("\nDo you want to use the Grade Manager again? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
