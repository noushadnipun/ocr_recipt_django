# Create your views here.
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ReceiptForm
from .models import Receipt

from ocr_project.receipt.ocr.main import  process_receipt_image  # Adjust the import based on your OCR file structure
#from ocr_project.receipt.ocr.main import pytesseract
def upload_receipt(request):
    if request.method == 'POST':
        image_path = 'media/receipts/my.jpg'
        myImg = process_receipt_image(image_path)
        # return HttpResponse(request.FILES)
        return JsonResponse(json.loads(myImg))
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            receipt = form.save()

            # Call the OCR function
            receipt_path = receipt.image.path
            ocr_result = process_receipt_image(receipt_path)
            return HttpResponse(ocr_result)
            # Save OCR data to the database
            receipt.extracted_data = ocr_result
            receipt.save()
            
            return redirect('receipt_detail', receipt_id=receipt.id)
    else:
        form = ReceiptForm()
    return render(request, 'receipt/upload.html', {'form': form})

def receipt_detail(request, receipt_id):
    # Fetch the receipt object from the database
    receipt = get_object_or_404(Receipt, id=receipt_id)
    
    # Pass the receipt data to the template
    context = {'receipt': receipt}
    return render(request, 'receipt_detail.html', context)