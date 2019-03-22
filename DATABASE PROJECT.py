import pymysql
import datetime

choice=int(input("enter the choice\n 1.to enter the patient details\n 2.to detele the patient details\n 3.update patient details\n 4.view the patient details\n"))
if choice==1:
           
            n=input("Enter Name of the patient\n")
            ph=input("Enter the phone number of the patient\n")
            em=input("enter the email-id\n")
            il=input("Enter disease of the patient\n")
            wn=input("Enter wardnumber of the patient admitted to\n")
            doc=input("enter the doctor consulted\n")
            a=int(input("Enter the bill's total amount\n"))
            d=int(input("Enter due amount\n"))
            ad=input("enter the date patient got admitted to the hospital in the format 'dd/mm/yy' : \n")
            cond=1
            while cond==1:
                day,month,year = ad.split('/')
                isValidDate = True
                try :
                    datetime.datetime(int(year),int(month),int(day))
                except ValueError :
                    isValidDate = False
                if(isValidDate) :
                    print ("Input date is valid ..")
                    break
                else :
                    print ("Input date is not valid..")
                    ad=input("enter valid input : \n")
                    break
            dat=input("enter the date patient got discharged from hospital in the format dd/mm/yy\n")
            condi=1
            while condi==1:
                day,month,year = dat.split('/')
                isValidDate = True
                try :
                    datetime.datetime(int(year),int(month),int(day))
                except ValueError :
                    isValidDate = False
                if(isValidDate) :
                    print ("Input date is valid ..")
                    break
                else :
                    print ("Input date is not valid..")
                    ad=input("enter valid input : \n")
                    break
            conn=pymysql.connect(host='localhost',user='root',password='',database='kavya')

            cur=conn.cursor()

            query="insert into patient_details(name,phone_number,email_id,disorder,ward_num,doctor_consulted,amt,due,admitted_date,discharged_date) values('%s','%s','%s','%s','%s','%s',%d,%d,'%s','%s')"%(n,ph,em,il,wn,doc,a,d,ad,dat)

            cur.execute(query)

            row=cur.rowcount

            if row>0:
                print("record inserted")
            else:
                print("record not inserted")

            conn.commit()

            conn.close()
elif choice==2:
            ref=input("Enter id or name or doctor consulted \n")
         
            conn=pymysql.connect(host='localhost',user='root',password='',database='kavya')

            cur=conn.cursor()

            query="delete from patient_details where id='%s' or name='%s' or doctor_consulted='%s'"%(ref,ref,ref)

            cur.execute(query)

            row=cur.rowcount

            if row>0:
                print("record Deleted")
            else:
                print("record not Deleted")

            conn.commit()

            conn.close()

elif choice==3:
    ref=input("ENter id or name\n")
    ln=int(input("ENter paid amount\n"))
    nb=int(input("ENter balance amount\n"))

    conn=pymysql.connect(host='localhost',user='root',password='',database='kavya')

    cur=conn.cursor()

    query="update patient_details set amt=%d,due=%d where id='%s' or name='%s'"%(ln,nb,ref,ref)

    cur.execute(query)

    row=cur.rowcount

    if row>0:
        print("record Updated")
    else:
        print("record not Updated")

    conn.commit()

    conn.close()
    
elif choice==4:
    conn=pymysql.connect(host='localhost',user='root',password='',database='kavya')

    cur=conn.cursor()
    c=int(input("Enter your choice on what basis the details should be displayed\n 1.id\n 2.name\n 3.doctor\n 4.admitted date or discharged date \n 5.balance amount\n 6.all details\n"))
    if c==1:
                ref=int(input("enter the id\n"))
                query="select * from patient_details where id=%d"%(ref)

                cur.execute(query)

                row=cur.rowcount


                for x in cur.fetchall():
                   for y in x:
                        print(y,end="\t")

                   print()

                if row==0:
                    print("No record exists")
                conn.commit()
                conn.close()
    elif c==2:
                ref=input("enter the name\n")
                query="select * from patient_details where name='%s'"%(ref)

                cur.execute(query)

                row=cur.rowcount


                for x in cur.fetchall():
                   for y in x:
                        print(y,end="\t")

                   print()

                if row==0:
                    print("No record exists")
                conn.commit()

                conn.close()
    elif c==3:
                ref=input("enter the consulted docter name \n")
                
                query="select * from patient_details where doctor_consulted='%s'"%(ref)

                cur.execute(query)

                row=cur.rowcount


                for x in cur.fetchall():
                   for y in x:
                        print(y,end="\t")

                   print()

                if row==0:
                    print("No record exists")
                conn.commit()
                conn.close()
    elif c==4:
                ref=input("enter the admitted date or discharged date in the format dd/mm/yy: \n")
                
                query="select * from patient_details where admitted_date='%s' or discharged_date='%s'"%(ref,ref)

                cur.execute(query)

                row=cur.rowcount


                for x in cur.fetchall():
                   for y in x:
                        print(y,end="\t")

                   print()

                if row==0:
                    print("No record exists")
                conn.commit()
                conn.close()
    elif c==5:
                ref=int(input("enter the balance amount: \n"))
                query="select * from patient_details where due=%d "%(ref)

                cur.execute(query)

                row=cur.rowcount


                for x in cur.fetchall():
                   for y in x:
                        print(y,end="\t")

                   print()

                if row==0:
                    print("No record exists")
                conn.commit()
                conn.close()
                
        
                
    elif c==6:
                

                query="select * from patient_details"

                cur.execute(query)

                row=cur.rowcount
                for x in cur.fetchall():       
                
                    for y in x:
                        
                        print(y,end="\t")

                    print()

                if row==0:
                    
                    
                    print("No record exists")


                conn.commit()

                conn.close()
    else:
                 print("wrong choice")
     
else:
           print("wrong choice")
           
           

           


            



        
