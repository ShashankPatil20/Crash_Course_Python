def first_and_last(message):
    if not message or message[0] == message[-1]:
        return True
    else:
        return False

print(first_and_last("EaglE"))
print(first_and_last(""))
print(first_and_last("sfssw"))


msg = "A kong string with silly typo"
new_msg = msg[0:2] + "l" + msg[3:]
print("Old Msg: " +msg)
print("Correct Msg: " +new_msg)


word = "supercalifragilisticexpialidocious"
print(word.index("x"))


