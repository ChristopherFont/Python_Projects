def question(question, key, score):
    answer = input(question)
    if answer.lower() == key:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect!")
    return score

print("Hello, welcome to the quiz game!")
score = 0
playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

score = question("What does CPU stand for? ", "central processing unit", score)
score = question("Do cats like to be petted? ", "yes", score)
score = question("2 + 2 = ? ", "4", score)
score = question("Is privacy a human right? ", "no", score)
score = question("What does RAM stand for? ", "random access memory", score)
score = question("Is gender a construct? ", "yes", score)
score = question("2 * 6 = ? ", "12", score)
score = question("What is an albatross? ", "bird", score)
score = question("Do cats need fur? ", "no", score)
score = question("Is this a good quiz? ", "yes", score)

print("Finished!")
print("Total Score %d/10" % score)
