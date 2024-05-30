import time
print("Checking for valid passphrase, if program crashes unexpectedly, re-generate passphrase and try again...")
time.sleep(8)
passkeyvalidation = open("passphraseV0.0.2a-01.txt", "r")
passkeyvalidation.close
print("Passphrase validated, welcome, Chara Dreemurr.")
print("In order to access File02, please answer a final question:")
print("Remember to put your answer in quotes.")
finalanswer = str(input("what are the first 4 notes of His Theme? "))
if finalanswer == "F G E F":
    print("https://tinyurl.com/RECOVERY02FINAL")
    time.sleep(10)