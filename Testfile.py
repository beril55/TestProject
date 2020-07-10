
from question_class import question

question_prompt = [
        "\n(1) Which is more precious?\n(a) Gold\n(b) Silver\n(c) Platinum\n\n",
        "\n(2) Which is more bright\n(a) Wall\n(b) Metal\n(c) Stone\n\n",
        "\n(3) Which is more colorful\n(a) Flower\n(b) Cloud\n(c) Rainbow\n\n"
                   ]
questions_set1 = [
        question(question_prompt[0], "c"),
        question(question_prompt[1], "b"),
        question(question_prompt[2], "c")
        ]


def run_test(questions):
    score = 0
    for i in questions:
        while True:
            try:
                ans = input(i.prompt)
                if ans.casefold() == "a" or ans.casefold() == "b" or ans.casefold() == "c":
                    if ans == i.answer:
                        score += 1
                else:
                    raise ValueError()
                break
            except:
                print("\nInvalid input!\nTry Again")
                continue
            #else:
                #break
    if score > 0:
        print("\nYou answered " + str(score) + " out of " + str(len(questions)) + " questions correctly.\n")
    else:
        print("\nNone of the answers are correct\n")

def main():
    run_test(questions_set1)

if __name__ == '__main__':
    main()

#end of code
