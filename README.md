# Project Meme Generator

In this project, we shall use Python to build a "Meme generator"
The generator shall be able to run as "CLI" and web mode.
In "CLI" mode you should give necessary parameters to generate a meme which is under src/tmp
In web mode you are able to use the button random to generate a random meme.
In web mode you are able to input url, body and text to generate a meme.

# Instructions about the project

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, 
including an image with an overlaid quote. It’s not that simple though! Your content team spent countless hours writing quotes in a variety of filetypes. 
You could manually copy and paste these quotes into one standard format. You’re going to over-engineer a solution to load quotes from each file to show
off your fancy new Python skills.

## Set up a cross development environment for the project

Since we need some modules which shall be installed in Linux, I build a cross development environment.

- Ubuntu: for instance 18.04 (linux version 5.4.0)
- Python version: python-3.6.9
- VMware Workstation version: 16.1.2 
- Share development folder between Linux and Windows
- python virtual environment is welcome, but not a must.
- Install an IDE like Pycharm to edit 

Goal:
- Edit the code in IDE Pycharm on Windows
- Execute/run code in Linux (virtual machine)
 
### Commands to install python on Linux

- On a new installed Linux python2 or 3 is not installed. To install it we use the command "sudo apt install python3.6" 
- To execute a python file we have to use "python3 xxx.py".

### Necessary Python modules to install

Before you use pip3 to install the modules, you have to ensure that pip3 is installed
- input "pip3" on terminal and see if it can be recognized
- if not, then use "sudo apt install pip3"
- Do not use pip install since pip is only for python 2. Instead of it you have to use "pip3 install xxxxx" to install Libs.

For Doc style and code style test :
- pip3 install pycodestyle:  using pycodestyle you can check the code style
- pip3 install pydocstyle:   using pydocstyle you can check the document style in your code.  

The requirements.txt is supplied on top level of the project:
- certifi==2021.10.8
- charset-normalizer==2.0.7
- click==8.0.3
- dataclasses==0.8
- Flask==2.0.2
- idna==3.3
- importlib-metadata==4.8.2
- itsdangerous==2.0.1
- Jinja2==3.0.3
- lxml==4.6.4
- MarkupSafe==2.0.1
- numpy==1.19.5
- pandas==1.1.5
- Pillow==8.4.0
- pkg_resources==0.0.0
- python-dateutil==2.8.2
- python-docx==0.8.11
- pytz==2021.3
- requests==2.26.0
- six==1.16.0
- typing_extensions==4.0.0
- urllib3==1.26.7
- Werkzeug==2.0.2
- zipp==3.6.0
Before you install the requirements.txt you have to ensure that the pip is latest. Please update the pip using "python -m pip install --upgrade pip"
Then use the command "pip install -r requirements.txt" to install all neccessary modules.


Trouble Shooting during install the tools:
- You may meet the message "The headers or library files could not be found for zlib, a required dependency when compiling Pillow from source."
  during install Pillow, please try to use "pip3 uninstall Pillow" at firstif you have already installed it, then upgrade pip3 using "python3 -m pip install -U --force-reinstall pip".
  Then use "pip3 install Pillow" to install the latest Pillow

## Sub Module instruction:

### QuoteEngine - This package includes following sub modules: 

- __init__
- QuoteModel
- IngestorInterface
- CSVIngestor
- DocxIngestor
- PDFIngestor
- TextIngestor
- Ingestor

- QuoteModel contains a basic model which supplies two attributes 'body' and 'author'. You can reference the document with .csv, .docx, .pdf and .txt
  to get the information.

- IngestorInterface contains an abstract class/interface about parse kinds of format files like .csv, .docx, .pdf and .txt.
  The method can_ingest checks if a given file can be parsed or not.
  You will use a strategy design pattern to parse kinds of files.

- CSVIngestor supplies a strategy object which is inherited from IngestorInterface. It supplies a detailed method to parse .csv file, and use QuoteModel to 
  instantiate the objects and save them into a quote list.

- DocxIngestor supplies a strategy object which is inherited from IngestorInterface. It supplies a detailed method to parse .docx file, and use QuoteModel to 
  instantiate the objects and save them into a quote list.

- PDFIngestor supplies a strategy object which is inherited from IngestorInterface. It supplies a detailed method to convert the PDF format to a txt file, 
  then parse the txt file and use QuoteModel to instantiate the objects and save them into a quote list. 

- TextIngestor supplies a strategy object which is inherited from IngestorInterface. It supplies a detailed method to parse .txt file, and use QuoteModel to 
  instantiate the objects and save them into a quote list.

- Ingestor is also inherited from IngestorInterface. It supplies the logic to seclect the file type which is compatible to the given file and parse it.


- QuoteModel :  
- '__init__' method: the constructor for the class. You will need to decide what arguments it should accept. If you make changes, you should also update the surrounding comments.
- '__repr__' method supplies a stylized string to be machine-readable.
- To get an object of QuoteModel: QuoteModel(body, author), body and author shall be type of string


- IngestorInterface: 
- can_ingest method: It checks if the extension of the given file can be parsed according to supported_file_type. It returns True if the given file can be parsed, or it returns False.
- parse: this interfaces shall be inherited and implemented in other class. This method shall return a list which has the QuoteModel as elements. 


- CSVIngestor:
- parse: It receives a filename (string) and checks if the given file is with format csv, if yes, then parse it and return a list which contains QuoteModel objects as elements.
- use example:  QuoteCSV.parse('DogQuotesCSV.csv')


- DocxIngestor:
- parse: It receives a filename (string) and checks if the given file is with format docx, if yes, then parse it and return a list which contains QuoteModel objects as elements.
- use example:  QuoteDocx.parse('DogQuotesDOCX.docx')


