import json
from django.shortcuts import render

def load_quizzes_from_json():
    with open('questions/static/quizzes.json', 'r', encoding='utf-8') as f:
        quizzes = json.load(f)
    return quizzes

def quiz_list(request):
    quizzes = load_quizzes_from_json()
    return render(request, 'questions/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quizzes = load_quizzes_from_json()
    if quiz_id < 0 or quiz_id >= len(quizzes):
        return render(request, 'questions/404.html')

    quiz = quizzes[quiz_id]
    return render(request, 'questions/quiz_detail.html', {'quiz': quiz})

# from django.shortcuts import render

# # Simulated JSON data
# quizzes = [
#     {
#         "question": "∫dx/(16+x^2) dx=?",
#         "options": [
#             "1/4  tan^(-1)⟨x/4⟩+C",
#             "tan^(-1)⟨x/4⟩+C",
#             "4 tan^(-1)⟨x/4⟩+C",
#             "4 tan^(-1)⟨4x⟩+C"
#         ],
#         "correct_answer": "1/4  tan^(-1)⟨x/4⟩+C"
#     },
#     {
#         "question": "∫(sinxcosx)/(sin^4x+cos^4x) dx=?",
#         "options": [
#             "1/2  tan^(-1)⟨(tan^2x)⟩+C",
#             "sinx+cosx+C",
#             "1/2  tan^(-1)⟨(sin^2⟨x⟩)⟩",
#             "কোনটি নয়"
#         ],
#         "correct_answer": "1/2  tan^(-1)⟨(tan^2x)⟩+C"
#     }
# ]

# def quiz_list(request):
#     return render(request, 'questions/quiz_list.html', {'quizzes': quizzes})

# def quiz_detail(request, quiz_id):
#     quiz = quizzes[quiz_id]
#     return render(request, 'questions/quiz_detail.html', {'quiz': quiz})


# from django.shortcuts import render

# # Simulated JSON data with LaTeX formatting
# quizzes = [
#     {
#         "question": r"$$\int \frac{dx}{16+x^2} dx=?$$",
#         "options": [
#             r"$$\frac{1}{4} \tan^{-1}\left(\frac{x}{4}\right) + C$$",
#             r"$$\tan^{-1}\left(\frac{x}{4}\right) + C$$",
#             r"$$4 \tan^{-1}\left(\frac{x}{4}\right) + C$$",
#             r"$$4 \tan^{-1}(4x) + C$$"
#         ],
#         "correct_answer": r"$$\frac{1}{4} \tan^{-1}\left(\frac{x}{4}\right) + C$$"
#     },
#     {
#         "question": r"$$\int \frac{\sin x \cos x}{\sin^4 x + \cos^4 x} dx=?$$",
#         "options": [
#             r"$$\frac{1}{2} \tan^{-1}(\tan^2 x) + C$$",
#             r"$$\sin x + \cos x + C$$",
#             r"$$\frac{1}{2} \tan^{-1}(\sin^2 x)$$",
#             "কোনটি নয়"
#         ],
#         "correct_answer": r"$$\frac{1}{2} \tan^{-1}(\tan^2 x) + C$$"
#     }
# ]

# def quiz_list(request):
#     return render(request, 'questions/quiz_list.html', {'quizzes': quizzes})

# def quiz_detail(request, quiz_id):
#     quiz = quizzes[quiz_id]
#     return render(request, 'questions/quiz_detail.html', {'quiz': quiz})

