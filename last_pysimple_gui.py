import PySimpleGUI as sg
sg.theme("DarkTeal12")
#r=open('output.txt','r+')
def  output(values):
    window.FindElement('list_box').Update(values=todolist)
    window.FindElement('priority_box').Update(values=droplist)
    window.FindElement('date_box').Update(values=datelist)

    window.FindElement('open_work').Update('opened')
    
   




    
def add_task(values):
    task=values['taskname']
    todolist.append(task)
    #todolist1.append(task)
    window.FindElement('taskname').Update(value="")
    window.FindElement('list_box').Update(values=todolist)
    window.FindElement('add_work').Update('add')
    
def edit_task(values):
    edit_value=values['list_box'][0]
    window.FindElement('taskname').Update(value=edit_value)
    #drop_value=values['priority_box'][0]
    drop_value=droplist[todolist.index(edit_value)]
    date_value=datelist[todolist.index(edit_value)]
    window.FindElement('drop_down').Update(value=drop_value)
    window.FindElement('date').Update(value=date_value)
    
    droplist.remove(drop_value)
    todolist.remove(edit_value)
    datelist.remove(date_value)
    #droplist1.remove(drop_value)
    #todolist1.remove(edit_value)
    
    window.FindElement('add_work').Update('Save')
    
    
def delete_task(values):
    delete_value=values['list_box'][0]
    
    drop_value=droplist[todolist.index(delete_value)]
    date_value=datelist[todolist.index(delete_value)]
    datelist.remove(date_value)
    todolist.remove(delete_value)
    droplist.remove(drop_value)
    #todolist1.remove(delete_value)
    #droplist1.remove(drop_value)
    window.FindElement('list_box').Update(values=todolist)
    window.FindElement('priority_box').Update(values=droplist)
    window.FindElement('date_box').Update(values=datelist)
    
def priority(values):
    drop=values['drop_down']
    droplist.append(drop)
    #droplist1.append(drop)
    window.FindElement('drop_down').Update(value='')
    window.FindElement('priority_box').Update(values=droplist)
def deadline_date(values):
    dates=values['date']
    datelist.append(dates)
    window.FindElement('date').Update(value='')
    window.FindElement('date_box').Update(values=datelist)
    
layout=[
    [sg.Text("Enter the task:",font=("Arial",14)),sg.InputText

("",font=("Arial",14), size=(20,1),key="taskname"),
     sg.Button("open",font=("Arial",12),key="open_work")],
     [sg.Button("add",font=("Arial",12),key="add_work"),
      sg.Button("Edit",font=("Arial",12),key="edit_work"),
     sg.Button("Delete",font=("Arial",12),key="delete_work")
      ],
     [sg.Text("select the priority:",font=("Arial",14)),sg.InputCombo(['very imp','imp','later'],size=(9,0),key="drop_down"),sg.Text("deadline date:"),sg.InputText("",font=("Arial",12),size=(9,1),key="date")],
     [sg.Listbox(values=[],font=("Arial",14),size=(20,9),key="list_box"),sg.Listbox(values=[],font=("Arial",14),size=(9,9),key="priority_box"),sg.Listbox(values=[],font=("Arial",14),size=(9,9),key="date_box")],
     [sg.Text("*Enter date in ( DD / MM / YYYY ) format ",font=("Arial",10))],
     [sg.Text("*Do not try to open a opened file again",font=("Arial",10))],
     [sg.Text("*Pls make sure to save a edited task",font=("Arial",10))]
    ]
todolist =[]
droplist=[]
datelist=[]
listboxopen=[]
todolist1= []
droplist1=[]
window=sg.Window('TO_DO_LIST',layout)

while True:
    
    event,values=window.Read()
    
    if event=='open_work':
        with open('output_pysimplegui.txt','r') as f:
            lines=f.readlines()
            print(lines)
            for l in lines:
                as_list = l.split(",")
                todolist.append(as_list[0])
                droplist.append(as_list[1])
                datelist.append(as_list[2].replace("\n",""))
                output(values)
                
                    
            
               # print(todolistopen)
                #print(droplistopen)
            
    elif event=='add_work':
            add_task(values)
            priority(values)
            deadline_date(values)
            
    elif event=='edit_work':
            edit_task(values)
            window.FindElement('list_box').Update(values=todolist)
            window.FindElement('priority_box').Update(values=droplist)
            window.FindElement('date_box').Update(values=datelist)

    elif event=='delete_work':
            delete_task(values)
    else:
        with open('output_pysimplegui.txt','a+') as f:        
                for i in range(len(todolist)):
                    f.writelines([str(todolist[i])+','+str(droplist[i])+','+str(datelist[i])+'\n'])
            
        break


#print(todolist)
#print(droplist)


            
#r.close()
