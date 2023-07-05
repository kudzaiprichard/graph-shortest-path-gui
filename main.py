import graph
from bellman_ford import *
import tkinter 
from tkinter import ttk
from tkinter import messagebox


# #Define graph         
E = [('Marondera', 'Mutoko', 148), ('Marondera', 'Mutare', 188.6), ('Mutoko', 'Mutare', 268.2), 
        ('Mutoko', 'Gweru', 420),('Mutoko', 'Harare', 142.3), ('Mutare', 'Kwekwe', 417.7), 
        ('Mutare', 'Harare', 262.9), ('Gweru', 'Harare', 277.6), ('Gweru', 'Kwekwe', 58), 
        ('Gweru', 'Zvishavane', 121.7), ('Kwekwe', 'Zvishavane', 18.37)]

def value_changed(event):
        if(start_selected_elem.get() == "Marondera"):
                end_vertex_input.set('')
                end_vertex_input['values'] = ("Marondera","Mutoko","Mutare","Gweru","Harare","Kwekwe","Zvishavane")
                
        elif(start_selected_elem.get() == "Kwekwe"):
                end_vertex_input.set('')
                end_vertex_input['values'] = ("Kwekwe","Zvishavane")
                
        elif(start_selected_elem.get() == "Mutoko"):
                end_vertex_input.set('')
                end_vertex_input['values'] = ("Mutoko","Mutare","Gweru","Harare","Kwekwe","Zvishavane")
                
        elif(start_selected_elem.get() == "Mutare"):
                end_vertex_input.set('')
                end_vertex_input['values'] = ("Mutare","Harare","Kwekwe","Zvishavane")
                
        elif(start_selected_elem.get() == "Gweru"):
                end_vertex_input.set('')
                end_vertex_input['values'] = ("Gweru","Harare","Kwekwe","Zvishavane")
        
        
def compute():
        # #Initialize/ create graph
        G, weight_mapping = graph.create_graph(E)
        start = start_vertex_input.get()
        end   = end_vertex_input.get()

        #If user haven't selected anything
        if(not start or not end ):
                messagebox.showwarning(title="Error", message="Please select start and end vertex")
                return False

        #get first and end vertex
        start_vertex = G.get_vertex(start)
        end_vertex = G.get_vertex(end)

        #Get the shortest path
        ford = Bellman_ford(G, weight_mapping, start_vertex, end_vertex)
        ford.execute()
        result_x,result_y = ford.get_results()

        #create labels for results
        if(result_x or result_y):
                messagebox.showinfo(message=result_y + "\n" + result_x)
                
                
#create a new tkinter window
window = tkinter.Tk()
window.title("Graph Assignment")

frame = tkinter.Frame(window)
frame.pack()

#define a label frame
input_frame = tkinter.LabelFrame(frame, text="Enter start and destination")
input_frame.grid(row = 0, column = 0)

#create start and end labels
start_vertex_label =  tkinter.Label(input_frame, text="Start destination")
start_vertex_label.grid(row=0, column=0)
end_vertex_label =  tkinter.Label(input_frame, text="End destination")
end_vertex_label.grid(row=0, column=1)

#create start and end combobox
start_selected_elem = tkinter.StringVar(value='Marondera')
start_vertex_input = ttk.Combobox(input_frame, text=start_selected_elem)
start_vertex_input['values'] = ("Marondera","Mutoko","Mutare","Gweru","Kwekwe")
start_vertex_input.bind('<<ComboboxSelected>>', value_changed)

end_selected_elem = tkinter.StringVar(value='')
end_vertex_input = ttk.Combobox(input_frame, text=end_selected_elem)
end_vertex_input['values'] = ("Marondera","Mutoko","Mutare","Gweru","Harare","Kwekwe","Zvishavane")

start_vertex_input.grid(row=1,column=0)
end_vertex_input.grid(row=1,column=1)

#assign padding for all widgets on the screen
for widget in input_frame.winfo_children():
        widget.grid_configure(padx = 20, pady = 5)
        
#button for triggering event
button = tkinter.Button(frame, text="Compute", command=compute)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)


window.mainloop()



