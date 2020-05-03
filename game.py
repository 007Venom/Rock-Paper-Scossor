from random import randint
#for for display purpose
print("ROOCK PAPER SCISSOR")
N=int(input("Best of how many games: "))
print("Let the best player win!!!!")
#initailizing values for scores
computer=0
me=0
i=0
#loop for as to how many values it should take
while i < N:
    n=input()
    if n in ['rock','Rock','ROCK','scissor','SCISSOR','Scissor','Paper','paper','PAPER']:
        number=randint(1,300)
        i=i+1
        if number in range(1,100):
            print("Computer chose 'ROCK'")
            if n=='rock' or n=='Rock' or n=='ROCK':
                print("Its a draw.Both get a point!!!")
                computer =computer +1
                me=me+1
            elif n=='scissor' or n=='Scissor' or n=='SCISSOR':
                print("Computer wins!!!")
                computer= computer + 1
            else:
                print("You win!!!")
                me =me+1
        elif number in range(100,200):
            print("Computer chose 'SCISSOR'")
            if n=='rock' or n=='Rock' or n=='ROCK':
                print("You win!!!")
                me=me+1
            elif n=='scissor' or n=='Scissor' or n=='SCISSOR':
                print("Its a draw.Both get a point!!!")
                computer= computer + 1
                me=me+1
            else:
                print("Computer wins!!!")
                computer =computer +1
        else:
            print("Computer chose 'PAPER'")
            if n=='rock' or n=='Rock' or n=='ROCK':
                print("Computer wins!!!")
                computer =computer +1
            elif n=='scissor' or n=='Scissor' or n=='SCISSOR':
                print("You win!!!")
                me=me+1
            elif n=='paper' or n=='Paper' or n=='PAPER':
                print("Its a draw.Both get a point!!!")
                computer =computer +1
                me=me+1
    else:
        print("You have entered an unknown character!!!")

#giving out the scores

print("GAME HAS COME TO AN END ")
print("Computer:%d::You:%d" %(computer,me))
if computer >me:
    print("COMPUTER WINS THE GAME!!!")
elif me>computer:
    print("YOU WON THE GAME!!!")
else:
    print("ITS A DRAW!!!")
   





