import time
import pyodbc
from ast import literal_eval
from threading import Thread
from datetime import datetime
import numpy
import sys



class GetTestTime():
    def __init__(self, *args):
        print('Get_TestTime')
        self.Connect_Server()
        if len(sys.argv) == 5:            
            self.get_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print('-?')

        
    def Send_DB_FinishPR(self, NList):
        self.OrdinalNumber = ''
        self.PR_ID = NList[4]
        self.PRCreater = NList[5]
        self.CreatedDate = NList[6][1]
        self.ProcessStatus = NList[7]
        self.Processer = NList[8]
        self.Last_Transaction = NList[9][1]
        self.Amount = NList[10]

        #cmd = "EXEC usp_Pendingprlist_Insert @PrId=" + self.PR_ID + ",@PRCreater=" + self.PRCreater + ",@CreatedDate=" + self.CreatedDate + ",@ProcessStatus=" + self.ProcessStatus + ",@Processer=" + self.Processer + ",@LastTransaction=" + self.Last_Transaction + ",@Amount=" + self.Amount
        #cmd = 'INSERT INTO PENDINGPRLIST(PR_ID, PRCreater, CreatedDate, ProcessStatus, Processer, Last_Transaction, Amount, WorkingDate)' \
        #      'VALUES('', '', '', '', '', '', '', '')'
        values = "'" + self.PR_ID + "', N'" + self.PRCreater + "', '" + self.CreatedDate + "', N'" + self.ProcessStatus + "', N'" + self.Processer +\
                 "', '" + self.Last_Transaction + "', '" + self.Amount + "', '" + (datetime.now().__format__('%d-%B-%Y %H:%M:%S'))+"'"
        #values = "@PrId='" + self.PR_ID + "', @PRCreater=N'" + self.PRCreater + "', @CreatedDate='" + self.CreatedDate + "', @ProcessStatus=N'" + self.ProcessStatus + "', @Processer=N'" + self.Processer + "', @LastTransaction='" + self.Last_Transaction + "', @Amount='" + self.Amount + "'"
        cmd = "INSERT INTO FINISHPRLIST(PR_ID, PRCreater, CreatedDate, ProcessStatus, Processer, Last_Transaction, Amount, WorkingDate) VALUES(" + values + ")"
        #cmd = "EXEC usp_Pendingprlist_Insert " + values
        print(cmd)
        self.get_data()
        self.cursor.execute(cmd)
        self.cursor.commit()
        print('=======================')
        self.get_data()

    def get_data(self, model='', route='', dateStart='', dateEnd=''):
        try:
            #cmd="exec Proc_TotalTime_by_Model_and_Day @ModelName='CGM4331COM', @Route='OBA_FUNCTION', @DateTime_Start='2022-01-18', @DateTime_End='2022-01-19'"
            cmd="exec Proc_TotalTime_by_Model_and_Day @ModelName='"+str(model)+"', @Route='"+str(route)+"', @DateTime_Start='"+str(dateStart)+"', @DateTime_End='"+str(dateEnd)+"'"
            self.totaltimeList = []
            self.cursor.execute(cmd)
            # print(self.maillist)
            # print(self.maillist[1])
            print('---------------DATA--------')
            for row in self.cursor:
                #self.maillist.extend((row))
                self.totaltimeList.append((row[8]))
                #print(row[8])
                # print(row[0].split(','))
            print(self.totaltimeList)
            print('==========Count=============')
            print(len(self.totaltimeList))
            print('==========AVERAGE=============')
            print(numpy.average(numpy.array(self.totaltimeList)))
        except Exception as e:
            print(e)

    def Connect_Server(self):
        try:
            print('Connect_Server')
            server = '10.228.110.91'
            database = 'QE'
            username = 'sa'
            password = 'Foxconn168!@#'
            self.cnxn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ',1432;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            self.cursor = self.cnxn.cursor()
            print('Connect_Server OK')
            time.sleep(10)
            #print(self.cnxn)
        except Exception as e:
            print(e)

    def GetContent(self, buf, strstart, strend):
        # strresult="none"
        posstart = buf.find(strstart) + len(strstart)
        buf1 = buf[posstart: len(buf)]
        posend = buf1.find(strend)
        if strend == '':
            posend = len(buf1)
        strresult = buf1[0: posend]
        return strresult


GetTestTime()
