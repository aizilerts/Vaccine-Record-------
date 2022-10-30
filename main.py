from tkinter import * # gui module
import vaccine_record 

#this method should be called when "Submit"   button is clicked
def process():
  print("submit was clicked")
  
  theEntry = vaccine_record.VaccineRecord(first_name_entry.get(), last_name_entry.get(), dob_entry.get(), first_manufacturer_entry.get(), first_batch_entry.get(), first_date_entry.get(), first_location_entry.get(), second_manufacturer_entry.get(), second_batch_entry.get(), second_date_entry.get(), second_location_entry.get())
  theEntry.printCard()

#this method should be called when checkbox is ticked/unticked. Have an IF for off, ELSE   for on
def checkbox_process():
  print("checkbox interaction")
  print(no_second_dose.get())
  if (no_second_dose.get() == 1):

    second_manufacturer.grid_remove()
    second_batch.grid_remove()
    second_date.grid_remove()
    second_location.grid_remove()
    
    second_manufacturer_entry.grid_remove()
    second_batch_entry.grid_remove()
    second_date_entry.grid_remove()
    second_location_entry.grid_remove()
  else:
    second_manufacturer.grid(row = 9, column = 0)
    second_manufacturer_entry.grid(row = 9, column = 1)

    second_batch.grid(row = 10, column = 0)
    second_batch_entry.grid(row = 10, column = 1)

    second_date.grid(row = 11, column = 0)
    second_date_entry.grid(row = 11, column = 1)

    second_location.grid(row = 12, column = 0)
    second_location_entry.grid(row = 12, column = 1)
    

#begin code for GUI 

main_window = Tk()
main_window.title("Vaccine Entry")
main_window.geometry("600x600")

#Labels for dose 1
first_name = Label(main_window, text = "Enter first name:")
last_name = Label(main_window, text = "Enter last name:")
dob = Label(main_window, text = "Enter date of birth (mm/dd/yyyy):")

first_dose = Label(main_window, text = "Information of first dose:")

first_manufacturer = Label(main_window, text = "Enter first manufacturer")
first_batch = Label(main_window, text = "Enter first batch:")
first_date = Label(main_window, text = "Enter date (mm/dd/yyyy)")
first_location = Label(main_window, text = "Enter location:")

second_dose = Label(main_window, text = "Information of second dose:")

second_manufacturer = Label(main_window, text = "Enter second manufacturer")
second_batch = Label(main_window, text = "Enter second batch:")
second_date = Label(main_window, text = "Enter date (mm/dd/yyyy)")
second_location = Label(main_window, text = "Enter location:")


##Entries
first_name_entry = Entry(main_window, bd = 5)
last_name_entry = Entry(main_window, bd = 5)
dob_entry = Entry(main_window, bd = 5)

first_dose_entry = Entry(main_window, bd = 5)
first_manufacturer_entry = Entry(main_window, bd = 5)
first_batch_entry = Entry(main_window, bd = 5)
first_date_entry = Entry(main_window, bd = 5)
first_location_entry = Entry(main_window, bd = 5)

second_dose_entry = Entry(main_window, bd = 5)
second_manufacturer_entry = Entry(main_window, bd = 5)
second_batch_entry = Entry(main_window, bd = 5)
second_date_entry = Entry(main_window, bd = 5)
second_location_entry = Entry(main_window, bd = 5)

##Buttons
submit = Button(main_window, text = "Done", command = process)

no_second_dose = IntVar()


check_box = Checkbutton(main_window, text = "no second dose", variable = no_second_dose, command = checkbox_process)

##Adding to frame

first_name.grid(row = 0, column = 0)
first_name_entry.grid(row = 0, column = 1)

last_name.grid(row = 1, column = 0)
last_name_entry.grid(row = 1, column = 1)

dob.grid(row = 2, column = 0)
dob_entry.grid(row = 2, column = 1)


first_dose.grid(row = 3, column = 1)

first_manufacturer.grid(row = 4, column = 0)
first_manufacturer_entry.grid(row = 4, column = 1)

first_batch.grid(row = 5, column = 0)
first_batch_entry.grid(row = 5, column = 1)

first_date.grid(row = 6, column = 0)
first_date_entry.grid(row = 6, column = 1)

first_location.grid(row = 7, column = 0)
first_location_entry.grid(row = 7, column = 1)


second_dose.grid(row = 8, column = 1)

second_manufacturer.grid(row = 9, column = 0)
second_manufacturer_entry.grid(row = 9, column = 1)

second_batch.grid(row = 10, column = 0)
second_batch_entry.grid(row = 10, column = 1)

second_date.grid(row = 11, column = 0)
second_date_entry.grid(row = 11, column = 1)

second_location.grid(row = 12, column = 0)
second_location_entry.grid(row = 12, column = 1)

check_box.grid(row = 8, column = 3)

submit.grid(row = 13, column = 2)

checkbox_process()

mainloop()