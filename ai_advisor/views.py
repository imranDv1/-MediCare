import google.generativeai as genai
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AIQueryForm
from .models import AIConsultation
from medicines.models import Medicine

@login_required
def ai_advisor(request):
    response_text = None
    consultation = None
    related_medicines = []

    if request.method == 'POST':
        form = AIQueryForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']

            try:
                genai.configure(api_key=settings.GEMINI_API_KEY)
                model = genai.GenerativeModel('gemini-2.5-flash')
                system_prompt = (
                    "You are a helpful medical assistant for a pharmacy. "
                    "Based on the patient's symptoms or situation, suggest suitable over-the-counter medicines, "
                    "their dosage, and any precautions. Always advise consulting a doctor for serious conditions. "
                    "Format your response in clear sections with headings."
                )
                full_prompt = f"{system_prompt}\n\nPatient symptoms: {symptoms}"

                ai_response = model.generate_content(full_prompt)
                response_text = ai_response.text

                consultation = AIConsultation.objects.create(
                    user=request.user,
                    query=symptoms,
                    response=response_text
                )

                keywords = symptoms.lower().split()
                medicine_query = Q()
                for keyword in keywords:
                    if len(keyword) > 3:
                        medicine_query |= (
                            Q(name__icontains=keyword) |
                            Q(generic_name__icontains=keyword) |
                            Q(category__name__icontains=keyword)
                        )
                if medicine_query:
                    related_medicines = Medicine.objects.filter(medicine_query)[:5]

            except Exception as e:
                messages.error(
                    request,
                    f'AI service error: {str(e)}. Please try again later.'
                )
                response_text = None
    else:
        form = AIQueryForm()

    return render(request, 'ai_advisor/ai_advisor.html', {
        'form': form,
        'response': response_text,
        'consultation': consultation,
        'related_medicines': related_medicines,
    })

@login_required
def consultation_history(request):
    consultations = AIConsultation.objects.filter(user=request.user)
    search = request.GET.get('search', '')
    if search:
        consultations = consultations.filter(query__icontains=search)
    return render(request, 'ai_advisor/consultation_history.html', {
        'consultations': consultations,
        'search': search,
    })

@login_required
def consultation_detail(request, pk):
    consultation = get_object_or_404(AIConsultation, pk=pk, user=request.user)
    return render(request, 'ai_advisor/consultation_detail.html', {
        'consultation': consultation,
    })
