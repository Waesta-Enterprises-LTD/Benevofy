from django.shortcuts import render
from .models import Pledge
from django.urls import reverse
from Events.models import PersonalEvent
from .forms import PledgeForm
from django.core.paginator import Paginator
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import qrcode
from django.http import FileResponse
 


def view_pledges(request, event_id):
    event = PersonalEvent.objects.get(id=event_id)
    return render(request, 'benevofy/view_pledges.html', {'event': event})


def pledge(request, event_id):
    event = PersonalEvent.objects.get(id=event_id)
    form = PledgeForm()
    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            form.instance.event = event
            pledge = form.save()
            image = Image.open('pledge_card.jpg')
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('ch.ttf', 70)
            names = form.cleaned_data.get('names')
            email = form.cleaned_data.get('email')
            amount = form.cleaned_data.get('amount')
            phone = form.cleaned_data.get('phone')
            due_date = form.cleaned_data.get('due_date')
            draw.text((1500, 323), f"{names}", font=font, fill=(0, 0, 255))
            draw.text((1580, 484), f"{phone}", font=font, fill=(0, 0, 255))
            draw.text((1530, 620), f"{amount} UGX", font=font, fill=(0, 0, 255))
            draw.text((1550, 774), f"{due_date.strftime('%d/%m/%Y')}", font=font, fill=(0, 0, 255))
            draw.text((2830, 774), f"{event.event_date.strftime('%d/%m/%Y')}", font=font, fill=(0, 0, 255))

            # Create QR code
            qr = qrcode.QRCode(
                version=3,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            pay_link = f"http://{request.META['HTTP_HOST']}{reverse('contribute_to_personal_event', args=[event.id])}"
            qr.add_data(pay_link)
            qr.make(fit=True)

            # Generate QR code image
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Add QR code to the image
            qr_width, qr_height = qr_image.size
            image_width, image_height = image.size
            qr_x = image_width - qr_width - 10
            qr_y = image_height - qr_height - 10
            image.paste(qr_image, (qr_x, qr_y))

            card_path = f'{names}-pledge_card.jpg'
            card_io = BytesIO()
            image.save(card_io, format='JPEG')
            card_io.seek(0)
            return FileResponse(card_io, as_attachment=True, filename=card_path)
    return render(request, 'benevofy/pledge.html', {'event': event, 'form': form})

    