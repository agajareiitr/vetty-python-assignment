from flask import Flask,render_template,request

app = Flask(__name__,template_folder="template")

@app.route("/",methods = ['GET'])
@app.route("/<filename>/",methods = ['GET'])
@app.route("/<filename>/<int:firstnum>-<int:secondnum>/",methods = ['GET'])

# By default the filename is file1, firstnum is the start line number and secondnum is the end line number
def hello_world(filename="file1",firstnum=0,secondnum=99999):
    filename = filename+".txt"
    fileLines = []

    # Opening the file requested, read all lines and appends it to a array filelines:
    with open(filename,'r',encoding='utf-8',errors='ignore') as file:
        for line in file.readlines():
            fileLines.append(line)
  
    file.close() # closed the file
    
    if firstnum>len(fileLines):
        firstnum = 0 
    if secondnum > len(fileLines):
        secondnum = len(fileLines)
    # the above 4 lines of code ensures not to throw error if the range given if more than len of file lines
    # and in index.html theres a simple if statement checks if end line number is greater than start line number

    if firstnum==0 and secondnum==len(fileLines):
        linenumber= False
    else:
        linenumber = True
    # the above 4 lines tells when to say all lines and when to print the start and end line numbers.

    return render_template("index.html",lines=fileLines[firstnum:secondnum+1],firstnum=firstnum,filename=filename,secondnum=secondnum,linenumber=linenumber)

if __name__=="__main__":
    app.run(debug=True)