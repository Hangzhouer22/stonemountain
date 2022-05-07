Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
color = input("Enter a color: ")
Enter a color: yellow
pluranoun = input("Enter a plural noun: ")
Enter a plural noun: chaires
celebrity = input("Enter a celebrity: ")
Enter a celebrity: Yutao Yan
print("Paintings are", color)
Paintings are yellow
print(pluralnoun, " are tall")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(pluralnoun, " are tall")
NameError: name 'pluralnoun' is not defined. Did you mean: 'pluranoun'?
NameError: name 'pluralnoun' is not defined. Did you mean: 'pluranoun'?
SyntaxError: invalid syntax
print(pluranoun, " are tall")
chaires  are tall
print(celebrity + " is the best")
Yutao Yan is the best




adj = input("adjective: ")
adjective: challenging
verb1 = input("verb: ")
verb: play

verb2 = input("verb: ")
verb: smiling
famous_person = input("famous person: ")
famous person: Michael Jordan

madlib = f" Basketball is so {adj}! it makes me so excited all the time because I love to {}
SyntaxError: unterminated string literal (detected at line 1)

madlib = f" Basketball is so {adj}! it makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)
 Basketball is so challenging! it makes me so excited all the time because I love to play. Stay hydrated and smiling like you are Michael Jordan!
