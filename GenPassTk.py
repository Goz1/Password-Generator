from tkinter import *
import random


upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
chars = '!@#$%&*()?<>{}~-+,[]'

pass1 = ''

# Function to generate password
def generate():
    try:
        # Receive input from the user requesting for length of the password
        passwordlength = int(e.get())

        # Check the values of the input for the length of password.
        # If the user inputs the recommended length
        if (passwordlength >= 4 and passwordlength <= 20):

            # The user selects the kind of characters they want in their password
            if var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1:
                password = "".join(random.sample(upper_case + lower_case + numbers + chars, passwordlength))
                code.config(text=password)


            elif var1.get() == 1 and var2.get()== 1 and var3.get()== 1 and var4.get() == 0:
                password = "".join(random.sample(upper_case + lower_case + numbers, passwordlength))
                code.config(text=password)


            elif var1.get() == 1 and var2.get()== 1 and var3.get()== 0 and var4.get() == 1:
                password = "".join(random.sample(upper_case + lower_case + chars, passwordlength))
                code.config(text=password)



            elif var1.get() == 1 and var2.get()== 1 and var3.get()== 0 and var4.get() == 0:
                password = "".join(random.sample(upper_case + lower_case, passwordlength))
                code.config(text=password)


            elif var1.get() == 1 and var2.get()== 0 and var3.get()== 1 and var4.get() == 1:
                password = "".join(random.sample(upper_case + numbers + chars, passwordlength))
                code.config(text=password)



            elif var1.get() == 1 and var2.get()== 0 and var3.get()== 1 and var4.get() == 0:
                password = "".join(random.sample(upper_case + numbers , passwordlength))
                code.config(text=password)



            elif var1.get() == 1 and var2.get()== 0 and var3.get()== 0 and var4.get() == 1:
                password = "".join(random.sample(upper_case + chars, passwordlength))
                code.config(text=password)



            elif var1.get() == 1 and var2.get()== 0 and var3.get()== 0 and var4.get() == 0:
                password = "".join(random.sample(upper_case, passwordlength))
                code.config(text=password)



            elif var1.get() == 0 and var2.get()== 1 and var3.get()== 1 and var4.get() == 1:
                password = "".join(random.sample(upper_case + lower_case + numbers + chars, passwordlength))
                code.config(text=password)



            elif var1.get() == 0 and var2.get() == 1 and var3.get() == 1 and var4.get() == 0:
                password = "".join(random.sample(lower_case + numbers, passwordlength))
                code.config(text=password)



            elif var1.get() ==0 and var2.get()== 1 and var3.get()== 0 and var4.get() == 1:
                password = "".join(random.sample(lower_case + chars, passwordlength))
                code.config(text=password)


            elif var1.get() == 0 and var2.get()== 1 and var3.get()== 0 and var4.get() == 0:
                password = "".join(random.sample(lower_case, passwordlength))
                code.config(text=password)



            elif var1.get() == 0 and var2.get()== 0 and var3.get()== 1 and var4.get() == 1:
                password = "".join(random.sample(numbers + chars, passwordlength))
                code.config(text=password)



            elif var1.get() == 0 and var2.get() == 0 and var3.get() == 1 and var4.get() == 0:
                if passwordlength >= 11:
                    code.config(text='The number length should be less than 10')
                else:
                    password = "".join(random.sample(numbers , passwordlength))
                    code.config(text=password)


            elif var1.get() == 0 and var2.get()== 0 and var3.get()== 0 and var4.get() == 1:
                global pass1
                password = "".join(random.sample(chars, passwordlength))
                code.config(text=password)


            elif var1.get() == 0 and var2.get()==0 and var3.get()==0 and var4.get() == 0:
                code.config(text="You should select at least 1 character")

        # If the user does not select the recommended password length
        else:
            code.config(text="You should input password length between 4 and 20")

    # Handling errors
    except:
        code.config(text="There was an error")

# Function to copy the password to a clipboard
def copy():
    global pass1
    pass1 = code.cget('text')
    window.clipboard_clear()
    window.clipboard_append(pass1)




# User interface

window = Tk()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

# Size of the window
window.geometry("700x200")


# Input length of password
Label(window, text='Length of password:').grid(row=0, padx=10, sticky='W')
e = Entry(window)
e.grid(row=0, column=1, sticky='W')


# Check box to select characters to include in password
Label(window, text='Characters to include:').grid(row=1, padx=10)
c1 = Checkbutton(window, text='Upper case', variable=var1, onvalue=1, offvalue='0').grid(row=2, column=0, padx=10, sticky='W')
c2 = Checkbutton(window, text='Lower case', variable=var2, onvalue=1, offvalue='0').grid(row=3, column=0, padx=10, sticky='W')
c3 = Checkbutton(window, text='Numbers', variable=var3, onvalue=1, offvalue='0').grid(row=4, column=0, padx=10, sticky='W')
c4 = Checkbutton(window, text='Special Characters', variable=var4, onvalue=1, offvalue='0').grid(row=5, column=0, padx=10, sticky='W')



# Call the generate password function using a button
Button(window, text='Generate Password', command=generate).grid(row='7', column='1', sticky='W')

# Display the password in a text field
code = Label(window, bg='white', width=50, text='Password')
code.grid(row='7', column='3', sticky='W', pady=10)


# Button to copy the code to clipboard
Button(window, text='Copy', command=copy).grid(row='7', column='2', sticky='W')


window.mainloop()
