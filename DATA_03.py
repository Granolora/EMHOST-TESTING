import time
print("Checking for valid passphrase, if program crashes unexpectedly, re-generate passphrase and try again...")
time.sleep(8)
passkeyvalidation = open("passphraseV0.0.3a-01.txt", "r")
passkeyvalidation.close
print("Passphrase validated, welcome, Chara Dreemurr.")
key1 = str(input("What was the answer to PROGRAM_01's puzzle? "))
if key1 == "doorkeys":
    print("Correct, next question.")
    key2 = str(input("Who built the core? "))
    if key2 == "Alphys":
        print("Correct, final question.")
        key3 = str(input("How many human souls would it take to break the barrier? "))
        if key3 == "7" or "Seven":
            print("https:/tinyurl.com/seven-souls")
        else:
            for i in "999999999999999999999999999999999999999999999999999999999999999999999999":
                time.sleep(0.25)
                print("wrong")
    else:
        for i in "999999999999999999999999999999999999999999999999999999999999999999999999":
            time.sleep(0.25)
            print("wrong")
else:
    for i in "999999999999999999999999999999999999999999999999999999999999999999999999":
            time.sleep(0.25)
            print("wrong")
