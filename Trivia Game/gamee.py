# Simple game in python

print('Hi, Welcome to the Minecraft Quiz!')
print('Try to get as many questions correct as possible!')

total_q = 10
score = 0

ans = input('1. When did Minecraft release?')

if ans.lower() == '2009':
    print('Correct!')
    score += 1
else:
    print('Incorrect! Minecraft released in 2009!')

ans = input('2. What is the name of the basic Minecraft skin?')

if ans.lower() == 'steve':
    print('Correct!')
    score += 1
else:
    print('Incorrect! Steve is the basic skin in minecraft versions 1.0 - 1.8 when Alex came out, but Steve is still the basic character.')

ans = input('3. Who created Minecraft?')

if ans.lower() == 'notch':
    print('Correct!')
    score += 1
else:
    print('Incorrect! The game was created by Notch')

ans = input('4. What is the rarest and strongest material in Minecraft?')

if ans.lower() == 'netherite':
    print('Correct!')
    score += 1
else:
    print('Incorrect! Netherite was added in 1.16 and was confirmed to be better than Diamond')

ans = input('5. What happens when you name a animal "Dinnerbone" A = It becomes upside down Or B = Nothing')

if ans.lower() == 'a':
    print('Correct!')
    score += 1
else:
    print('Incorrect! This is a special feature added by one of the developers who goes by the name of Dinnerbone.')

ans = input('6. What happens when you try to sleep in the Nether? A = You explode Or B = You sleep peacfully')

if ans.lower() == 'a':
    print('Correct!')
    score += 1
else:
    print('Incorrect! This is a intented feature in minecraft added by the developers.')

ans = input('7. What is the build limit in Minecraft?')

if ans.lower() == '256':
    print('Correct!')
    score += 1
else:
    print('Incorrect! It is 256 blocks!')

ans = input('8. True Or False - Can you mine bedrock?')

if ans.lower() == 'false':
    print('Correct!')
    score += 1
else:
    print('Incorrect! You can not destroy bedrock at all besides going into creative mode.')

ans = input('9. True Or False - You can go above the Bedrock Ceiling in the Nether')

if ans.lower() == 'true':
    print('Correct!')
    score += 1
else:
    print('Incorrect! You can go above the ceiling by using glitches that any player can do.')

ans = input('10. Who owns Minecraft?')

if ans.lower() == 'microsoft':
    print('Correct!')
    score += 1
else:
    print('Incorrect! Microsoft bought minecraft from Notch in 2014')

print('Thank you for playing, you got ', score, " questions correct!")
mark = (score/total_q) * 100

print("Mark:", str(mark) + '%')

print('Goodbye!')
