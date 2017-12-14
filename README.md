# diary / 하루 세 줄, 마음정리법

## 20171213
포트폴리오 시작  
1. 라이브러리 설치 [참조](https://libsora.so/posts/good-django-library/)
- smarturls // 플라스크 형식의 URL Route
- django-extensions
- werkzeug // 보기 쉬운 디버거
2. c드라이브의 가상환경을 복사했더니 라이브러리 설치가 그쪽으로 돼서 복붙해야함
#### 해야 할 것
1. 유저 모델 / 포스트 모델 / 코멘트 모델 / 태그 모델 설계
2. url 정책 세우기
#### 새로 안 것
1. smarturls 사용법

        from smarturls import surl

    urls.py 파일에 임포트한다

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
        ]

        urlpatterns = [
            surl('admin/', admin.site.urls),
        ]
    surl을 사용하고 r과^ 삭제

    만드신 분 홈페이지가 접속이 안 돼서 난감했는데 해결했다
---
## 20171214
1. 포스트 모델 생성