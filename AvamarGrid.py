import subprocess
def showgroup():
    mccli = "mccli group show --mcsprofile=ix20"
    p = subprocess.check_output(mccli,shell=True)
    print p

showgroup()
