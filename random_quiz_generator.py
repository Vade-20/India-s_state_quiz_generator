import random,os,shutil

state = {'Andhra Pradesh': 'Amaravati',
 'Arunachal Pradesh': 'Itanagar',
 'Assam': 'Dispur',
 'Bihar': 'Patna',
 'Chhattisgarh': 'Raipur',
 'Goa': 'Panaji',
 'Gujarat': 'Gandhinagar',
 'Haryana': 'Chandigarh',
 'Himachal Pradesh': 'Shimla',
 'Jharkhand': 'Ranchi',
 'Karnataka': 'Bangalore',
 'Kerala': 'Thiruvananthapuram',
 'Madhya Pradesh': 'Bhopal',
 'Maharashtra': 'Mumbai',
 'Manipur': 'Imphal',
 'Meghalaya': 'Shillong',
 'Mizoram': 'Aizawl',
 'Nagaland': 'Kohima',
 'Odisha': 'Bhubaneshwar',
 'Punjab': 'Chandigarh',
 'Rajasthan': 'Jaipur',
 'Sikkim': 'Gangtok',
 'Tamil Nadu': 'Chennai',
 'Telangana': 'Hyderabad',
 'Tripura': 'Agartala',
 'Uttar Pradesh': 'Lucknow',
 'Uttarakhand': 'Dehradun',
 'West Bengal': 'Kolkata'}


total_number = int(input("Enter total number of question paper you want to create-"))
multiple = [i for i in state.values()]
keys = [i for i in state.keys() if i is not None]
option = ['A','B','C','D']
path = os.getcwd()
if 'question_paper'  in os.listdir(os.path.abspath("random_quiz_generator")):
    shutil.rmtree(os.path.join("random_quiz_generator\\question_paper"))
    os.makedirs(os.path.join('random_quiz_generator\\question_paper'))
else:
    os.makedirs(os.path.join('random_quiz_generator\\question_paper'))

if 'answer_sheet'  in os.listdir(os.path.abspath("random_quiz_generator")):
    shutil.rmtree(os.path.join("random_quiz_generator\\answer_sheet"))
    os.makedirs(os.path.join("random_quiz_generator\\answer_sheet"))
else:
    os.makedirs(os.path.join("random_quiz_generator\\answer_sheet"))

for i in range(1,total_number+1):
    ques_path = path+'\\random_quiz_generator\\question_paper'
    os.chdir(os.path.join(ques_path))
    f = open(f'Question paper - {i}.txt','w')
    ans_path = path+'\\random_quiz_generator\\answer_sheet'
    os.chdir(os.path.join(ans_path))
    g = open(f'Answer paper-{i}.txt','w')
    f.write('\t\t Question on India States and capital\n\n'.upper())
    f.writelines(['Name-\n','Roll No.-\n','Class-\n','Section-\n\n'])
    random.shuffle(keys)
    for j,k in enumerate(keys,start=1):
        f.write(f'{j}.The capital of {k} is __________________\n')
        mul = [state.get(k)]
        for _ in range(3):
            rom = random.choice(multiple)
            while rom in mul:
                rom = random.choice(multiple)
            mul.append(rom)
        random.shuffle(mul)
        for l in range(4):
            if mul[l] == state.get(k):
                ans = option[l]
        f.write(f'\tA.{mul[0]}\tB.{mul[1]}\tC.{mul[2]}\tD.{mul[3]}\n\n')
        g.write(f'{j}. {ans}\n')
    f.write('-'*100)
    f.close()
    g.close()

    

        



        
        


