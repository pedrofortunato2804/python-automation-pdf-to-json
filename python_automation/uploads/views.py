from django.shortcuts import render
from django.http import HttpResponse
from .convertion import make_convertion_pdf_to_json
import json
import os

def file_upload(request):
    if request.method == "POST":
        if "arquivo" not in request.FILES:
            return HttpResponse("Nenhum arquivo enviado.")

        pdf_file = request.FILES["arquivo"]
        path_temp = os.path.join("uploads/temp_files/", pdf_file.name)
        
        with open(path_temp, "wb+") as des:
            for chunk in pdf_file.chunks():
                des.write(chunk)

        response = make_convertion_pdf_to_json(pdf_file = pdf_file)

        os.remove(path_temp)

        json_str = response.output[1].content[0].text
        json_data = json.loads(json_str)

        json_filename = "output.json"
        json_path = os.path.join("media", json_filename)

        with open(json_path, "w", encoding = "utf-8") as f:
            json.dump(json_data, f, ensure_ascii = False, indent = 2)
        
        return render(request, 'uploads/success.html', {
            "json_filename": json_filename,
        })
    return render(request, "uploads/index.html")
