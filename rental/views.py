from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipmentForm , BookingForm
from .models import Equipment ,Booking
from django.core.files.base import ContentFile
import base64
from django.contrib import messages

def home(request):
    return render(request, 'rental\step6.html')

def tools(request):
    return render(request, 'rental/tools.html')

def seeds(request):
    return render(request, 'rental/seeds.html')

# def seedlings(request):
#     return render(request, 'seedlings.html')

def about(request):
    return render(request, 'rental/about.html')  # Ensure about.html exists

def login_view(request):
    return render(request, 'rental/login.html') 

def forgot_password(request):
    return render(request, 'rental/fp.html') 

def create_account(request):
    return render(request, 'rental/new_account.html')

def upload_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)

        # Handle captured image
        captured_image_data = request.POST.get('captured_image')
        if captured_image_data:
            format, imgstr = captured_image_data.split(';base64,')  
            ext = format.split('/')[-1]  
            image_data = ContentFile(base64.b64decode(imgstr), name=f"captured_image.{ext}")

            equipment = Equipment(
                name=request.POST['name'],
                price=request.POST['price'],
                image=image_data  # Save captured image
            )
            equipment.save()
            return redirect('equipment_list')

        if form.is_valid():
            form.save()
            return redirect('equipment_list')

    else:
        form = EquipmentForm()

    return render(request, 'rental/upload.html', {'form': form})

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'rental/equipment_list.html', {'equipments': equipments})

def rent_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    return render(request, 'rental/rent_equipment.html', {'equipment': equipment})

def calendar_booking(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    bookings = Booking.objects.filter(equipment=equipment)
    form = BookingForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            booking = form.save(commit=False)
            booking.equipment = equipment
            booking.user = request.user  # Ensure the user is logged in
            booking.save()
            messages.success(request, "Booking successful!")
            return redirect('equipment_list')  # Redirect to equipment list

    return render(request, 'rental/calendar_booking.html', {
        'equipment': equipment,
        'form': form,
        'bookings': bookings
    })

def payment_page(request, equipment_id):
    return render(request, 'rental/payment.html')

def payment2_view(request):
    return render(request, 'rental/payment2.html')

def search_equipment(request):
    query = request.GET.get('q', '')  # Get search query
    equipment_list = Equipment.objects.filter(name__icontains=query) if query else []

    return render(request, 'rental/search_results.html', {'equipment_list': equipment_list, 'query': query})

def subscription1(request):
    return render(request, 'rental/subscription1.html')

def subscription2(request):
    return render(request, 'rental/subscription2.html')

def subscription3(request):
    return render(request, 'rental/subscription3.html')

def subscription4(request):
    return render(request, 'rental/subscription4.html')



# rental/views.py
import os
import time
import shutil
import traceback
from urllib.parse import quote as urlquote

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

# Import your ML prediction function
from .ml_models import predict_agri

# Default threshold for classifying as 'agri'
DEFAULT_THRESHOLD = 0.6


def _ensure_media_dirs():
    """Ensure MEDIA_ROOT and accepted subfolder exist. Return (media_root, accepted_dir)."""
    media_root = settings.MEDIA_ROOT
    accepted_dir = os.path.join(media_root, "accepted")
    os.makedirs(media_root, exist_ok=True)
    os.makedirs(accepted_dir, exist_ok=True)
    return media_root, accepted_dir


def _unique_filepath(folder, filename):
    """Return a filepath in folder for filename; append timestamp if it exists already."""
    base, ext = os.path.splitext(filename)
    dest = os.path.join(folder, filename)
    if not os.path.exists(dest):
        return dest
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    new_name = f"{base}_{timestamp}{ext}"
    return os.path.join(folder, new_name)


def save_uploaded_file(file_obj, dest_folder):
    """
    Save Django UploadedFile to dest_folder. Returns absolute path of saved file.
    """
    os.makedirs(dest_folder, exist_ok=True)
    dest_path = _unique_filepath(dest_folder, file_obj.name)
    with open(dest_path, "wb+") as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    return dest_path


# ---------- View for normal GET (renders HTML) ----------
def new_upload(request):
    """
    Render the upload page for GET request.
    """
    return render(request,'rental/new_upload.html')


# ---------- AJAX endpoint for prediction ----------
def predict_ajax(request):
    """
    Handle AJAX POST request from upload form and return JSON with prediction.
    """
    result = {"label": "unknown", "prob": 0.0, "preview_url": "", "saved_path": ""}

    if request.method == "POST":
        try:
            media_root, accepted_dir = _ensure_media_dirs()

            # Check if equipment image is uploaded
            if not request.FILES.get("equipment_image"):
                return JsonResponse({"error": "No image uploaded"}, status=400)

            uploaded_file = request.FILES["equipment_image"]

            # Save uploaded file
            saved_input_path = save_uploaded_file(uploaded_file, media_root)
            filename = os.path.basename(saved_input_path)

            # Run ML prediction
            label, prob = predict_agri(saved_input_path, threshold=DEFAULT_THRESHOLD)

            # If 'agri', copy to accepted folder
            saved_path = None
            if label == "agri":
                dest = _unique_filepath(accepted_dir, filename)
                shutil.copy(saved_input_path, dest)
                saved_path = dest

            # Build preview URL
            preview_url = settings.MEDIA_URL + urlquote(filename)

            # Prepare JSON response
            result = {
                "label": label,
                "prob": float(prob),
                "preview_url": preview_url,
                "saved_path": saved_path
            }

        except Exception as e:
            # Log the error on server
            traceback.print_exc()
            result = {"error": str(e)}

    return JsonResponse(result)
