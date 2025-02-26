from tkinter import *

#Widget is a object with specific information or function

#Creating the main window widget
root = Tk()

#variable to manipulate text counter
#p_count = 3
#button interaction
#########################   METHODS   #########################
def on_click():
    #global p_count
    pie = item.get()
    label3 = Label(root, text=pie, font=(32)).grid(row = 5, column =3)
    #p_count += 1
    print("IIIII LIKE " + pie)
    
def rbutton(value):
    label4 = Label(root, text=myradiovar.get())
    label4.grid(row = 8, column = 0)
    
#Create a widget to display in our root
#label = Label(root, text="Me pueden decir...porque estan ustedes tan...")

#Two options: pack the object[take whatever you need, pass to root widget], 
#OR ... GRIDS

#1.Packing widgets in the root (centered on screen, but not flexible)
#label.pack()

#2.Using grids to create a window

######################### Widgets ###################################
#labels
label = Label(root, text="Me pueden decirr...",font=(24)).grid(row = 0, column = 0)
label2 = Label(root, text="Porque estan ustedes tan...", font=(24)).grid(row = 1, column = 1)
#button widgets
mybutton = Button(root, text="Click Here :)", command = on_click).grid(row=2, column = 2)
#methods can be concatenated
item = Entry(root)
item.insert(0,"Type your favorite pie")
#Every widget can have a default value

#Drop Menu Setup
drop_var = StringVar()
drop_var.set("Choose a pie")
drop_menu = OptionMenu(root, drop_var, "Keylime", "Pumpkin", "Pecan", "Blueberry")
#thecoolpie = drop_var.get()


#Radio Button setup
myradiovar = IntVar()
#myrad = Radiobutton(root, text="Option1", variable = myradiovar, value = 1)
#myrad2 = Radiobutton(root, text="Option2", variable = myradiovar, value = 2)

options = ["Option1", "Option2", "Option3"]


counter = 0
for option in options:
    Radiobutton(root, text=option, variable = myradiovar, value = counter, command = lambda:rbutton(myradiovar.get())).grid(row = counter+4, column = 0)
    counter +=1

#gridding
#label.grid(row = 0, column = 0)
#label2.grid(row = 1, column = 1)
#mybutton.grid(row=2, column = 2)
item.grid(row = 3,column = 0)
drop_menu.grid(row = 8, column = 2)




#Call the main loop for displaying the root window
root.mainloop()