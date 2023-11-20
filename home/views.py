from django.shortcuts import render
from .src import crawl_news
from . import models
from Crypto.Hash import SHA512

#####
#def make_hash():



######
#for uploadFile, append CRUD
def uploadFile_create(fileTitle, uploadedFile):
    #split with "."
    filename = uploadedFile.name.split('.')
    #check html
    if filename[-1] == "html":
        #Save in database
        document = models.Document(
                title=fileTitle,
                uploadedFile=uploadedFile
                )
        document.save()
        print("saved")
    else:
        print("save failed")
        pass

        #set url.py
       # with open('/playground/playground/urls.py') as file:
       #     code = file.read()
       # tree = ast.parse(code)
        
        

        


######
# Create your views here.
def main(request):
    datas = crawl_news.main()
    contexts = {"datas": datas}
    return render(request, 'main.html', contexts)

def test(request):
    return render(request, 'test.html')

def uploadFile(request):
    if request.method == "POST":
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        
        #upload DB, make page
        uploadFile_create(fileTitle, uploadedFile)
    
    documents = models.Document.objects.all()

    return render(request, "upload_file.html", context={
        "files": documents})






