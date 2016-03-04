print('Gimme opcodes!')
end = False
mnemonics = ''
while (end == False):
    full = int(input())
    op = full // 100
    mailbox = full % 100
    if (op == 0):
        end = True
        mnemonics += 'HLT'
    elif (op == 1):
        mnemonics += 'ADD ' + str(mailbox).zfill(2) + '\n'
    elif (op == 2):
        mnemonics += 'SUB ' + str(mailbox).zfill(2) + '\n'
    elif (op == 3):
        mnemonics += 'STA ' + str(mailbox).zfill(2) + '\n'
    elif (op == 5):
        mnemonics += 'LDA ' + str(mailbox).zfill(2) + '\n'
    elif (op == 6):
        mnemonics += 'BRA ' + str(mailbox).zfill(2) + '\n'
    elif (op == 7):
        mnemonics += 'BRZ ' + str(mailbox).zfill(2) + '\n'
    elif (op == 8):
        mnemonics += 'BRP ' + str(mailbox).zfill(2) + '\n'
    elif (op == 9):
        if(mailbox == 1):
            mnemonics += 'INP\n'
        else: mnemonics += 'OUT\n'
print(mnemonics)
