def writeToResultsFile(testName,Date,startTimeStr, correctStr, wrongStr, EndTimeStr):
    file1 = open("Results\Results.txt","a")
    L = [testName + "\n", Date + "\n", startTimeStr + "\n", correctStr + "\n", wrongStr + "\n",EndTimeStr+ "\n", "///////////////////" + "\n"  ] 
    file1.writelines(L) 
    file1.close()


