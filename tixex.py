import tkinter as tk
from tkinter import messagebox

class MenuBar(tk.Menu):
    def __init__(self, master):
        super().__init__(master)

        # create the menu items
        add_menu = tk.Menu(self, tearoff=0)
        show_menu = tk.Menu(self, tearoff=0)
        edit_menu = tk.Menu(self, tearoff=0)
        search_menu = tk.Menu(self, tearoff=0)
        delete_menu = tk.Menu(self, tearoff=0)
        look_menu = tk.Menu(self, tearoff=0)

        # add the options to each menu
        add_menu.add_command(label="Add Trainee", command=self.show_add_form)
        show_menu.add_command(label="Show Trainee", command=self.show_trainee_profiles)
        delete_menu.add_command(label="Delete Trainee", command=self.show_delete_form)
        edit_menu.add_command(label="Edit Trainee", command=self.show_edit_form)
        search_menu.add_command(label="Search for Trainee by the Name", command=self.search_trainee_by_name)
        search_menu.add_command(label="Search for Trainee by the Age", command=self.search_trainee_by_age)
        look_menu.add_command(label="Look up for Trainee", command=self.look_up)

        # add the menus to the menu bar
        self.add_cascade(label="ADD", menu=add_menu)
        self.add_cascade(label="SHOW", menu=show_menu)
        self.add_cascade(label="DELETE", menu=delete_menu)
        self.add_cascade(label="EDIT", menu=edit_menu)
        self.add_cascade(label="SEARCH", menu=search_menu)
        self.add_cascade(label="LOOK UP", menu=look_menu)

        # add the exit option to the menu bar
        self.add_command(label="EXIT", command=master.quit)

        # initialize trainee data structure
        self.trainees = []

    def show_add_form(self):
        # create a new window for the form
        form_window = tk.Toplevel(self.master)

        # add the form elements
        tk.Label(form_window, text="Num:").grid(row=0, column=0)
        num_entry = tk.Entry(form_window)
        num_entry.grid(row=0, column=1)

        tk.Label(form_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(form_window)
        name_entry.grid(row=1, column=1)

        tk.Label(form_window, text="Age:").grid(row=2, column=0)
        age_entry = tk.Entry(form_window)
        age_entry.grid(row=2, column=1)

        submit_button = tk.Button(form_window, text="Submit",command=lambda: self.add_trainee(num_entry.get(), name_entry.get(),age_entry.get(), form_window))
        submit_button.grid(row=3, column=1)

    def add_trainee(self, num, name, age, form_window):
        # add trainee to data structure
        self.trainees.append({'Num': num, 'Name': name, 'Age': age})
        # display message box
        messagebox.showinfo("Success", "Trainee added successfully.")
        # clear form entries
        form_window.destroy()

    def show_trainee_profiles(self):
        # create a new window for the trainee profiles
        profile_window = tk.Toplevel(self.master)

        # add the trainee profiles
        for i, trainee in enumerate(self.trainees):
            tk.Label(profile_window, text=f"Trainee {i + 1}:").grid(row=i, column=0)
            tk.Label(profile_window, text=f"Num: {trainee['Num']}, Name: {trainee['Name']}, Age: {trainee['Age']}").grid(row=i,column=1)

        # add a message if there are no trainee profiles
        if not self.trainees:
            tk.Label(profile_window, text="No trainee profiles available.", font=("Arial Bold", 12)).grid(row=0,column=0)

    def show_delete_form(self):
        # create a new window for the form
        form_window = tk.Toplevel(self.master)

        # add the form elements
        tk.Label(form_window, text="Num:").grid(row=0, column=0)
        num_entry = tk.Entry(form_window)
        num_entry.grid(row=0, column=1)

        submit_button = tk.Button(form_window, text="Submit",command=lambda: self.delete_trainee(num_entry.get(), form_window))
        submit_button.grid(row=1, column=1)

    def delete_trainee(self, num, form_window):
        # search for the trainee with the given num
        for trainee in self.trainees:
            if trainee['Num'] == num:
                # remove the trainee from the data structure
                self.trainees.remove(trainee)
                # display message box
                messagebox.showinfo("Success", "Trainee deleted successfully.")
                # clear form entries
                form_window.destroy()
                return

        # display error message if trainee with given num not found
        messagebox.showerror("Error", "Trainee not found.")

    def show_edit_form(self):
        # create a new window for the form
        edit_window = tk.Toplevel(self.master)

        # add the form elements
        tk.Label(edit_window, text="Enter trainee number:").grid(row=0, column=0)
        num_entry = tk.Entry(edit_window)
        num_entry.grid(row=0, column=1)

        submit_button = tk.Button(edit_window, text="Submit",command=lambda: self.edit_trainee(num_entry.get(), edit_window))
        submit_button.grid(row=1, column=1)

    def edit_trainee(self, num, edit_window):
        # search for the trainee with the given num
        for trainee in self.trainees:
            if trainee['Num'] == num:
                # create a new window for editing the trainee profile
                edit_form_window = tk.Toplevel(self.master)

                # add the form elements with the trainee information pre-filled
                tk.Label(edit_form_window, text="Num:").grid(row=0, column=0)
                num_entry = tk.Entry(edit_form_window, state="disabled")
                num_entry.grid(row=0, column=1)
                num_entry.insert(0, trainee['Num'])

                tk.Label(edit_form_window, text="Name:").grid(row=1, column=0)
                name_entry = tk.Entry(edit_form_window)
                name_entry.grid(row=1, column=1)
                name_entry.insert(0, trainee['Name'])

                tk.Label(edit_form_window, text="Age:").grid(row=2, column=0)
                age_entry = tk.Entry(edit_form_window)
                age_entry.grid(row=2, column=1)
                age_entry.insert(0, trainee['Age'])

                # add a "Save" button to save the changes
                save_button = tk.Button(edit_form_window, text="Save",command=lambda: self.save_trainee(trainee, name_entry.get(), age_entry.get(),edit_form_window))
                save_button.grid(row=3, column=1)

                return

        # display error message if trainee with given num not found
        messagebox.showerror("Error", "Trainee not found.")

    def save_trainee(self, trainee, name, age, edit_form_window):
        # modify the trainee profile with the new information
        trainee['Name'] = name
        trainee['Age'] = age
        # display success message
        messagebox.showinfo("Success", "Trainee updated successfully.")
        # close the edit form window
        edit_form_window.destroy()

    def search_trainee_by_name(self):
        # create a new window for the search form
        search_window = tk.Toplevel(self.master)

        # add the search form elements
        tk.Label(search_window, text="Name:").grid(row=0, column=0)
        name_entry = tk.Entry(search_window)
        name_entry.grid(row=0, column=1)

        submit_button = tk.Button(search_window, text="Submit", command=lambda: self.display_trainees_by_name(name_entry.get(), search_window))
        submit_button.grid(row=1, column=1)

    def display_trainees_by_name(self, name, search_window):
        # create a new window for the search results
        results_window = tk.Toplevel(self.master)

        # add the search results
        for i, trainee in enumerate(self.trainees):
            if trainee['Name'].lower() == name.lower():
                tk.Label(results_window, text=f"Trainee {i + 1}:").grid(row=i, column=0)
                tk.Label(results_window,text=f"Num: {trainee['Num']}, Name: {trainee['Name']}, Age: {trainee['Age']}").grid(row=i,column=1)

        # add a message if there are no search results
        if not any(trainee['Name'].lower() == name.lower() for trainee in self.trainees):
            tk.Label(results_window, text="No trainees with that name found.").grid(row=0, column=0)

        # clear form entries and destroy search window
        search_window.destroy()

    def search_trainee_by_age(self):
        # create a new window for the search form
        search_window = tk.Toplevel(self.master)

        # add the search form elements
        tk.Label(search_window, text="Age:").grid(row=0, column=0)
        age_entry = tk.Entry(search_window)
        age_entry.grid(row=0, column=1)

        submit_button = tk.Button(search_window, text="Submit",command=lambda: self.display_trainees_by_age(age_entry.get(), search_window))
        submit_button.grid(row=1, column=1)

    def display_trainees_by_age(self, age, search_window):
        # create a new window for the search results
        results_window = tk.Toplevel(self.master)

        # add the search results
        for i, trainee in enumerate(self.trainees):
            if trainee['Age'] == age:
                tk.Label(results_window, text=f"Trainee {i + 1}:").grid(row=i, column=0)
                tk.Label(results_window,
                         text=f"Num: {trainee['Num']}, Name: {trainee['Name']}, Age: {trainee['Age']}").grid(row=i,column=1)

        # add a message if there are no search results
        if not any(trainee['Age'] == age for trainee in self.trainees):
            tk.Label(results_window, text="No trainees with that age found.").grid(row=0, column=0)

        # clear form entries and destroy search window
        search_window.destroy()

    def look_up(self):
        # create a new window for the search results
        look_window = tk.Toplevel(self.master)

        ra = tk.StringVar(value='E')
        # add the radio form elements
        age_entry = tk.Radiobutton(look_window, text=": Age", value='A', variable=ra)
        age_entry.grid(row=0, column=0)
        name_entry = tk.Radiobutton(look_window, text=": Name", value='N', variable=ra)
        name_entry.grid(row=0, column=2)

        def submit():
            selected_option = ra.get()
            if selected_option == 'A':
                self.display_lookupN(look_window)
            elif selected_option == 'N':
                self.display_lookupN(look_window)

        submit_button = tk.Button(look_window, text="Submit", command=submit)
        submit_button.grid(row=1, column=1)

    def display_lookupA(self,age):
        # create a new window for the search form
        search_window = tk.Toplevel(self.master)

        # add the search form elements
        tk.Label(search_window, text="Age:").grid(row=0, column=0)
        age_entry = tk.Entry(search_window)
        age_entry.grid(row=0, column=1)

        submit_button = tk.Button(search_window, text="Submit",
                                  command=lambda: self.look_trainees_by_age(age_entry.get(), search_window))
        submit_button.grid(row=1, column=1)

    def look_trainees_by_age(self, age, search_window):
        # create a new window for the search results
        results_window = tk.Toplevel(self.master)

        # add the search results
        for i, trainee in enumerate(self.trainees):
            if trainee['Age'] == age:
                tk.Label(results_window, text=f"Trainee {i + 1}:").grid(row=i, column=0)
                tk.Label(results_window,
                         text=f"Num: {trainee['Num']}, Name: {trainee['Name']}, Age: {trainee['Age']}").grid(row=i,
                                                                                                             column=1)

        # add a message if there are no search results
        if not any(trainee['Age'] == age for trainee in self.trainees):
            tk.Label(results_window, text="No trainees with that age found.").grid(row=0, column=0)

        # clear form entries and destroy search window
        search_window.destroy()

    def display_lookupN(self,name):
        # create a new window for the search form
        search_window = tk.Toplevel(self.master)

        # add the search form elements
        tk.Label(search_window, text="Name:").grid(row=0, column=0)
        name_entry = tk.Entry(search_window)
        name_entry.grid(row=0, column=1)

        submit_button = tk.Button(search_window, text="Submit",
                                  command=lambda: self.look_trainees_by_name(name_entry.get(), search_window))
        submit_button.grid(row=1, column=1)

    def look_trainees_by_name(self, name, search_window):
        # create a new window for the search results
        results_window = tk.Toplevel(self.master)

        # add the search results
        for i, trainee in enumerate(self.trainees):
            if trainee['Name'].lower() == name.lower():
                tk.Label(results_window, text=f"Trainee {i + 1}:").grid(row=i, column=0)
                tk.Label(results_window,text=f"Num: {trainee['Num']}, Name: {trainee['Name']}, Age: {trainee['Age']}").grid(row=i,column=1)

        # add a message if there are no search results
        if not any(trainee['Name'].lower() == name.lower() for trainee in self.trainees):
            tk.Label(results_window, text="No trainees with that name found.").grid(row=0, column=0)

        # clear form entries and destroy search window
        search_window.destroy()



def main():
    root = tk.Tk()
    root.title("Trainee Gestion")
    root.geometry("350x200")
    menubar = MenuBar(root)
    root.config(menu=menubar)
    root.mainloop()

if __name__ == "__main__":
    main()