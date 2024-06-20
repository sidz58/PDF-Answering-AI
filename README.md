# Project Overview:
We must build an AI application that takes in our own PDF as an input and responds to our queries about the same. Our task
is to create a model leveraging the concepts of Natural Language
Processing and generate/ extract relevant answers from the PDF file that
we uploaded, without the use of an API. This project involves getting familiar with transformers and their architecture and shows how a working model can be deployed on a Web Application, using Python, Flask and HTML.

## Installation Instructions
>https://github.com/sidz58/PDF-Answering-AI.git

* Using the URL (given above) to this repository, go ahead and clone it onto your system. Because this project involves multiple languages, it is best to run these programs via VS Code.

* **Important:** To install ***ANY*** package on VS Code, it is necessary to set up a **virtual environment** in the same folder that you cloned this repo into. Refer to this video link:
_https://www.youtube.com/watch?v=GZbeL5AcTgw_
* Install the packages by using the **pip** program. **Refer to the end of this file to find the relevant versions of the packages to insure compatibility**. 
* If you have a newer version of the packages mentioned please downgrade it by using the **pip uninstall** command.

* To access the web application, please run the **WebApp.py** program. You will find a URL which will be hosted locally. **CTRL + Click** to launch the web app.

## Usage:
It is fairly simple to use the application. Once you open up the web application you fill find a box, where you can input the query you want to ask based on the PDF you are going to upload. 

After this, proceed to upload the PDF by clicking on the "Upload PDF" button. Once you have uploaded your file, your file name will be displayed next to this box.

Next, press the "Submit and predict" button to display the extracted answer for your PDF!

## Dependancies
* Python
* Pytorch - Version 2.2.1
* **Important:** Numpy -  Version 1.26.4
* Flask - Version 3.0.3
* Transformers - Version 4.41.2





