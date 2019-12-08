[33mcommit b57db3447e8860f8f5e2c78303a431236a0a1042[m[33m ([m[1;36mHEAD -> [m[1;32mbestvideo[m[33m)[m
Author: jieun <jieun@congtube.com>
Date:   Fri Dec 6 14:22:45 2019 +0900

    리뷰 기본 뷰 갯수 수정

[33mcommit 82656d1f293c73bc1a763587db78231c052e4d2e[m
Author: jieun <jieun@congtube.com>
Date:   Fri Dec 6 14:22:03 2019 +0900

    스타페이지 pc화면 레이아웃 변경 완료

[33mcommit de7d2ecc49fb206341cb26d34a88132c8eee0828[m
Author: jieun <jieun@congtube.com>
Date:   Thu Dec 5 18:57:49 2019 +0900

    추가 이미지

[33mcommit 3f27f689b763b93e0980d5e55f38fb3f1a94518c[m
Author: jieun <jieun@congtube.com>
Date:   Thu Dec 5 18:56:26 2019 +0900

    스타페이지 상단바 반응형 레이아웃, 디자인 수정

[33mcommit 2fb3c008edb140e64bd130a601330274ae859bff[m
Author: jieun <jieun@congtube.com>
Date:   Thu Dec 5 15:49:52 2019 +0900

    스타페이지 상단 동영상,info부분 수정

[33mcommit 47e9b5625d431e7ed200d7f8fa160ec53226c01c[m
Author: jieun <jieun@congtube.com>
Date:   Thu Dec 5 12:38:04 2019 +0900

    스타페이지 CSS

[33mcommit b07b78a9b7bd712c4a5d15218e02656ba010c92f[m
Author: jieun <jieun@congtube.com>
Date:   Thu Dec 5 12:37:50 2019 +0900

    스타페이지 HTML

[33mcommit bf7ad2b7cec3ab4f83813afc012e2232c72c726c[m
Author: congbro <2044smile@naver.com>
Date:   Thu Dec 5 09:44:20 2019 +0900

    CI 구축 주석

[33mcommit 109b942e5f8a0a1847374cad475e9ad4887e154a[m
Author: congbro <2044smile@naver.com>
Date:   Thu Dec 5 09:44:06 2019 +0900

    models/bestvideo __str__ 이창석님의 베스트 비디오 로 변경

[33mcommit 2677e8fc65111ceba7a56d69b47778bc53cc0c42[m
Author: congbro <2044smile@naver.com>
Date:   Thu Dec 5 09:41:07 2019 +0900

    order_confirm 에 추가되어있던 models/bestvideo 를 생성

[33mcommit 4a20ddd0a53f2e1b38c7b2068070b825c76d90b4[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 15:50:34 2019 +0900

    detail.html video src= {{ bestvideo.video.url }} ADD

[33mcommit 14a89b8cc40983a3e31f4ded894a30bda9dae258[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 15:43:46 2019 +0900

    models/__init__ BestVideo ADD

[33mcommit 8b363cded4d7fbf0b83db0b6742813143d56f690[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 15:43:26 2019 +0900

    admin/channel.py inlines = ( BestVideoInline, ) ADD

[33mcommit 6fa6573d632f5fbc976ccf88a99a09de038e5d8f[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 15:42:48 2019 +0900

    admin/bestvideo.py BestVideoInline, extra = 1 설정

[33mcommit 8fe1117070e77a460644efcbd651a4bc76bcfd2a[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 15:41:44 2019 +0900

    bestvideo/admin/__init__ ADD

[33mcommit 5952f26f1b6904c428a455c438633750beedfa02[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 11:55:19 2019 +0900

    idea gitignore!!

[33mcommit ca150b9e0c17f8fabba370eb5323f06732cb1a62[m
Merge: 829c022 95fb33a
Author: cs_lee <47213853+2044smile@users.noreply.github.com>
Date:   Wed Dec 4 10:26:12 2019 +0900

    Merge pull request #2 from congtubeteam/future
    
    docker login -u AWS -p

[33mcommit 95fb33aad9c637f16134ed4ba6752cd773f5c774[m[33m ([m[1;31morigin/future[m[33m)[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 10:00:24 2019 +0900

    docker login -u AWS -p blah blah ~

[33mcommit 6540a44e8d14121243a727e4c5d2ba9e564e5be1[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 09:59:44 2019 +0900

    docker login -u AWS -p blah blah ~

[33mcommit 222f5cb7ddab55b33de8e04203d4ec127810a1a3[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 09:46:03 2019 +0900

    (aws ecr get-login) ADD

[33mcommit ed8be53ba2d944ea305fc49ca07c19e340abb8bb[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 09:44:25 2019 +0900

    (aws ecr get-login) ADD

[33mcommit 796a7668278802e5672c07d7c859119fe850e30e[m
Author: congbro <2044smile@naver.com>
Date:   Wed Dec 4 09:43:44 2019 +0900

    (aws ecr get-login) ADD

[33mcommit 47f1cc78e58e89c7f7033dc4571b3703c1809bc9[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:54:54 2019 +0900

    aws ecr get-login --no-include-email --region ap-northeast-2

[33mcommit 12ce2bc2e3843595d512f35ae4849bd2b094a940[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:37:51 2019 +0900

    sudo pip install awscli aws configure settinggit add .circleci/

[33mcommit c18a258bfd22a582444fea9f64b040a4eefd92a8[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:36:48 2019 +0900

    sudo pip install awscli aws configure settinggit add .circleci/

[33mcommit 9abd7c28da35c0b57c0daca8ce463b205c8e5470[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:30:08 2019 +0900

    sudo pip install awscli aws configure settinggit add .circleci/

[33mcommit 146ebfbcd5dbac746ee5dc083395510b218086ed[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:29:24 2019 +0900

    sudo pip install awscli aws configure settinggit add .circleci/

[33mcommit 3034c60f1c5dffedfe2ee0f027ba675faae44e26[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:24:18 2019 +0900

    {awsAccountNum}

[33mcommit 06f776406d8d32b26812cdb99339211203e8f1e2[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:22:07 2019 +0900

    string ADD

[33mcommit 75183a35438747534dd16ab305dec83261dea969[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:21:07 2019 +0900

    orbs TEST

[33mcommit c0c6059e8d7ea30037592a9996080ead45cfcd7b[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:05:00 2019 +0900

    sudo pip install awscli

[33mcommit dd6e8d081fd1df0996d93f4eb13c5f37e840150d[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 17:02:23 2019 +0900

    circleci/aws-ecr@6.5.0 TEST

[33mcommit f022250f32011328135c22d55725d5854f47958d[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 16:06:10 2019 +0900

    jobs ADD -build, -test

[33mcommit 5ba59749e3682a1249e556b4108ad1547946c6f8[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 16:00:53 2019 +0900

    RealCode orbs: ADD

[33mcommit 9fab1f0ca3359a123ccda05675bdd1ce04005731[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 15:42:46 2019 +0900

    RealCode (aws ecr get-login . . .) ADD

[33mcommit 8a62501f5c2c8e3a25cecadf8fdf2a7ff42e7f88[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 15:41:25 2019 +0900

    RealCode orbs aws-ecr ADD

[33mcommit 9079b19eb753fa9b3200cb2f89f83a0003f30987[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 15:21:28 2019 +0900

    RealCode aws_auth ADD

[33mcommit d69ab6a895b195b71ad0cfca3f45a3ed2fd08bd5[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 15:08:14 2019 +0900

    RealCode

[33mcommit 829c022254d878b32b53be24c2e044c07579e12c[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 15:04:43 2019 +0900

    AWS-auth infomation ADD

[33mcommit 6573556eeaa0767a6a14492ec33fe1b530e180ca[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 15:03:15 2019 +0900

    AWS-auth infomation ADD

[33mcommit 88790c34a2dcb1fc33b747d2275e28fbc4d85a03[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 15:01:55 2019 +0900

    AWS-auth infomation ADD

[33mcommit c427fbc4b4ae78282b1230f5d36d0debf203bb8f[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 14:56:14 2019 +0900

    realCodegit add .circleci/

[33mcommit f70123171a49f997495d9ae4a1ca97719f7222e6[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 14:55:47 2019 +0900

    realCodegit add .circleci/

[33mcommit 2a1d44b38f0769e191c954c67cccaf66c958ed67[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 14:42:51 2019 +0900

    circleci/python:3.6.1 docker 18.06.0-ce docker forgot syntax Error

[33mcommit ba3d988ddd1b30aa1c385cf8f757a4481d502a2b[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 14:41:39 2019 +0900

    circleci/python:3.6.1 docker 18.06.0-ce docker build tag push ADD

[33mcommit 2f0e9e947b9bc1224eae8354a008dc3d4ce89e95[m
Author: congbro <2044smile@naver.com>
Date:   Tue Dec 3 14:40:04 2019 +0900

    circleci/python:3.6.1 docker 18.06.0-ce docker bui