- PDFIngestor:
- parse: It receives a filename (string) and checks if the given file is with format pdf, if yes, then convert it to a txt file, parse it and return a list which contains QuoteModel objects as elements.
- use example:  QuotePDF.parse('DogQuotesPDF.pdf')


- TextIngestor:
- parse: It receives a filename (string) and checks if the given file is with format txt, if yes, then parse it and return a list which contains QuoteModel objects as elements.
- use example:  QuotePDF.parse('DogQuotesTXT.txt')


- Ingestor:
- parse: It defines a set of classes which shall be supported for parsing. It receives the path and check if the given file is with format defined, if yes, then parse it and return a list which contains QuoteModels as elements.
- use example:  Ingestor.parse('DogQuotesTXT.txt')


## MemeGenerator - This module includes following sub-modules: 

- MemeExceptionManager: It declares some self-defined exception classes
- MemeGenerator:  It supplies functionalities to generate meme
- MemeRandom: It supplies random function to get random parameters like location, color and font
              It supplies a class inherited from MemeRandomInterface. This class implements a kind of strategy to get random parameters
              You can extend another class parallel to it, and transfer it to MemeGenerator, then this strategy will be used. (Polymorphism)
- MemeRandomInterface: It supplies an abstract class. You can define a customized strategy class based on this interface.


### Functions

- check_image: it checks an image if it is valid, return True if it is valid
- use example: check_image('./_data/photos/Naruto/Sakura.jpg')


- get_random_mem_name: Since you will generate many memes, you should get a random name of meme and ensure there is no name conflict.
                        Output path is the path of the generated memes
- use example: get_random_mem_name('./static')


- make_meme: The function Image.alpha_composite will report a ValueError if the first image mode is RGB. So you have to convert it to RGBA then call the function.
             The width is an optional parameter. It shall be limited so that it should be too small or too large.
             Text and author are from the file with the format CSV, PDF, docx or txt.
             img_path is the path of the image as input, the name of the image shall be also included in img_path.
- use example: make_meme('./_data/photos/Naruto/Sakura.jpg', '"Youth has no end."', 'Sasori', 600)  
- use example: make_meme('./_data/photos/Naruto/Sakura.jpg', '"I understand because I lost."', 'Kakashi')  


- get_random_location: image_size is a tuple (width, height). 
                       body and author are from CSV, PDF, docx or txt file.
                       font_max_height_size is the maximal height of body and author
                       font_max_size is the maximal width of body and author
- use example: get_random_location((500, 500), '"I understand because I lost"', 'Kakashi', 40, 200)  


- get_random_color: Get random R, G, B for a color, returns a tuple (R,G,B,max_value)
- use example: get_random_color()


- get_random_font: font_path is the path of fonts with the format ttf
                   it returns the path and a random name of the font
- use example: get_random_font(./_data/Fonts)



## meme.py
- meme.py is located on a concrete application level. It receives command parameters from user and generate a meme.
- The parameters can be path, body and author. All of them are optional.
- path is the path of image. Body and author are from csv, pdf, txt and docx.
- after that it runs successfully you can find the meme in ./tmp.
- it also prints the output image path+name on the terminal.
- use example: python3 meme.py --path './_data/photos/Naruto/default.jpg' --body '"I understand because I lost"' --author 'Kakashi'


## app.py 
- app.py gives you a flask framework to generate meme on web.
- There are two optional ways to reach the goal, one way is to click the random button, then the image will be generated randomly.
- The other way is to input image url, body and author to generate a meme.
- meme_rand: this function picks one random image, body and author as inputs, then generate a meme. Flask will use render_template
  to add the new meme to the web page.
- meme_form: this function is to get the input parameters from user, image url, body and author.
- meme_post: this function is to response a 'post' request from the client/user. 'request' module supplies a method to get the posted
  parameter like url, body and author. The image on the url will be parsed and saved in an object. You write the object into a new image
  which will be used for creating meme. The temporary image shall be removed after that you use it to generate a meme.


## meme_email.py
- meme_email.py gives you a way to send an email via SMTP.
- It is designed using "builder" design pattern. Multiple inheritance simplifies the initial process and instantiate the email object.
- The building process has some builders' methods which supply the user a simple interface and developer an easy extension.
- If follows the OCP principle: Open for extension , closed for modification.
- This module combines with meme.py which writes the path of generated meme to a shared file. Meme_email.py will then read the shared file to get the path of the meme.
- For getting the meme you can use the subprocess to execute meme.py. The image path, body and author you should input one by one.
- For building an email you should input the parameters like : Sender, Sender Password, Receiver, Server name of SMTP, Port, Content of email, attachment of email, message.
- After sending the email, the temporary files shall be removed.
- The email Receiver and Sender shall both support SMTP. You can use gmail for SMTP, but you need a configuration. You can reference this link : https://kb.synology.com/en-ca/SRM/tutorial/How_to_use_Gmail_SMTP_server_to_send_emails_for_SRM.
- use example: "python3 meme_email.py  'shaguarhan123@gmail.com' 'shaguarhan1234@gmail.com' --server 'smtp.gmail.com'  'Email Title' 'Hello'"
- use example explanation: 'shaguarhan123@gmail.com' is sender, 'shaguarhan1234@gmail.com' is receiver, 'smtp.gmail.com' is server name, 'Email Title' is title of email, 'Hello' is content.


## Unit Test
- The unit test covers the modules which include functions/classes.
- For the test the unittest module of python is in use.
- the following modules were tested: CSVIngestor, DocxIngestor, Ingestor, IngestorInterface, MemeGenerator, MemeRandom, PDFIngestor, QuoteModel, TextIngestor
