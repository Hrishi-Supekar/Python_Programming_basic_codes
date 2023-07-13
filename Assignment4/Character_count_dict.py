# Create character count dict from give string
msg = "WelcometoITPreneunerthisishrishi"
char_dict = {}
for x in msg:
    char_dict.update({x: msg.count(x)})
print(char_dict)
