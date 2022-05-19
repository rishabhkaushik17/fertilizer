from django.shortcuts import redirect, render
import joblib

def get_prediction(request):
    return render(request, 'fprediction.html')

def get_fertilizer_result(request):
    cls = joblib.load('fertilizer_model.sav')

    lis = []
    lis.append(request.POST.get('ca'))
    lis.append(request.POST.get('mg'))
    lis.append(request.POST.get('k'))
    lis.append(request.POST.get('s'))
    lis.append(request.POST.get('n'))
    lis.append(request.POST.get('lime'))
    lis.append(request.POST.get('c'))
    lis.append(request.POST.get('p'))
    lis.append(request.POST.get('moisture'))

    ans = str(cls.predict([lis]))
    s = ""
    s = s.join(ans)
    return render(request, 'fertilizer_result.html', {'ans': s})


