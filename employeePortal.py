from flet import *
import flet as ft
import sqlite3

def main(page:ft.Page):
    page.title="EMPLOYEE PORTAL"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.padding=350
    page.theme_mode="light"
    #page.add(body)
    page.update()

    def Login(e):
        userName.error_text=""
        password.error_text=""
        if not userName.value:
            userName.error_text="Missing Employee Name"
            page.update()
        elif not password.value:
            password.error_text="Missing Employee Password"
            page.update()
        else:
            conn = sqlite3.connect('Dodhia.db')
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM employeeTable WHERE employeeId=? AND employeeName=?",(userName.value,password.value))
            user=cursor.fetchone()
            conn.commit()
            conn.close()
            if user is not None:
                page.go("/employeeDashboard")
                print("LoginSuccesfull")
            else:
                password.error_text="Invalid Inputs. Try Again"
                page.update()
                print("Loggin Failed")

  
    userName=ft.TextField(hint_text="Enter Employee Id",color='black',border="underline",width=300)
    password=ft.TextField(hint_text="Enter Employee Name",color='black',border="underline",width=300)
    loginn=ft.ElevatedButton("Login",on_click=Login)

   
    logInnPage=Container(
        Container(
            Stack([
                Container(
                    border_radius=11,
                    rotate=Rotate(0.98*3.14),#degree
                    width=360,
                    height=560,
                    bgcolor="#22ffffff"
                    ),
                Container(
                    Container(
                        Column([
                            Container(
                                padding=padding.only(110,20),
                                ),
                            Text(
                                "login ",
                                width=360,
                                size=30,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    #CLASS
                                    Column([
                                   userName,
                                   password,
                                   loginn
                                   ]),padding=padding.only(20,100),
                                
                                    
                                    ),
                                width=355,
                                height=490,
                                bgcolor='white',
                                border_radius=8
                                ),
                            ])
                        ),
                    width=360,
                    height=760,
                    bgcolor="#22ffffff",
                    border_radius=11,
                    )
                ]),
            padding=50,
            width=360,
            height=580
            ),
        width=780,
        height=1060,
        #gradient=LinearGradient(['red','white'])
        )
    #ROUTING FUNCTIONS FROM DAHSBOARD
    def scheduleFunc(e):
        page.go("/schedulePage")
    def shiftFunc(e):
        page.go("/shiftPage")
    def taskFunc(e):
        page.go("/taskPage")
    def requestFunc(e):
        page.go("/requestPage")
    def Logout(e):
        page.go("/")
    schedule=ft.TextButton("Schedule",on_click=scheduleFunc)
    shift=ft.TextButton("Shift",on_click=shiftFunc)
    Task=ft.TextButton("Task",on_click=taskFunc)
    Request=ft.TextButton("Request",on_click=requestFunc)
    Logout=ft.TextButton("Logout",on_click=Logout)
    dashboardpage=Container(
        Container(
            Stack([
                Container(
                    border_radius=11,
                    rotate=Rotate(0.98*3.14),#degree
                    width=360,
                    height=560,
                    bgcolor="#22ffffff"
                    ),
                Container(
                    Container(
                        Column([
                            Container(
                                padding=padding.only(110,20),
                                ),
                            Text(
                                "Employee Dashboard ",
                                width=360,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        schedule,
                                        shift,
                                        Task,
                                        Request,
                                        Logout
                                   
                                   ]),padding=padding.only(50,100),
                                
                                    
                                    ),
                                width=355,
                                height=490,
                                bgcolor='white',
                                border_radius=8
                                ),
                            ])
                        ),
                    width=360,
                    height=760,
                    bgcolor="#22ffffff",
                    border_radius=11,
                    )
                ]),
            padding=50,
            width=360,
            height=580
            ),
        width=780,
        height=1060,
        #gradient=LinearGradient(['red','white'])
        )
    #SCHEDULE
    class schedule_(ft.UserControl):
        def build(self):
            self.scheduleId=""
            self.taskId =""
            self.shiftId =""
            self.data =""
            self.managerId =""
            self.employeeId =""

            schedule_text=ft.Text(self.scheduleId,size=15)
            taskId_text=ft.Text(self.taskId,size=15)
            shiftId_tetx=ft.Text(self.shiftId,size=15)
            data_tetx=ft.Text(self.data,size=15)
            managerId_tetx=ft.Text(self.managerId,size=15)
            employeeId_tetx=ft.Text(self.employeeId,size=15)

            def Check_schedule(e):
                query=userName.value
                conn=sqlite3.connect('Dodhia.db')
                cursor=conn.cursor()
                cursor.execute("SELECT scheduleId,taskId,shiftId,data,managerId,employeeId FROM scheduleTable WHERE employeeId=?",(query,))
                data=cursor.fetchone()
                conn.commit()
                print(query)
                print(data)
                if data:
                    print("DATA FOUND")
                    scheduleId_value,taskId_value,shiftId_value,data_value,managerId_value,employeeId_value=data

                    self.scheduleId=scheduleId_value
                    self.taskId =taskId_value
                    self.shiftId =shiftId_value
                    self.data =data_value
                    self.managerId =managerId_value
                    self.employeeId =employeeId_value
                    
                    schedule_text.value=self.scheduleId
                    taskId_text.value=self.taskId
                    shiftId_tetx.value=self.shiftId
                    data_tetx.value=self.data
                    managerId_tetx.value=self.managerId
                    employeeId_tetx.value=self.employeeId
                    self.update()
                   
                    
                else:
                    print("Data not found")




            return Column([
                Row([
                    Text("Schedule Id:"),
                    schedule_text
                    ]),
                Row([
                    Text("Task Id:"),
                    taskId_text
                    ]),
                Row([
                    Text("Shift Id:"),
                    shiftId_tetx
                    ]),
                Row([
                    Text("Date:"),
                    data_tetx
                    ]),
                Row([
                    Text("Manager Id:"),
                    managerId_tetx
                    ]),
                Row([
                    Text("Employee Id:"),
                    managerId_tetx
                    ]),
                Row([
                    ElevatedButton("Check Schedule",on_click=Check_schedule),
                    ElevatedButton("Go Back",on_click=lambda _:page.go("/employeeDashboard"))

                    ])

                ])
            
    schedulePage=Container(
        Container(
            Stack([
                Container(
                    border_radius=11,
                    rotate=Rotate(0.98*3.14),#degree
                    width=460,
                    height=560,
                    bgcolor="#22ffffff"
                    ),
                Container(
                    Container(
                        Column([
                            Container(
                                padding=padding.only(110,20),
                                ),
                            Text(
                                "SchedulePortal ",
                                width=460,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        schedule_(),
                                        Row([
                                             
                                             ])
                                   
                                   ]),padding=padding.only(20,100),
                                
                                    
                                    ),
                                width=455,
                                height=590,
                                bgcolor='white',
                                border_radius=8
                                ),
                            ])
                        ),
                    width=460,
                    height=860,
                    bgcolor="#22ffffff",
                    border_radius=11,
                    )
                ]),
            padding=50,
            width=360,
            height=780
            ),
        width=880,
        height=1160,
        #gradient=LinearGradient(['red','white'])
        )
    #SHIFT
    shiftId=ft.TextField(hint_text="Enter Your Shift Id",color='black',border="underline",width=300)
    class shiftCalss(ft.UserControl):
        def build(self):
            self.shiftId=""
            self.taskId=""
            self.scheduleDate =""
            self.startTime =""
            self.endTime =""
            self.shiftManagerId =""
            self.taskManagerId =""

            shiftId_tetx=ft.Text(self.shiftId,size=15)
            taskId_tetx=ft.Text(self.taskId,size=15)
            scheduleDate_tetx=ft.Text(self.scheduleDate,size=15)
            startTime_tetx=ft.Text(self.startTime,size=15)
            endTime_tetx=ft.Text(self.endTime,size=15)
            shiftManagerId_text=ft.Text(self.shiftManagerId,size=15)
            taskManagerId_text=ft.Text(self.taskManagerId,size=15)

            def shift_(e):
                query__=shiftId.value
                print("_____")
                conn=sqlite3.connect('Dodhia.db')
                cursor=conn.cursor()
                cursor.execute("SELECT shiftId,taskId,scheduleDate,startTime,endTime,shiftManagerId,taskManagerId FROM shiftTable WHERE shiftId=?",(query__,))
                data=cursor.fetchone()
                conn.commit()
                conn.close()
                print(query__)
                print(data)
                if data:
                    shiftId_value,taskId_value,scheduleDate_value,startTime_value,endTime_value,shiftManagerId_value,taskManagerId_value=data
                    self.shiftId=shiftId_value
                    self.taskId=taskId_value
                    self.scheduleDate =scheduleDate_value
                    self.startTime =startTime_value
                    self.endTime =endTime_value
                    self.shiftManagerId =shiftManagerId_value
                    self.taskManagerId =taskManagerId_value

                    shiftId_tetx.value=self.shiftId
                    taskId_tetx.value=self.taskId
                    scheduleDate_tetx.value=self.scheduleDate
                    startTime_tetx.value=self.startTime
                    endTime_tetx.value=self.endTime
                    shiftManagerId_text.value=self.shiftManagerId
                    taskManagerId_text.value=self.taskManagerId
                    self.update()
                    
                    
                    
                    
                else:
                    print("SHIFT DATA NOT AVAILABLE")


            return Column([
                Row([
                    Text("Shift Id:"),
                    shiftId_tetx
                    
                    ]),
                Row([
                    Text("Task Id:"),
                    taskId_tetx
                    
                    ]),
                Row([
                    Text("Schedule Date:"),
                    scheduleDate_tetx
                    
                    ]),
                Row([
                    Text("Start  Time:"),
                    startTime_tetx
                    
                    ]),
                Row([
                    Text("End Time:"),
                    endTime_tetx
                    
                    ]),
                Row([
                    Text("Shift Manager Id:"),
                    shiftManagerId_text
                    
                    ]),
                Row([
                    Text("Task Manager Id:"),
                    taskManagerId_text
                    
                    ]),
                Row([
                    ElevatedButton("My Shift Details",on_click=shift_),
                    ElevatedButton("Go Back",on_click=lambda _:page.go("/employeeDashboard"))
                    
                    ])

                ])
            
            
    shiftPage=Container(
        Container(
            Stack([
                Container(
                    border_radius=11,
                    rotate=Rotate(0.98*3.14),#degree
                    width=460,
                    height=560,
                    bgcolor="#22ffffff"
                    ),
                Container(
                    Container(
                        Column([
                            Container(
                                padding=padding.only(110,20),
                                ),
                            Text(
                                "Shift Portal ",
                                width=460,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        shiftId,
                                        shiftCalss(),
                                        Row([
                                             
                                             ])
                                   
                                   ]),padding=padding.only(20,100),
                                
                                    
                                    ),
                                width=455,
                                height=590,
                                bgcolor='white',
                                border_radius=8
                                ),
                            ])
                        ),
                    width=460,
                    height=860,
                    bgcolor="#22ffffff",
                    border_radius=11,
                    )
                ]),
            padding=50,
            width=360,
            height=780
            ),
        width=880,
        height=1160,
        #gradient=LinearGradient(['red','white'])
        )

    class taskClass(ft.UserControl):
        def build(self):
            self.taskTitle=""
            self.taskId =""
            self.taskemployeeId =""
            self.taskManagerId =""
            self.shiftId=""

            taskTitle_tetx=Text(self.taskTitle,size=15)
            taskId_text_=Text(self.taskId,size=15)
            taskemployeeId_text=Text(self.taskemployeeId,size=15)
            taskManagerId_text=Text(self.taskManagerId,size=15)           
            shiftId_text=Text(self.shiftId,size=15)
            def CheckTask(e):
                __query='111'#userName.value
                print(__query)
                conn=sqlite3.connect('Dodhia.db')
                cursor=conn.cursor()
                cursor.execute("SELECT taskTitle,taskId,taskemployeeId,taskManagerId,shiftId  FROM assignTaskTable WHERE taskemployeeId=?",(__query,))
                data=cursor.fetchone()
                conn.commit()
                conn.close()
                print(data)
                if data:
                    taskTitle_value,taskId_value,taskemployeeId_value,taskManagerId_value,shiftId_value=data
                    self.taskTitle=taskTitle_value
                    self.taskId =taskId_value
                    self.taskemployeeId =taskemployeeId_value
                    self.taskManagerId =taskManagerId_value
                    self.shiftId=shiftId_value

                    taskTitle_tetx.value=self.taskTitle
                    taskId_text_.value=self.taskId
                    taskemployeeId_text.value=self.taskemployeeId
                    taskManagerId_text.value=self.taskManagerId
                    shiftId_text.value=self.shiftId
                    self.update()
                    

                    
                    


            return Column([
                Row([
                    Text("Task Tittle:"),
                    taskTitle_tetx
                    ]),
                
                Row([
                    Text("Task Id:"),
                    taskId_text_
                    ]),
                Row([
                    Text("Employee Id:"),
                    taskemployeeId_text
                    ]),
                Row([
                    Text("Task Manager:"),
                    taskManagerId_text
                    ]),
                Row([
                    Text("Shift Id:"),
                    shiftId_text
                    ]),
                Row([
                    ElevatedButton("Check Task",on_click=CheckTask),
                    ElevatedButton("Go Back",on_click=lambda _:page.go("/employeeDashboard"))

                    ])



                ])
            
    taskPage=Container(
        Container(
            Stack([
                Container(
                    border_radius=11,
                    rotate=Rotate(0.98*3.14),#degree
                    width=460,
                    height=560,
                    bgcolor="#22ffffff"
                    ),
                Container(
                    Container(
                        Column([
                            Container(
                                padding=padding.only(110,20),
                                ),
                            Text(
                                "Shift Portal ",
                                width=460,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        taskClass(),
                                        Row([
                                             
                                             ])
                                   
                                   ]),padding=padding.only(20,100),
                                
                                    
                                    ),
                                width=455,
                                height=590,
                                bgcolor='white',
                                border_radius=8
                                ),
                            ])
                        ),
                    width=460,
                    height=860,
                    bgcolor="#22ffffff",
                    border_radius=11,
                    )
                ]),
            padding=50,
            width=360,
            height=780
            ),
        width=880,
        height=1160,
        #gradient=LinearGradient(['red','white'])
        )
    #REQUEST
    def request_(e):
        try:
            status="pending"
            conn=sqlite3.connect('Dodhia.db')
            cursor=conn.cursor()
            cursor.execute("INSERT INTO requestTable(requestId,requestName,employeeName,employeeId,managerName ,managerId,status) VALUES(?,?,?,?,?,?,?)",
                           (requstId.value,requestName.value,employeeName.value,employeeId.value,managerName.value,managerId.value,status))
            conn.commit()
            print("REQUEST SENT")
        except sqlite3.Error as e:
            print("REQUEST ERROR:",e)
        finally:
            conn.close()
    
    
    requstId=ft.TextField(hint_text="Enter Request Id",color='black',border="underline",width=300)
    requestName=ft.TextField(hint_text="Enter Request Name",color='black',border="underline",width=300)
    employeeName=ft.TextField(hint_text="Enter Employee Name",color='black',border="underline",width=300)
    employeeId=ft.TextField(hint_text="Enter Employee Id",color='black',border="underline",width=300)
    managerName=ft.TextField(hint_text="Enter Manager Name",color='black',border="underline",width=300)
    managerId=ft.TextField(hint_text="Enter Manager Id",color='black',border="underline",width=300)
    submit=ft.ElevatedButton("Send Request",on_click=request_)
    request=Container(
        Container(
            Stack([
                Container(
                    border_radius=11,
                    rotate=Rotate(0.98*3.14),#degree
                    width=460,
                    height=560,
                    bgcolor="#22ffffff"
                    ),
                Container(
                    Container(
                        Column([
                            Container(
                                padding=padding.only(110,20),
                                ),
                            Text(
                                "Shift Portal ",
                                width=460,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        requstId,
                                        requestName,
                                        employeeName,
                                        employeeId,
                                        managerName,
                                        managerId,
                                        
                                        Row([
                                        submit,
                                        ElevatedButton("Go Back",on_click=lambda _:page.go("/employeeDashboard")),
                                        
                                             ])
                                   
                                   ]),padding=padding.only(20,100),
                                
                                    
                                    ),
                                width=455,
                                height=590,
                                bgcolor='white',
                                border_radius=8
                                ),
                            ])
                        ),
                    width=460,
                    height=860,
                    bgcolor="#22ffffff",
                    border_radius=11,
                    )
                ]),
            padding=50,
            width=360,
            height=780
            ),
        width=880,
        height=1160,
        #gradient=LinearGradient(['red','white'])
        )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [#LANDING PAGE
                    logInnPage
                    ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                )
            )
        if page.route=="/employeeDashboard":
            page.views.append(
                ft.View(
                    "/employeeDashboard",
                    [
                        dashboardpage,
                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()
        if page.route=="/schedulePage":
            page.views.append(
                ft.View(
                    "/schedulePage",
                    [
                        schedulePage 

                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()
        if page.route=="/shiftPage":
            page.views.append(
                ft.View(
                    "/shiftPage",
                    [
                       shiftPage

                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()
        if page.route=="/taskPage":
            page.views.append(
                ft.View(
                    "/taskPage",
                    [
                        taskPage

                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()
        if page.route=="/requestPage":
            page.views.append(
                ft.View(
                    "/requestPage",
                    [
                        request

                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()

     #Routing engine
    def view_pop(view):
        page.views.pop()
        top_view=page.views[-1]
        page.go(top_view.route)
    page.on_route_change=route_change
    page.on_view_pop=view_pop
    page.go(page.route)
    page.update()


ft.app(target=main)
