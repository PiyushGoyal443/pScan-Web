from modules import *

def rendertxt(fname):
    """
    function to read the output text file by praat and return it as a numpy array
    """

    data = ["" for i in range(27)]
    dbData = defaultdict(float)

    # for bias
    data[0] = 1
    dbData["Bias"] = 1

    with open(fname) as f:
        f.readline()
        f.readline()

        # for Pitch features
        for i in range(15, 20):
            tmp = f.readline()
            tmp = tmp.strip(" ").split(":")
            tmp[1] = tmp[1].replace(" ","").replace("Hz","")
            data[i] = float(tmp[1])
            dbData[tmp[0]] = float(tmp[1])

        # for Pulses features
        f.readline()
        for i in range(20, 24):
            tmp = f.readline()
            tmp = tmp.strip(" ").split(":")
            tmp[1] = tmp[1].replace(" ","").replace("seconds","")
            data[i] = float(tmp[1])
            dbData[tmp[0]] = float(tmp[1])

        # for Voicing features
        f.readline()
        for i in range(24, 27):
            tmp = f.readline()
	    print tmp
            tmp = tmp.strip(" ").split(":")
	    print tmp
	    print tmp[1]
	    try:
                data[i] = float(tmp[1].split("%")[0])
		dbData[tmp[0]] = float(tmp[1].split("%")[0])
	    except ValueError:
		data[i] = float(tmp[1].strip(" ").split(" ")[0])
                dbData[tmp[0]] = float(tmp[1].strip(" ").split(" ")[0])

        # for Jitter features
        f.readline()
        for i in range(1, 6):
            tmp = f.readline()
            tmp = tmp.strip(" ").split(":")
            tmp[1] = tmp[1].replace(" ","").replace("seconds","").replace("%", "")
            data[i] = float(tmp[1])
            dbData[tmp[0]] = float(tmp[1])

        # for Shimmer features
        f.readline()
        for i in range(6, 12):
            tmp = f.readline()
            tmp = tmp.strip(" ").split(":")
            tmp[1] = tmp[1].replace(" ","").replace("dB","").replace("%", "")
            data[i] = float(tmp[1])
            dbData[tmp[0]] = float(tmp[1])

        # for Harmonicity of the voiced parts features
        f.readline()
        tmp = f.readline()
        tmp = tmp.strip(" ").split(":")
        tmp[1] = tmp[1].replace(" ","").replace("dB","").replace("%", "")
        data[12] = float(tmp[1])
        dbData["AC"] = float(tmp[1])

        tmp = f.readline()
        tmp = tmp.strip(" ").split(":")
        tmp[1] = tmp[1].replace(" ","").replace("dB","").replace("%", "")
        data[13] = float(tmp[1])
        dbData["NTH"] = float(tmp[1])

        tmp = f.readline()
        tmp = tmp.strip(" ").split(":")
        tmp[1] = tmp[1].replace(" ","").replace("dB","").replace("%", "")
        data[14] = float(tmp[1])
        dbData["HTN"] = float(tmp[1])

    db.train.insert(dbData)

    # remove the text file
    os.system("rm " + fname)
    return data

def getAttributes(fname):

    """
    function to extract the features from audio file
    """

    txtName = "/home/piyush/code2create/uploads/" + fname.split(".")[0] + ".txt"
    from pydub import AudioSegment
    AudioSegment.from_file("/home/piyush/code2create/uploads/" + fname).export("/home/piyush/code2create/uploads/" + fname[:-3]+"mp3", format="mp3")
    os.system("praat --run /home/piyush/code2create/Voice \"" + fname[:-4] +"\" > " + txtName)

    return rendertxt(txtName)

def mongoTolist(cls = True):

    """
    function to parse dictionary to list and return it
    """

    data = db.train.find({})

    retData = []
    if cls:
        for d in data:
            try:
                retData.append([
                    d["Bias"], d["Jitter (local)"], d["Jitter (local, absolute)"],
                    d["Jitter (rap)"], d["Jitter (ppq5)"], d["Jitter (ddp)"],
                    d["Shimmer (local)"], d["Shimmer (local, dB)"], d["Shimmer (apq3)"],
                    d["Shimmer (apq5)"], d["Shimmer (apq11)"], d["Shimmer (dda)"], d["AC"],
                    d["NTH"], d["HTN"], d["Median pitch"], d["Mean pitch"], d["Standard deviation"],
                    d["Minimum pitch"], d["Maximum pitch"], d["Number of pulses"], d["Number of periods"],
                    d["Mean period"], d["Standard deviation of period"], d["Fraction of locally unvoiced frames"],
                    d["Number of voice breaks"], d["Degree of voice breaks"], d["UPDRS"], d["Class"]
                    ])
            except KeyError:
                pass
    else:
        for d in data:
            try:
                retData.append([
                    d["Bias"], d["Jitter (local)"], d["Jitter (local, absolute)"],
                    d["Jitter (rap)"], d["Jitter (ppq5)"], d["Jitter (ddp)"],
                    d["Shimmer (local)"], d["Shimmer (local, dB)"], d["Shimmer (apq3)"],
                    d["Shimmer (apq5)"], d["Shimmer (apq11)"], d["Shimmer (dda)"], d["AC"],
                    d["NTH"], d["HTN"], d["Median pitch"], d["Mean pitch"], d["Standard deviation"],
                    d["Minimum pitch"], d["Maximum pitch"], d["Number of pulses"], d["Number of periods"],
                    d["Mean period"], d["Standard deviation of period"], d["Fraction of locally unvoiced frames"],
                    d["Number of voice breaks"], d["Degree of voice breaks"], d["UPDRS"]
                    ])
            except KeyError:
                pass

    return np.array(retData)

def updateTheta():

    """
    function to read theta1.txt and theta2.txt file and update in database
    """
    t1 = []
    t2 = []

    with open("theta1.txt") as f:
        for i in range(28):
            temp =  f.readline().strip("\n").strip(" ").split(" ")
            t1.append(map(float, temp))

    with open("theta2.txt") as f:
        for i in range(12):
            temp =  f.readline().strip("\n").strip(" ").split(" ")
            t2.append(map(float, temp))

    db.theta.remove({})
    db.theta.insert({"theta1" : t1})
    db.theta.insert({"theta2" : t2})
