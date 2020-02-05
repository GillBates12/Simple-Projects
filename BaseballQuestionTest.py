import random

questionDict = {'Red Sox': 'Jeff Bagwell', 'Dodgers': 'Roberto Clemente', 'Tigers': 'John Smoltz',
                'Rockies': 'Clayton Kershaw', 'Padres': 'A.J Burnett', 'Pirates': 'Bob Gibson', 'Mets': 'Darryl Kylie'}

score = 0
questionList = list(questionDict.keys())
random.shuffle(questionList)
for i in range(len(questionDict)):
    if i <= 2:
        print(15*"-")
        print(str(i+1) + " Who was the first team to draft this player? " + questionList[i])
    if i >= 3:
        print(15*"-")
        print(str(i+1) + " What team did this player throw a no-hitter against? " + questionList[i])
    options = []
    correctAnswer = questionDict[questionList[i]]
    answers = list(questionDict.values())
    answers.remove(correctAnswer)
    wrongAnswer = random.sample(answers, 3)
    options.append(correctAnswer)
    options = options + wrongAnswer
    random.shuffle(options)
    for j in range(len(options)):
        print(str(j+1) + " " + options[j])
    print("Choose the correct answer: ")
    answerIndex = int(input())
    if options[answerIndex - 1] == correctAnswer:
        score = score + 10
print("score: " + str(score) + " You got "+ str(int(score / 10)) + " correct!")












