from flask import Flask,render_template,request

app = Flask(__name__,template_folder="template")
@app.route("/")
@app.route("/<filename>/")
# def show_all(filename="file1"):
#     filename = filename+".txt"
#     fileLines = []
#     i=0
#     with open(filename,'r') as file:
#         for line in file.readlines():
#             fileLines.append(line)
#             i+=1
#     file.close()
#     return render_template("index.html",data=fileLines,filename=filename)
@app.route("/<filename>/<int:firstnum>-<int:secondnum>/")
def hello_world(filename="file1",firstnum=0,secondnum=99999):
    filename = filename+".txt"
    fileLines = []
    i=0
    with open(filename,'r') as file:
        for line in file.readlines():
            fileLines.append(line)
            i+=1    
    file.close()
    
    if firstnum>len(fileLines):
        firstnum = 0
    if secondnum > len(fileLines):
        secondnum = len(fileLines)

    if firstnum and secondnum:
        linenumber= True
    else:
        linenumber = False

    return render_template("index.html",data=fileLines[firstnum:secondnum+1],firstnum=firstnum,filename=filename,secondnum=secondnum,linenumber=linenumber)

if __name__=="__main__":
    app.run(debug=True)