from MimeDiversity import ComputeMIME
from util import utility

if __name__ == '__main__':
    mime = ComputeMIME.GetMIMEInformation(utility.constant.DATA_DIR)
    mimeInfo = mime.computeMIME()

    print mimeInfo
