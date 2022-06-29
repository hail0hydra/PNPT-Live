# Starts !!!

<br>
<br>

>### Learning Python

<br>

- We've covered some `scripting`, now we are looking at `coding`.
<br>

- We download `exploits` off of the internet but we need to __Understand__ it first 

<br>

- `mkdir python` !!!

<br>

- Now some stuffs:

    ```python
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ cat first.py   
    #!/usr/bin/python3

    # Print tring
    print("Hello, World!")


                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ python3 first.py          
    Hello, World!
                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$
    ```

    First python program

    <br>

    - Now ;

    ```python
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ cat first.py 
    #!/usr/bin/python3

    # Print tring
    print("Hello, World!")

    print('Hello, world!')

    print("""This string runs multiple 
            lines""")


    print("This string is "+"awesome!")


                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ python3 first.py
    Hello, World!
    Hello, world!
    This string runs multiple 
            lines
    This string is awesome!
                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$
    ```

    let's do some other things
    <br>

    Maths now:

    ```python
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ cat first.py
    #!/usr/bin/python3

    # Print tring
    print("Hello, World!") #double quotes

    print('Hello, world!') #single quotes

    print("""This string runs multiple 
            lines""") # triple quotes for multiple lines


    print("This string is "+"awesome!")

    print("\n") # new line

    # MATH

    print(50+50) #add
    print(50-50) #subtract
    print(50 *50) #multiply
    print(50/50) #divide


                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ python3 first.py
    Hello, World!
    Hello, world!
    This string runs multiple 
            lines
    This string is awesome!


    100
    0
    2500
    1.0
                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$
    ```


    Still doing some of the things

    ```python
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ cat first.py 
    #!/usr/bin/python3

    # Print string
    print("Hello, World!") #double quotes

    print('Hello, world!') #single quotes

    print("""This string runs multiple 
            lines""") # triple quotes for multiple lines


    print("This string is "+"awesome!")

    print("\n") # new line



    # MATH

    print(50+50) #add
    print(50-50) #subtract
    print(50 *50) #multiply
    print(50/50) #divide
    print(50+50 - 50*50 /  50) #BODMAS
    print(50**2) #exponents
    print(50%6) # modulo - remainder
    print(50/6)
    print(50//6) #Quotient - division with no leftovers


    # Variables and methods
    quote = "All is fair in love and war"
    print(quote)

    # A method is a functions avialable for given object. we are talking about bbuilt-ins

    print(quote.upper())
    print(quote.lower())
    print(quote.title())
    print(len(quote))
                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ python3 first.py
    Hello, World!
    Hello, world!
    This string runs multiple 
            lines
    This string is awesome!


    100
    0
    2500
    1.0
    50.0
    2500
    2
    8.333333333333334
    8
    All is fair in love and war
    ALL IS FAIR IN LOVE AND WAR
    all is fair in love and war
    All Is Fair In Love And War
    27
                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$
    ```

    `ERROR` codes:

    ```python
    print(int(age))
    print(int(30.1))
    print(int(30.9))

    print("My name is "+name+" and I am "+age+" years old.")
                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ python3 first.py
    All is fair in love and war
    ALL IS FAIR IN LOVE AND WAR
    all is fair in love and war
    All Is Fair In Love And War
    27
    1337
    30
    30
    Traceback (most recent call last):
      File "/home/kali/Public/TCM/python/first.py", line 51, in <module>
        print("My name is "+name+" and I am "+age+" years old.")
    TypeError: can only concatenate str (not "int") to str
                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$
    ```

    What happened 

    ```python
    print("My name is "+name+" and I am "+str(age)+" years old.")

    age+=1

    print(age)
                                                                                    
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ python first.py           
    All is fair in love and war
    ALL IS FAIR IN LOVE AND WAR
    all is fair in love and war
    All Is Fair In Love And War
    27
    1337
    30
    30
    My name is regx and I am 1337 years old.
    1338
    ```

    - `Functions`

    ```python
    # Functions

    print('\n')

    print("Here is an example function")

    def whoami():  # this is a function
        name = "regx"
        age = "1337"
        print("My name is "+ name + " and I am "+str(age)+" years old.")

    whoami()
                                                                                       
    ┌──(kali㉿kali)-[~/Public/TCM/python]
    └─$ python first.py


    Here is an example function
    My name is regx and I am 1337 years old.
    ```


<br>
<br>

- Ok the whole program will be saved as a file.


<br>

- Look at a `Truth Table` online. example search `python truth table`


<br>
<br>

>Ends
