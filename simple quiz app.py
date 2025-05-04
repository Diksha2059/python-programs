score = 0

q1 = input("What is the capital of France? ")
if q1.lower() == "paris":
    score += 1

q2 = input("What is 5 * 6? ")
if q2 == "30":
    score += 1

print(f"You got {score}/2 correct.")
