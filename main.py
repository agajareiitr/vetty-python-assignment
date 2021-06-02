from os import abort
from flask import Flask,render_template,request

app = Flask(__name__,template_folder="template")

allfilenames = ["file1","file2","file3","file4"] # names of all fiiles

@app.route("/",methods = ['GET'])
@app.route("/<filename>/",methods = ['GET'])
@app.route("/<filename>/<int:firstnum>-<int:secondnum>/",methods = ['GET'])

# By default the filename is file1, firstnum is the start line number and secondnum is the end line number

def index(filename="file1",firstnum=None,secondnum=None):
    if filename in allfilenames:
        filename = filename+".txt"
        fileLines = []

        # Opening the file requested, read all lines and appends it to a array filelines:
        with open(filename,'r',encoding='utf-8',errors='ignore') as file:
            for line in file.readlines():
                fileLines.append(line)
    
        file.close() # closed the file
        
        if firstnum==None or firstnum>len(fileLines):
            firstnum = 0 
        if secondnum==None or secondnum > len(fileLines):
            secondnum = len(fileLines)
        # the above 4 lines of code ensures not to throw error if the range given if more than len of file lines
        # and in index.html theres a simple if statement checks if end line number is greater than start line number
        # however 
        if firstnum==0 and secondnum==len(fileLines):
            linenumber= False
        else:
            linenumber = True
        # the above 4 lines tells when to say all lines and when to print the start and end line numbers.

        return render_template("main.html",lines=fileLines[firstnum:secondnum+1],firstnum=firstnum,filename=filename,secondnum=secondnum,linenumber=linenumber)

    else:
        return page_not_found(404) # this will throw error on file_not_found
        
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html") , 404


if __name__=="__main__":
    app.run(debug=True)