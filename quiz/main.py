
import sys

def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku")
        input("Naciśnij dowolny klawisz aby zakończyć program")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    return question, answers, correct

def main():
    human_file = open_file("pytania.txt", "r")
    title = next_line(human_file)
    print(f'Witaj w quizie: {title}')
    score = 0
    question, answers, correct = next_block(human_file)
    while question:
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])
        answer = input("Jaka jest Twoja odpowiedź?")
        if answer == correct:
            print("Brawo, odpowiedź prawidłowa!")
            score +=1
        else:
            print("Odpowiedź błędna")
        print(f'Wynik: {score}pkt')
        question, answers, correct = next_block(human_file)
    human_file.close()
    print(f'To już koniec. Twój wynik: {score}pkt')

main()