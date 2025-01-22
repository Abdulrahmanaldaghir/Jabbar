import os

def saveqa(q,a):
  f = open("Q&A.txt", "a")
  f.write("Q: "+ q + "\n")
  f.write("A: "+ a + "\n")
  f.close()

def saveimg(q,arr):
  f = open("Q&A.txt", "a")
  f.write("Imagination Subject: "+ q + "\n")
  for a in arr:
    f.write("url: "+ a["url"] + "\n")
  f.close()
def savestory(q,a,url):
  f = open("Q&A.txt", "a")
  f.write("Story Subject: "+ q + "\n")
  f.write("url: "+ url + "\n")
  f.write("Story: "+ a + "\n")

  f.close()
def savejoke(q,a):
  f = open("Q&A.txt", "a")
  f.write("Joke Subject: "+ q + "\n")
  f.write("Joke: "+ a + "\n")
  f.close()
#saveqa("TEST","answer")