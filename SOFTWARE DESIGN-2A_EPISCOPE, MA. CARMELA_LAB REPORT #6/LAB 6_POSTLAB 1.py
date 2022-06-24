import Tkinter
def CelsiusToFahenheit (Celsius, entry): #function for CelsiusToFahenheit
    # #Celsius = int(input ("Enter a temperature in Celsius: "))
    Fahrenheit = 9.0/5.0 * float (Celsius) + 32
    entry.delete (0, 'end')
    entry.insert(0, str(Fahrenheit))


def FahenheitToCelsius (Fahrenheit, entry):

    Celsius = (float (Fahrenheit) - 32) * 5.0/9.0
    entry.delete (0, 'end')
    entry.insert(0, str(Celsius))

def main():
    window = Tkinter.Tk () # Creating main window
    window.title("Grid")
    lb = Tkinter.Label (window, text='Fahrenheit') # Creating label
    lb.grid (row=0,column=0)
    lb1=Tkinter.Label (window, text='Celsius:') # Creating label
    lb1.grid (row=0, column=1)
    en =Tkinter. Entry (window, justify='right') # Creating text field
    en.grid(row=1, column=0)
    en.insert(0, "32.0")
    en1=Tkinter.Entry (window, justify='right') # Creating text field
    enl.grid(row=1, column=1)
    enl.insert (0, "0.0")
    btnFtoc =Tkinter. Button (window, text='>>>>', command=lambda: FahenheitToCelsius (en.get(), en1))
    btnFtoc.grid(row=2, column=0)
    btnCtoF =Tkinter. Button (window, text='<<<<<', command=lambda: CelsiusToFahenheit(enl.get(), en))
    btnCtoF.grid(row=2, column=1)
    window.mainloop() # Running the application
if __name__ == 'main':
    main()
