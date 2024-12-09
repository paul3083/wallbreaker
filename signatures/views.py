from django.shortcuts import render

# 더미 데이터
dummy_data = [
    {
        "id": 1,
        "title": "Petition 1",
        "description": "Description for Petition 1",
        "current_signatures": 2000,
        "target_signatures": 4000,
        "end_date": "2024-12-10"
    },
    {
        "id": 2,
        "title": "Petition 2",
        "description": "Description for Petition 2",
        "current_signatures": 1500,
        "target_signatures": 3000,
        "end_date": "2024-12-20"
    },
    # 추가 데이터
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