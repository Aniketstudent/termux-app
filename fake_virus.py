import os
import time
import webbrowser

def fake_virus():
    for i in range(5):
        webbrowser.open("https://www.google.com")
        time.sleep(1)
    os.system("shutdown -s -t 60")

def main():
    print("Your system is infected!")
    time.sleep(2)
    print("Just kidding! This is a fake virus.")
    time.sleep(2)
    fake_virus()

if __name__ == "__main__":
    main()
  
