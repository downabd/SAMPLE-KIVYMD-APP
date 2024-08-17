from flet import*
import sqlite3 
#########قاعدة البيانات###########

conn = sqlite3.connect("data.db",check_same_thread=False)
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS student 
        (id INTEGER PRIMARY KEY,
stdname TEXT,
stdphone TEXT,
stdaddress TEXT,
squran INTEGER,
sarabic INTEGER,
sbilogy INTEGER,
schimastry INTEGER,
senglish INTEGER,
smathss INTEGER); 
""");
conn.commit( )




def main(page:Page):
   page.title = "abboud"
   page.scroll = 'auto'
   page.window.top = 1
   page.window.left = 960
   page.window.width = 390
   page.window.height = 740
   page.bgcolor = 'white'
   page.theme_mode = ThemeMode.LIGHT
   phh = PermissionHandler()
   page.overlay.append(phh)

   ###########################
   table_name = 'student'
   query = f'SELECT COUNT(*) FROM {table_name}'
   cursor.execute(query)
   result = cursor.fetchone()
   row_count = result[0]


   def add() :
      cursor.execute("""INSERT INTO student( stdname,stdphone,stdaddress,squran,sarabic,sbilogy,schimastry,senglish,smathss ) VALUES(?,?,?,?,?,?,?,?,?)""",( tname.value,tphone.value,taddress.value,dquran.value,darabic.value,dbilogy.value,dchimastry.value,denglish.value,dmathss.value
 ) )
      conn.commit()        


   def show(e):
      page.clean()
      c = conn.cursor()
      c.execute("SELECT * FROM student")
      users = c.fetchall()
      print(users)

   #if not users == "":
      keys = ['id','stdname' ,'stdphone' ,'stdaddress' ,'squran' ,'sarabic' ,'sbilogy' ,'schimastry' ,'senglish' ,'smathss' ]
      result = [dict(zip(keys,values)) for values in users] 
      for x in result:
         ###########marks##########
         m = x['smathss']
         q = x['squran']
         a = x['sarabic']
         p = x['sbilogy']
         c = x['schimastry']
         e = x['senglish']
         res = m + q + a + p + c + e
         resum = (m + q + a + p + c + e)/6

         if res < 50 :
            s = Text('راسب 😒')
         if res > 50 :
            s = Text('ناجح 😊')
            #######################3
         page.add(
             Card(  
               color = '#ccc',
               content=Container(
                  content = Column([
                        ListTile(
                           leading=Icon(icons.PERSON),
                           title=Text('Name: '+x['stdname'])

                        ),
                        ListTile(
                           leading=Icon(icons.PHONE),
                           title=Text('Phone: '+x['stdphone'])

                        ),
                        ListTile(
                           leading=Icon(icons.LOCATION_CITY),
                           title=Text('Address: '+x['stdaddress'])

                        ),
                        Row([
                           Text('درجات الطالب',size=16)
                        ],alignment=MainAxisAlignment.CENTER),
                        Row([
                          Text('الاسلامية: ' +str(x['squran'])),
                          Text('العربي: ' +str(x['sarabic'])),
                          Text('الاحياء: ' +str(x['sbilogy']))
                        ],alignment=MainAxisAlignment.CENTER),
                                                Row([
                          Text('الكيمياء: ' +str(x['schimastry'])),
                          Text('الرياضيات: ' +str(x['smathss'])),
                          Text('الانكليزي: ' +str(x['senglish']))
                        ],alignment=MainAxisAlignment.CENTER),
                        Row([
                          Text('المعدل :  '+str(resum))
                        ],alignment=MainAxisAlignment.CENTER),
                        Row([
                          s
                        ],alignment=MainAxisAlignment.CENTER),


                  ]))),
                        Row([
                        lineblack
                        ],alignment=MainAxisAlignment.CENTER,rtl=True)
                        )
         page.update()


 
   
   def exit_app(e):
      page.window_close()
   def rest_app(e):
      page.update()
 
######## Feilds #######
   tname = TextField(label='اسم الطالب',icon=icons.PERSON, rtl=True,height=38)
   #tmail = TextField(label='البريد الالكتروني',icon=icons.MAIL, rtl=True,height=38)
   tphone = TextField(label='رقم الهاتف',icon=icons.PHONE, rtl=True,height=38)
   taddress = TextField(label='العنوان',icon=icons.LOCATION_CITY, rtl=True,height=38)
#######################

######## Marks #######
   marktext = Text(" درجات الطالب - Marks Student ",color="blue",text_align='center',font_family="All Genders v4",size=18)
   dquran = TextField(label='الاسلامية',width=110,rtl=True,height=38)
   darabic = TextField(label='العربي',width=110,rtl=True,height=38)
   dbilogy = TextField(label='الاحياء',width=110,rtl=True,height=38)
   dchimastry = TextField(label='الكيمياء',width=110,rtl=True,height=38)
   denglish = TextField(label='الانكليزي',width=110,rtl=True,height=38)
   dmathss = TextField(label='رياضيات',width=110,rtl=True,height=38)

######################

   addbuttn = ElevatedButton(
      "اضافة طالب جديد",
      width=170,
      style=ButtonStyle(bgcolor='#ff9900',color='white',padding=15),
      on_click=add
   )
   
   showbuttn = ElevatedButton(
      "عرض كل الطلاب",
      width=170,
      style=ButtonStyle(bgcolor='blue',color='white',padding=15),
      on_click=show
   )
   closebuttn = ElevatedButton(
      "خروج  ",
      width=170,
      style=ButtonStyle(bgcolor='blue',color='white',padding=15),
      on_click=exit_app
   )
   lineblack = ElevatedButton(
      "  ",
      width=170,
      height=1,
      style=ButtonStyle(bgcolor='black',color='white',padding=2),
      on_click=...
   )

   page.add(
      AppBar(
          
          bgcolor="#ff9900",
          title=Text('نظام مدرستي',color="white",font_family="All Genders v4",),
          actions=[
              IconButton(icons.SETTINGS,on_click=...)
          ],color="white"
      ),
      Row([
         #Image(src="home.gif",width=280)
      ],alignment=MainAxisAlignment.CENTER),

      Row([
         Text("تطبيق مدرسي من برمجة عبدالخالق",size=20,color='black',font_family="All Genders v4")
      ],alignment=MainAxisAlignment.CENTER),

      Row([
         Text(" عدد الطلاب المسجلين: ",size=19,color='#ff9900',font_family="All Genders v4"),
         Text(row_count,size=20,color='#ff9900',font_family="Noor",weight="bold")
      ],alignment=MainAxisAlignment.CENTER,rtl=True),

         tname,
         
         tphone,
         taddress,
      
      Row([
         marktext

          ],alignment=MainAxisAlignment.CENTER,rtl=True),

      Row([
         dquran,
         darabic,
         dbilogy

          ],alignment=MainAxisAlignment.CENTER,rtl=True),

      Row([
         dchimastry,
         dmathss,
         denglish

          ],alignment=MainAxisAlignment.CENTER,rtl=True),
      
      Row([
         addbuttn,showbuttn
      ],alignment=MainAxisAlignment.CENTER,rtl=True),
      Row([
         closebuttn
      ],alignment=MainAxisAlignment.CENTER,rtl=True),
      Row([
         Text("abdalkaliq basheer © 2025",size=12,color='black')
      ],alignment=MainAxisAlignment.CENTER),
             Row([
         Text("v: 1.0.1",size=12,color='black')
      ],alignment=MainAxisAlignment.CENTER)
   )
   page.update()

app(main)
