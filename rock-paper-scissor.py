import random
def play():
    user = input("whats ur choice ? 'r' for rock, 'p' for paper, 's' for scissor ")
    computer= random.choice([ 'r','p', 's'])
    
    if user==computer:
        print("its a tie")
        
    if is_win(user,computer):
        return "you've won"
    
    return "you've lost"    
        
        
def is_win(player, opponent):
    #return true if player wins
    # r>s,p>r,s>p
    if (player == 'r'and opponent =='s')or (player =='p' and opponent=='r') or (player =='s' and opponent=='p'):
        return True
print(play())