#Let everyone enjoy the fun of fucking. --Chi_Tang
import requests, json, os
print('Let everyone enjoy the fun of fucking.')
try:
    print('Checking Internet...')
    js=requests.get('https://ssmzhn.github.io/FuckComputer.json')
    print('Checking git...')
    if os.system('git --version')!=0:
        print('Git is not found!')
        sys.exit(255)
except requests.exceptions.ConnectionError:
    print('Great connection!')
    sys.exit(255)

ls=json.loads(js.text)
print('Welcome to FuckComputer {} in 1 (Python ver)!'.format(len(ls.keys())))
for x in range(len(ls.keys())):
    print('    ({}){}'.format(x+1,list(ls.keys())[x]))
ch=int(input('Please choose a mode: '))
choice=list(ls.keys())[ch-1]
os.system('git clone https://github.com/FuckComputer/{}'.format(choice))
if ls[choice]=='cpp':
    if os.system('g++ --version')!=0:
        print('G++ is not found!')
        sys.exit(255)
    os.system('g++ {}/src/main.cpp'.format(choice))
    os.system('./a.out')
elif ls[choice]=='nim':
    if os.system('nim --version')!=0:
        print('Nim is not found!')
        sys.exit(255)
    os.system('nim compile -d:release {}/src/main.nim'.format(choice))
    os.system('{}/src/main'.format(choice))
elif ls[choice]=='python':
    os.system('python {}/src/main.py'.format(choice))
