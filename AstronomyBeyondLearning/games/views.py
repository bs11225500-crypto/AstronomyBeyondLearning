from django.shortcuts import render, redirect
import random

def all_games(request):
    return render(request, "games/all_games.html")

def true_false_game(request):

    # RESET GAME
    if request.GET.get("reset"):
        request.session["score"] = 0
        request.session["question_number"] = 1

    facts = [
        {"statement": "Venus rotates backward compared to most planets.", "is_true": True},
        {"statement": "Mars has five moons.", "is_true": False},
        {"statement": "Jupiter is the largest planet in the solar system.", "is_true": True},
        {"statement": "The Sun is a planet.", "is_true": False},
    ]

    # Initialize score & question count
    if "score" not in request.session:
        request.session["score"] = 0
    if "question_number" not in request.session:
        request.session["question_number"] = 1

    MAX_QUESTIONS = 5

    # GAME OVER
    if request.session["question_number"] > MAX_QUESTIONS:
        return render(request, "games/true_false.html", {
            "game_over": True,
            "score": request.session["score"],
            "max": MAX_QUESTIONS
        })

    # Pick a random fact
    fact = random.choice(facts)

    user_answer = None
    result = None

    if request.method == "POST":

        # If time ended
        if request.POST.get("time_up") == "1":
            request.session["question_number"] += 1
            return redirect("games:true_false")

        # If user answered
        user_answer = request.POST.get("answer")
        correct_answer = "true" if fact["is_true"] else "false"
        result = (user_answer == correct_answer)

        # update score
        if result:
            request.session["score"] += 1

        request.session["question_number"] += 1

        return redirect("games:true_false")

    return render(request, "games/true_false.html", {
        "fact": fact,
        "score": request.session["score"],
        "question_number": request.session["question_number"],
        "max_questions": MAX_QUESTIONS,
        "game_over": False
    })
