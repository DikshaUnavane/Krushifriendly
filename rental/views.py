from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipmentForm , BookingForm
from .models import Equipment ,Booking
from django.core.files.base import ContentFile
import base64
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RenterForm
from .models import Renter
from django.shortcuts import render
import random
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


def add_renter(request):
    if request.method == 'POST':
        form = RenterForm(request.POST)
        lat = request.POST.get('latitude')
        lng = request.POST.get('longitude')
        if form.is_valid() and lat and lng:
            renter = form.save(commit=False)
            renter.latitude = lat
            renter.longitude = lng
            renter.save()
            return redirect('add_renter')
    else:
        form = RenterForm()
    return render(request, 'rental/add_renter.html', {'form': form})


def track_booking(request):
    # Default warehouse location (set once, no manual input needed later)
    base_lat = 20.005  # Example city center
    base_lng = 73.778

    # Auto-generate tool location nearby (within 0.02° ~ 2 km)
    tool_lat = base_lat + random.uniform(-0.02, 0.02)
    tool_lng = base_lng + random.uniform(-0.02, 0.02)

    context = {
        'tool_lat': tool_lat,
        'tool_lng': tool_lng,
    }
    return render(request, 'rental/track_booking.html', context)

def step6_view(request):
    return render(request, 'rental/step6.html')