import subprocess
def showgroup():
    mccli = "mccli group show --mcsprofile=ix20"
    #p = subprocess.check_output(mccli,shell=True)
    x = subprocess.call(mccli,shell=True)
    print(x)

showgroup()
