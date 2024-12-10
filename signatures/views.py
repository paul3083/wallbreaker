from django.shortcuts import render, redirect
from django.http import HttpResponse

# 더미 데이터
dummy_data = [
    {
        "id": 1,
        "title": "이정우 놀리기",
        "description": "5반에서 문제가 많은 이정우 놀리기 서명에 참여해 주세요",
        "current_signatures": 1000,
        "target_signatures": 4000,
        "end_date": "2024-12-10"
    },
    {
        "id": 2,
        "title": "이주영 놀리기",
        "description": "5반에서 문제가 많은 이주영 놀리기 서명에 참여해 주세요",
        "current_signatures": 2000,
        "target_signatures": 4000,
        "end_date": "2024-12-10"
    },
    {
        "id": 3,
        "title": "나제준 놀리기",
        "description": "5반에서 문제가 많은 나제준 놀리기 서명에 참여해 주세요",
        "current_signatures": 3000,
        "target_signatures": 4000,
        "end_date": "2024-12-10"
    },
    {
        "id": 4,
        "title": "윤희쌤 놀리기",
        "description": "5반에서 문제가 많은 윤희쌤 놀리기 서명에 참여해 주세요",
        "current_signatures": 4000,
        "target_signatures": 4000,
        "end_date": "2024-12-10"
    },
]

def main_page(request):
    hot_issues = dummy_data[:4]
    nearby_petitions = dummy_data[4:8]
    return render(request, 'main_page.html', {
        'hot_issues': hot_issues,
        'nearby_petitions': nearby_petitions,
    })

def detail_page(request, petition_id):
    petition = next((p for p in dummy_data if p["id"] == petition_id), None)
    return render(request, 'detail_page.html', {'petition': petition})

def sign_petition(request, petition_id):
    # POST 요청인지 확인
    if request.method == 'POST':
        petition = next((p for p in dummy_data if p["id"] == petition_id), None)
        if petition:
            # 현재 서명 수를 증가
            petition['current_signatures'] += 1
            # 서명 후 상세 페이지로 리다이렉트
            return redirect('detail_page', petition_id=petition_id)
        return HttpResponse("Petition not found", status=404)
    return HttpResponse("Invalid request", status=400)