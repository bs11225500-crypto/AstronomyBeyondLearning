from django.shortcuts import render, redirect
import random
import json
from pathlib import Path
from .models import QuizProgress


def load_questions():
    file_path = Path(__file__).resolve().parent / "questions.json"
    with open(file_path, "r") as f:
        return json.load(f)


def game(request):

    request.session.pop("questions", None)
    request.session.pop("score", None)
    request.session.pop("q_index", None)
    request.session.pop("last_game_score", None)

    return render(request, "games/game.html")



def multiple_choice_game(request):

    if request.GET.get("reset_quiz"):
        request.session.pop("questions", None)
        request.session.pop("score", None)
        request.session.pop("q_index", None)

        if request.GET.get("go_back"):
            return redirect("games:game")

    TOTAL = 5

    if "questions" not in request.session:
        all_q = load_questions()
        random.shuffle(all_q)
        request.session["questions"] = all_q[:TOTAL]
        request.session["score"] = 0
        request.session["q_index"] = 0

    questions = request.session["questions"]
    q_index = request.session["q_index"]
    score = request.session["score"]

    if request.GET.get("next"):
        request.session["q_index"] = q_index + 1
        return redirect("games:multiple_choice")


    if q_index >= TOTAL:

        if request.user.is_authenticated:
            progress, created = QuizProgress.objects.get_or_create(user=request.user)
            progress.last_score = score
            progress.attempts += 1
            if score > progress.best_score:
                progress.best_score = score
            progress.save()

        request.session["last_game_score"] = score

        return render(request, "games/mc_quiz.html", {
            "game_over": True,
            "score": score,
            "total": TOTAL })


   
    current = questions[q_index]

    if request.method == "POST":
        selected = request.POST.get("answer")
        correct = current["correct"]

        if selected == "NONE":
            return render(request, "games/mc_quiz.html", {
                "question": current,
                "feedback": True,
                "selected": None,
                "correct": correct,
                "correct_text": current["options"][correct],
                "index": q_index + 1,
                "score": score,
                "total": TOTAL,
                "show_next": True,
                "time_out": True
            })

        if selected == correct:
            request.session["score"] = score + 1

        return render(request, "games/mc_quiz.html", {
            "question": current,
            "feedback": True,
            "selected": selected,
            "correct": correct,
            "correct_text": current["options"][correct],
            "index": q_index + 1,
            "score": request.session["score"],
            "total": TOTAL,
            "show_next": True
        })

    return render(request, "games/mc_quiz.html", {
        "question": current,
        "score": score,
        "index": q_index + 1,
        "total": TOTAL
    })


def results(request):
    score = request.session.get("last_game_score") 
    total = 5

    leaderboard = QuizProgress.objects.order_by('-best_score')[:5]

    user_progress = None
    if request.user.is_authenticated:
        user_progress = QuizProgress.objects.filter(user=request.user).first()

    return render(request, "games/results.html", {
        "score": score,
        "total": total,
        "leaderboard": leaderboard,
        "user_progress": user_progress,
        "is_logged_in": request.user.is_authenticated,
    })

def leaderboard(request):
    players = QuizProgress.objects.order_by('-best_score')

    total_players = QuizProgress.objects.count()

    return render(request, "games/leaderboard.html", {
        "players": players,
        "total_players": total_players
    })
