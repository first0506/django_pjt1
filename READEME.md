1. 명세서의 프로젝트 구조는 base.html이 들어있는 templates 폴더가 django_pjt1 폴더 안에 있지 않고 밖에 나와있었다. 그렇기 때문에 처음에 `setting.py` 에서 `templates` 경로를 설정할 때 평소와 다르게 지정해야 했기 때문에 조금 어려웠다.
2. 전체 리뷰 목록 조회 중 `title` 을 클릭하면 해당 리뷰의 상세 조회로 이동해야했는데 `a tag` 안에 `{{}}`를 통해 pk를 넣어주는 과정에서 약간 애를 먹었다. 
3. redirect를 할 때 위에 `from django.shortcuts import redirect`를 써주는 것을 몰라 약간 헤맸었다.