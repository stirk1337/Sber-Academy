from django.shortcuts import render
from .models import Vacancy
from tests.models import Test, Question
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import random
import ast
# Create your views here.
def browse(request):
    return render(request, 'vacancy/vacancy.html')

def get_vacancies(request):
    vac = Vacancy.objects.all()
    vac = list(vac.values())
    return JsonResponse(vac, safe=False)

def test(request, vacancy_id):
    vac = Vacancy.objects.get(id=vacancy_id)
    return JsonResponse(model_to_dict(vac))

def start_test(request):
    vac = Vacancy.objects.get(id=request.GET.get('vacancy_id'))
    skills = vac.skill_set.all()
    q_list = []
    test_xd = Test(name='На вакансию ' + vac.name, random=True, skill='Net', description='Тест оценит ваши знания на вакансию ' + vac.name )
    test_xd.save()
    for skill in skills:
        tests = Test.objects.all().filter(skill=skill.skill)
        for test in tests:
            questions = test.question_set.all()
            for question in questions:
                q_list.append({'question': question.question, 'opt1': question.opt1, 'opt2': question.opt2, 'opt3': question.opt3, 'opt4': question.opt4, 'right': question.right, 'skill': skill.skill})
    
    random_list = random.sample(q_list, min(len(skills)*10, len(q_list)))
    for q in random_list:
        question = Question(question=q['question'],
                            opt1=q['opt1'],
                            opt2=q['opt2'],
                            opt3=q['opt3'],
                            opt4=q['opt4'],
                            right=q['right'],
                            skill=q['skill'],
                            test=test_xd)
        question.save()
    test_dict = model_to_dict(test_xd)
    test_dict['questions'] = random_list
    return JsonResponse(test_dict)

def complete_test(request):
    test = Test.objects.get(id=request.GET.get('test_id'))
    answers = request.GET.get('answers').split(',')
    test_dict = model_to_dict(test)
    questions = test.question_set.all()
    rights = 0
    rights_dict = {}
    all_skills_dict = {}
    for i, q in enumerate(questions):
        if q.skill not in all_skills_dict:
            all_skills_dict[q.skill] = 1
        else:
            all_skills_dict[q.skill] += 1
        if str(q.right) == str(answers[i]):
            if q.skill not in rights_dict:
                rights_dict[q.skill] = 1
            else:
                rights_dict[q.skill] += 1
    print(rights_dict)
    print(all_skills_dict)
    for key,val in rights_dict.items():
        rights_dict[key] = int(val / all_skills_dict[key]) * 100
    #points = int(rights / len(questions) * 100)
    print(rights_dict)
    return JsonResponse(rights_dict, safe=False)