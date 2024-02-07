from flet import *
import flet as ft
import sqlite3

def main(page:ft.Page):
    page.title="ADMIN PORTAL"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.padding=350
    page.theme_mode="light"
    #page.add(body)
    page.update()

    def Login(e):
        adminName.error_text=""
        password.error_text=""
        if not adminName.value:
            adminName.error_text="Missing Admin Name"
            page.update()
        elif not password.value:
            password.error_text="Missing Admin Password"
            page.update()
        else:
            conn = sqlite3.connect('Dodhia.db')
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM managerTable WHERE managerName=? AND managerId=?",(adminName.value,password.value))
            admin=cursor.fetchone()
            conn.commit()
            conn.close()
            if admin is not None:
                page.go("/adminDashboard")
                print("LoginSuccesfull")
            else:
                password.error_text="Invalid Inputs. Try Again"
                page.update()
                print("Loggin Failed")

    adminName=ft.TextField(hint_text="Enter Admin Name",color='black',border="underline",width=300)
    password=ft.TextField(hint_text="Enter Admin Password",color='black',border="underline",width=300)
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
                                "Admin login ",
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
                                   adminName,
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
    def manageEmployee(e):
        page.go("/managemEmployeePage")
    def GenerateSchedule(e):
        page.go("/generateSchedulePage")
    def assigntaskFunc(e):
        page.go("/assignTaskPage")
    def shiftFunc(e):
        page.go("/shiftPage")
    def requestmanagementFunc(e):
        page.go("/requestmanagementPage")
    
    def Logout(e):
        page.go("/")
    schedule=ft.TextButton("Manage Employee",on_click=manageEmployee)
    shift=ft.TextButton("Generate Schedule",on_click=GenerateSchedule)
    Task=ft.TextButton("Assign Task",on_click=assigntaskFunc)
    shift__=ft.TextButton("Shift Management",on_click=shiftFunc)
    Request=ft.TextButton("Request Management",on_click=requestmanagementFunc)
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
                                "Admin Dashboard ",
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
                                        shift__,
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
    
    def register(e):
        id_=employeeID.value
        name=employeeName.value
        gender=employeeGender.value
        email=employeeemail.value
        try:
            conn=sqlite3.connect('Dodhia.db')
            cursor=conn.cursor()
            cursor.execute("INSERT INTO employeeTable (employeeId,employeeName,gender,emailAddress) VALUES (?,?,?,?)",
                           (id_,name,gender,email))
            conn.commit()
            print("Data added")
        except sqlite3.Error as e:
            print("Employee Registration Error",e)
        finally:
            conn.close
            

    def goback(e):
        page.go("/adminDashboard")
    #MANAGE EMPLOYEE
    employeeID=ft.TextField(hint_text="Enter Employee Id",color='black',border="underline",width=300)
    employeeName=ft.TextField(hint_text="Enter Employee Name",color='black',border="underline",width=300)
    employeeGender=ft.TextField(hint_text="Enter Employee Gender",color='black',border="underline",width=300)
    employeeemail=ft.TextField(hint_text="Enter Employee Email",color='black',border="underline",width=300)
    register=ft.ElevatedButton("Register",on_click=register)
    goback=ft.ElevatedButton("Go Back",on_click=goback)
    manageEmployeePage=Container(
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
                                "Employee Management Dashboard ",
                                width=360,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        employeeID,
                                        employeeName,
                                        employeeGender,
                                        employeeemail,
                                        Row([register,
                                             goback
                                             ])
                                   
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
    def schedule_(e):
        try:
            conn=sqlite3.connect('Dodhia.db')
            cursor=conn.cursor()
            cursor.execute("INSERT INTO scheduleTable(scheduleId,taskId,shiftId,data,managerId,employeeId) VALUES(?,?,?,?,?,?)",
                           (scheduleId.value,taskId.value,shiftId.value,date.value,managerId_.value,employeeId_.value))
            conn.commit()
            print("Schedule data added successfuly")
        except sqlite3.Error as e:
            print("SCHEDULE ERROR:",e)
        finally:
            conn.close()
            

    def goback_(e):
        page.go("/adminDashboard")
        
    #SCHEDULE CONTROLS
    scheduleId=ft.TextField(hint_text="Enter Schedule Id",color='black',border="underline",width=300)
    taskId=ft.TextField(hint_text="Enter Task Id",color='black',border="underline",width=300)
    shiftId=ft.TextField(hint_text="Enter Shift Id",color='black',border="underline",width=300)
    date=ft.TextField(hint_text="Enter Date",color='black',border="underline",width=300)
    managerId_=ft.TextField(hint_text="Enter Manager Id",color='black',border="underline",width=300)
    employeeId_=ft.TextField(hint_text="Enter Employee Id",color='black',border="underline",width=300)
    schedule=ft.ElevatedButton("Schedule",on_click=schedule_)
    goback_=ft.ElevatedButton("Go Back",on_click=goback_)

    schedulePageBody=Container(
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
                                "Schedule Management Portal ",
                                width=360,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        scheduleId,
                                        taskId,
                                        shiftId,
                                        date,
                                        managerId_,
                                        employeeId_,
                                        Row([schedule,
                                             goback_
                                             ])
                                   
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
    #ASSIGN TASK
    def assignTask(e):
        try:
            conn=sqlite3.connect('Dodhia.db')
            cursor=conn.cursor()
            cursor.execute("INSERT INTO assignTaskTable(taskTitle,taskId,taskemployeeId,taskManagerId,shiftId) VALUES(?,?,?,?,?)",
                           (taskttitle.value,taskId.value,assigned_emolpoyeeId.value,taskManagerId.value,shiftId.value))
            conn.commit()
            print("Task Assigin Succesfully")
        except sqlite3.Error as e:
            print("TASK ASSIGNING ERROR:",e)
        finally:
            conn.close()


    def Goback_(e):
        page.go("/adminDashboard")
    taskttitle=ft.TextField(hint_text="Enter Task Tittle",color='black',border="underline",width=300)
    taskId=ft.TextField(hint_text="Enter Task Id",color='black',border="underline",width=300)
    assigned_emolpoyeeId=ft.TextField(hint_text="Enter Assigned Emolpyee Id",color='black',border="underline",width=300)
    taskManagerId=ft.TextField(hint_text="Enter Task Manager Id",color='black',border="underline",width=300)
    shiftId=ft.TextField(hint_text="Enter Shift Id",color='black',border="underline",width=300)
    assignTask=ft.ElevatedButton("Assign Task",on_click=assignTask)
    Goback_=ft.ElevatedButton("Go Back",on_click=Goback_)


    assignTaskBodyPage=Container(
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
                                "Assign Task Portal ",
                                width=360,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        taskttitle,
                                        taskId,
                                        assigned_emolpoyeeId,
                                        taskManagerId,
                                        shiftId,
                                        Row([assignTask,
                                             Goback_
                                             ])
                                   
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
    #SHIFT
    def shift__(e):
        try:
            conn=sqlite3.connect('Dodhia.db')
            cursor=conn.cursor()
            cursor.execute("INSERT INTO shiftTable(shiftId,taskId,scheduleDate,startTime,endTime,shiftManagerId,taskManagerId) VALUES (?,?,?,?,?,?,?)",
                           (shiftId_.value,taskId.value,scedlueDate.value,startTime.value,endTime.value,shiftManagerId.value,taskManagerId.value,))
            conn.commit()
            print("SHIFT DATA ADDEED")
        except sqlite3.Error as e:
            print("SHIFT MANAGEMENT ERROR:",e)
        finally:
            conn.close()
            
    
    def Goback__(e):
        page.go("/adminDashboard")
    
    shiftId_=ft.TextField(hint_text="Enter Shift Id",color='black',border="underline",width=300)
    taskId=ft.TextField(hint_text="Enter Task Id",color='black',border="underline",width=300)
    scedlueDate=ft.TextField(hint_text="Enter Schedule Date",color='black',border="underline",width=300)
    startTime=ft.TextField(hint_text="Enter Start Time",color='black',border="underline",width=300)
    endTime=ft.TextField(hint_text="Enter End Time",color='black',border="underline",width=300)
    shiftManagerId=ft.TextField(hint_text="Enter Shift Manager ID",color='black',border="underline",width=300)
    taskManagerId=ft.TextField(hint_text="Enter Task Manager Id",color='black',border="underline",width=300)
    shift=ft.ElevatedButton("Assign Task",on_click=shift__)
    Goback__=ft.ElevatedButton("Go Back",on_click=Goback__)


    shiftBodyPage=Container(
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
                                "Shift Management Portal ",
                                width=360,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        shiftId_,
                                        taskId,
                                        scedlueDate,
                                        startTime,
                                        endTime,
                                        shiftManagerId,
                                        taskManagerId,
                                        Row([shift,
                                             Goback__
                                             ])
                                   
                                   ]),padding=padding.only(20,100),
                                
                                    
                                    ),
                                width=355,
                                height=590,
                                bgcolor='white',
                                border_radius=8
                                ),
                            ])
                        ),
                    width=360,
                    height=860,
                    bgcolor="#22ffffff",
                    border_radius=11,
                    )
                ]),
            padding=50,
            width=360,
            height=780
            ),
        width=780,
        height=1160,
        #gradient=LinearGradient(['red','white'])
        )
    #REQUEST
    employeeId=ft.TextField(hint_text="Search By Employee Id",color='black',border="underline",width=300)
    class Request_(ft.UserControl):
        def build(self):
            self.requestId=""
            self.requestName =""
            self.employeeName =""
            self.employeeId =""
            self.managerName=""
            self.status=""

            requestId_text=ft.Text(self.requestId,size=15)
            requestName_text=ft.Text(self.requestName,size=15)
            employeeName_tetx=ft.Text(self.employeeName,size=15)
            employeeId_tetx=ft.Text(self.employeeId,size=15)
            managerName_tetx=ft.Text(self.managerName,size=15)
            requestStatus_text=ft.Text(self.status,size=15)

            def searchRequest(e):
                query=employeeId.value
                conn=sqlite3.connect('Dodhia.db')
                cursor=conn.cursor()
                cursor.execute("SELECT requestId,requestName,employeeName,employeeId,managerName,status FROM requestTable WHERE employeeId=? ",(query,))
                data=cursor.fetchone()
                print(data)
                if data:
                    requestId_value,requestName_value,employeeName_value,employeeId_value,managerName_value,status_value=data
                    self.requestId=requestId_value
                    self.requestName =requestName_value
                    self.employeeName =employeeName_value
                    self.employeeId=employeeId_value
                    self.managerName=managerName_value
                    self.status=status_value
                    
                    requestId_text.value=self.requestId
                    requestName_text.value=self.requestName
                    employeeName_tetx.value=self.employeeName
                    employeeId_tetx.value=self.employeeId
                    managerName_tetx.value=self.managerName
                    requestStatus_text.value=self.status
                    self.update()
                    
                else:
                    print("Data not found")
            def grantRequest(e):
                ##UPDATE REQUEST STATUS
                entry=employeeId.value
                status_="Approved"
                conn=sqlite3.connect('Dodhia.db')
                cursor=conn.cursor()
                cursor.execute("UPDATE requestTable SET status=? WHERE employeeId=?",(status_,entry))
                conn.commit()
                print("REQUEST GRANTED")
                conn.close()

                
            def denieRequest(e):
                ##DELETE REQUEST
                entry=employeeId.value
                
                conn=sqlite3.connect('Dodhia.db')
                cursor=conn.cursor()
                cursor.execute("DELETE FROM requestTable WHERE employeeId=?",(entry,))
                conn.commit()
                print("Row Deleted")
                conn.close()
                



            return Column([
                Row([
                    Text("Request Status",weight='bold',size=15),
                    requestStatus_text
                    ]),
                Row([
                    Text("Request ID",weight='bold',size=15),
                    requestId_text
                    ]),
                Row([
                    Text("Request Name",weight='bold',size=15),
                    requestName_text
                    ]),
                Row([
                    Text("Employee Name ",weight='bold',size=15),
                    employeeName_tetx
                    ]),
                Row([
                    Text("Employee ID",weight='bold',size=15),
                    employeeId_tetx
                    ]),
                Row([
                    Text("Manager Name",weight='bold',size=15),
                    managerName_tetx
                    ]),
                Row([
                    ElevatedButton("Search Request",on_click=searchRequest),
                    ElevatedButton("Grant Request",on_click=grantRequest),
                    ElevatedButton("Denie Request",on_click=denieRequest)

                    ])


                ])
    requestBodyPage=Container(
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
                                "Request Management Portal ",
                                width=460,
                                size=15,
                                weight="w900",
                                text_align="center",
                                color='black'
                                ),
                            Container(
                                Container(
                                    
                                    Column([
                                        employeeId,
                                        Request_(),
                                        Row([
                                             Goback__
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
        if page.route=="/adminDashboard":
            page.views.append(
                ft.View(
                    "/adminDashboard",
                    [
                        ft.Text("Employee Management dashboard",weight="bold"),
                        dashboardpage,
                        ft.ElevatedButton("Go Back", on_click =lambda _:page.go("/")) 

                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()
        if page.route=="/managemEmployeePage":
            page.views.append(
                ft.View(
                    "/managemEmployeePage",
                    [
                        manageEmployeePage, 

                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()
        if page.route=="/generateSchedulePage":
            page.views.append(
                ft.View(
                    "/generateSchedulePage",
                    [
                        schedulePageBody
                        

                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()
        if page.route=="/assignTaskPage":
            page.views.append(
                ft.View(
                    "/assignTaskPage",
                    [
                        assignTaskBodyPage

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
                        shiftBodyPage

                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()
            
        if page.route=="/requestmanagementPage":
            page.views.append(
                ft.View(
                    "/requestmanagementPage",
                    [
                        requestBodyPage 

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
