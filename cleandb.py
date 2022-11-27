import pandas

df = pandas.read_csv('master.csv')

df.replace("(152) COMPUTER SCIENCE AND ENGINEERING (ARTIFICIAL INTELLIGENCE)", "AI", inplace=True)
df.replace("(153) COMPUTER SCIENCE AND ENGINEERING(ARTIFICIAL INTELLIGENCE & MACHINE LEARNING)", "AIML", inplace=True)
df.replace("(154) COMPUTER SCIENCE AND ENGINEERING(DATA SCIENCE)", "DS", inplace=True)
df.replace("(155) COMPUTER SCIENCE AND ENGINEERING(INTERNET OF THINGS)", "IOT", inplace=True)
df.replace("(11) COMPUTER SCIENCE AND INFORMATION TECHNOLOGY", "CSIT", inplace=True)


print(df.head())

df.to_csv('master1.csv', index=False)