import os,random,send2trash

# This script will create n number of question paper with m number of question in each of them.
# Enter the number below which you want to ask question from them 
# Eg 12 will ask multiple question between 1 and 13

paper_no = int(input("Enter the number of question papers you want to create :"))
ques_no = int(input('Enter the number of questions in each question paper :'))
high_no =  int(input("Enter the nnumber below which question will be prepared:"))

num_list = [i for i in range(1,high_no+1)]
path = os.getcwd()

if 'random_quiz_generator' not in os.listdir(path):
    os.makedirs(os.path.join('random_quiz_generator'))
    os.chdir('random_quiz_generator')
else:
    os.chdir('random_quiz_generator')

if not os.path.isdir('Maths_Papers'):
    os.makedirs('Maths_Papers')
    os.chdir('Maths_Papers')
else:
    os.chdir('Maths_Papers')

for i in range(1,paper_no+1):
    f = open(f'Maths_paper_{i}.txt','w')
    f.write('\t\t Maths Exams\n\n'.upper())
    f.writelines(['Name-\n\n','Roll No.-\n\n','Class-\n\n','Section-\n\n'])
    for j in range(1,ques_no+1):
        num_1 = random.choice(num_list)
        num_2 = random.choice(num_list)
        f.write(f'{j}. {num_1}\t X\t {num_2}\t =\t ______\n')
        f.write('   '*20)
        f.write('\n')

    f.write('-'*100)




