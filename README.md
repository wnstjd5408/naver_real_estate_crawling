# naver_real_estate_crawling

<<<<<<< HEAD
aaaa
=======

## 2-1. Git Workflow

기능, 버그 수정, 문서 작성은 모두 별도 브랜치에서 작업하고, 이를 PR로 만들어 메인 브랜치인 `main`에 병합하는 것으로 한다.

아래 순서에 따라 작업한다.

1. 추가할 기능에 대한 이슈 생성
2. 이슈의 성격에 따라 브랜치 생성 (`feat`, `fix`, `refactor`)
3. 브랜치에서 커밋한 후 GitHub로 `push`
4. `Create Pull Request` 로 PR 생성
5. `Merge Pull Request` 로 `main` 에 병합
6. 완료된 브랜치는 삭제

> 간단한 수정 또는 리팩터링의 경우 이슈를 생성하지 않고 바로 브랜치를 만들어 작업할 수 있다.

## 2-2. 브랜치 이름 컨벤션

브랜치 이름은 cebab case로 작성하는 것을 원칙으로 한다.

- `feat/#ISSUE-feature-description`: 기능 추가 브랜치
- `fix/#ISSUE-fix-description`: 버그 수정 브랜치
- `refactor/#ISSUE-refactor-description`: 리팩터링 브랜치
- `docs/docs-description`: 문서 브랜치

> 해당되는 이슈가 없다면 #ISSUE는 생략할 수 있다.

## 2-3. 커밋 이름 컨벤션

커밋도 브랜치와 마찬가지로 성격에 따라 구분하여 `feat`, `fix`, `refactot`, `docs` 등을 붙인다.

- `feat: commit message`: 기능 추가 커밋
- `fix: commit message`: 버그 수정 커밋
- `refactor: commit message`: 리팩터링 커밋
- `docs: commit message`: 문서 커밋
- `style: commit message`: 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우
- `test: commit message`: 테스트 코드, 리펙토링 테스트 코드 추가
- `chore: commit message`: 빌드 업무 수정, 패키지 매니저 수정
