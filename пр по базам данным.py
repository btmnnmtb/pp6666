import sqlite3
import doctor
import mettt
conn = sqlite3.connect ("database.db")

cursor = conn.cursor()
cursor.execute('''
create table if not exists pat
               (
                id integer primary key  , 
               name text not null , 
               passwor integer not null , 
               age integer not null , 
               jaloba text not null ,
               familia_vr text , 
               dol_vr text  )
                ''')
cursor.execute('''
            create table if not exists doctorsss
               (
                id integer primary key , 
               name text not null , 
               familia text not null ,
               otchestvo text not null ,         
               doljnost text not null )
                ''')

cursor.execute("insert into doctorsss (name , familia , otchestvo , doljnost) values ( ? , ? ,? ,? )" , (doctor.doctor1.name , doctor.doctor1.familia , doctor.doctor1.otchestvo , doctor.doctor1.doljnost))
cursor.execute("insert into doctorsss (name , familia , otchestvo , doljnost) values (  ? , ? ,? ,? )" , (doctor.doctor2.name , doctor.doctor2.familia , doctor.doctor2.otchestvo , doctor.doctor2.doljnost))
cursor.execute("insert into doctorsss (name , familia , otchestvo , doljnost) values (  ? , ? ,? ,? )" , (doctor.doctor3.name , doctor.doctor3.familia , doctor.doctor3.otchestvo , doctor.doctor3.doljnost))
cursor.execute("insert into doctorsss (name , familia , otchestvo , doljnost) values ( ? , ? ,? ,? )" , (doctor.doctor4.name , doctor.doctor4.familia , doctor.doctor4.otchestvo , doctor.doctor4.doljnost))
cursor.execute('''create table if not exists meddd
               (
               id integer primary key ,
                name_of_med text not null , 
               proizvodi text not null , 
               colvo integer )
                ''')
cursor.execute("insert into meddd (name_of_med , proizvodi , colvo) values ( ? , ? ,?  )" , (mettt.med1.name_of_medi , mettt.med1.proizvod , mettt.med1.colvo))
cursor.execute("insert into meddd (name_of_med , proizvodi , colvo) values ( ? , ? ,?  )" , (mettt.med2.name_of_medi , mettt.med2.proizvod , mettt.med2.colvo))
cursor.execute("insert into meddd (name_of_med , proizvodi , colvo) values ( ? , ? ,?  )" , (mettt.med3.name_of_medi , mettt.med3.proizvod , mettt.med3.colvo))
cursor.execute("insert into meddd (name_of_med , proizvodi , colvo) values ( ? , ? ,?  )" , (mettt.med4.name_of_medi , mettt.med4.proizvod , mettt.med4.colvo))
cursor.execute('''create table if not exists ret
               (
               name text not null , 
                ret integer )
                ''')
conn.commit()










def md ():
    cursor.execute("select * from meddd")
    med = str(input())
    cursor.execute(f"SELECT name_of_med from meddd WHERE name_of_med = '{med}'")
    if cursor.fetchone() is None:
            print("Вы ввели лекарство неправильно")
            md()
    elif (f"select name_of_med from meddd where name_of_med  = '{med}' and colvo != 0 "):
            print("Вот ваше лекарство")
            cursor.execute(f"update meddd set colvo = colvo - 1 where name_of_med = '{med}'")
            print(cursor.execute("select * from meddd").fetchall())
            conn.commit()
                
    elif cursor.execute(f"select  colvo from meddd where colvo = 0"):
        print("Лекарство закончилось")
                
def reg():
    name = str(input("имя>> "))



    
    passwor = input("пароль>> ")
    age = int(input("возраст --  "))
    jaloba = input("опишите ваше недомагание -- ")
    cursor.execute(f"select * from  patt where name = '{name}' and passwor = '{passwor}' ")
    cursor.execute(f"SELECT  name, passwor , age , jaloba FROM patt WHERE name = '{name}' AND passwor = '{passwor}' and age = '{age}' and jaloba = '{jaloba}'")
    conn.commit()
    
    if cursor.fetchone() is None:
        patient = [name, passwor , age , jaloba]
        
        cursor.execute("INSERT INTO patt (name, passwor , age , jaloba) values (? , ? , ? , ?)", patient)
        
        print('Вы зарегесрировались')
        conn.commit()
        login()
        
        
        
        
    
        
        
    else:
        print('Такая запись уже существует')

           
def login():
    conn = sqlite3.connect ("database.db")
    cursor = conn.cursor()
    
    name = input("Имя> ")
    passwor = input("пароль>> ")
    
    
    

    
    cursor.execute(f"SELECT name, passwor FROM patt WHERE name = '{name}' AND passwor = '{passwor}'")
     
    if not cursor.fetchone():
        print("Нет такой записи")
        print("Начало регистрации")
        conn.commit()

        reg()
    else:
        print('Доюро пожаловать')
        print("Выберите врача, который вам нужен, нажав на 1, 2, 3 ,4")
        print(cursor.execute('select * from doctorsss').fetchall())
        
        
        
        
        b =int(input())
    
        if(b == 1 ):
            
            cursor.execute("update patt set familia_vr = 'Крикун' ")
            cursor.execute("update patt set dol_vr = 'Эндокренолог' ")
            cursor.execute('select * from patt where name = ? and passwor = ?' , (name , passwor))
            row = cursor.fetchall()
            for rr in row:
                print(rr)
            conn.commit()
            print("Вам выписывают пропитал")
        elif( b == 2) :
            cursor.execute("update patt set familia_vr = 'Ковалев' ")
            cursor.execute("update patt set dol_vr = 'Стомотолог' ")
            cursor.execute('select * from patt where name = ? and passwor = ?' , (name , passwor))
            row = cursor.fetchall()
            for rr in row:
                print(rr)
            conn.commit()
            print("Вам выписывают P22")
        
        elif( b == 3) :
            cursor.execute("update patt set familia_vr = 'Иванова' ")
            cursor.execute("update patt set dol_vr = 'Травматолог' ")
            cursor.execute('select * from patt where name = ? and passwor = ?' , (name , passwor))
            row = cursor.fetchall()
            for rr in row:
                print(rr)
            conn.commit()
            print("Вам выписали ибупрофен")
        elif( b == 4) :
            cursor.execute("update patt set familia_vr = 'Петренко' ")
            cursor.execute("update patt set dol_vr = 'Психиатр' ")
            cursor.execute('select * from patt where name = ? and passwor = ?' , (name , passwor))
            row = cursor.fetchall()
            for rr in row:
                print(rr)
            conn.commit()
            print("Вам выписали Звездочку")
    print("Введите название вашего препарата")
    print(cursor.execute("select * from meddd").fetchall())
    md()
    conn.commit()

    print("поставтье оценку от 1 до 5")
    rett = int(input())
    while rett > 5 or rett < 1:
        print("поставть оценку от 1 до 5")
        rett = int(input())
    cursor.execute(f"insert into ret (name, ret) values('{name}' , '{rett}')")
    print(cursor.execute("select * from ret").fetchall())
    
               
login()

      
   
    





