from tkinter import  *
import  tkinter.ttk as t

#create the app window
tree=Tk()
tree.title('Family Details')
#create the tree view object and header
tr=t.Treeview(tree)
tr.pack()
tr.heading('#0',text='Name')
tr.column('#0',anchor=CENTER,width=110)

#adding data to the first column
family_names=['Tom','Sara','Harry','Jhon','Tommy']
family=['Father','Mother','Son1','Son2','Son3']
for name,kind,i in zip(family_names,family,range(5)):
    tr.insert('',str(i) ,kind,text=name)

tr.insert('Father','0','Son_1',text='Harry')
tr.insert('Father','1','Son_2',text='Jhon')
tr.insert('Father','2','Son_3',text='Tommy')
tr.move('Son1','Mother','0')
tr.move('Son2','Mother','1')
tr.move('Son3','Mother','2')

#creating the age and jobs and type columns
tr.configure(column=('#t','#a','#j'))
tr.heading('#t',text='Type')
tr.heading('#j',text='Job')
tr.heading('#a',text='Age')
tr.column('#t',anchor=CENTER,width=90)
tr.column('#j',anchor=CENTER,width=130)
tr.column('#a',anchor=CENTER,width=70)

#filling them with data
family_ids=['Father','Mother','Son1','Son2','Son3','Son_1','Son_2','Son_3']
Ages=[48,44,29,26,22,29,26,22]
for kind,age in zip(family_ids,Ages):
    tr.set(kind,'#a',age)

jobs=['Consultant_General_Manger','HeadMaster_Teacher','Free_Lancer_Dev','Doctor','Student','Free_Lancer_Dev','Doctor','Student']
for job,member in zip(jobs,family_ids):
    tr.set(member,'#j',job)

types=['Father','Mother','First Son','Second Son','Third Son','First Son','Second Son','Third Son']
for typ,memb in zip(types,family_ids):
    tr.set(memb,'#t',typ)
    
tree.mainloop()
