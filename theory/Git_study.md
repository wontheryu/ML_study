# 🍎 macOS 환경 VS Code & GitHub 연동 가이드
오늘 처음으로 맥북에서 VS Code와 GitHub을 성공적으로 연동한 과정을 기록합니다.

## 1. 초기 세팅 (Configuration)
맥북 터미널에서 Git 사용자 정보를 등록합니다. (최초 1회)
- `git config --global user.name "내 닉네임"`
- `git config --global user.email "내 이메일"`

## 2. 저장소 가져오기 (Clone)
1. GitHub 웹사이트에서 새 저장소(Repository) 생성 (예: `ML_study`).
2. 초록색 **[<> Code]** 버튼을 눌러 HTTPS 주소 복사.
3. VS Code에서 `Command(⌘) + Shift + P` -> `Git: Clone` 입력 후 엔터.
4. 주소 붙여넣고 맥북의 로컬 폴더(바탕화면 등) 선택하여 저장.

## 3. 작업 업로드 (Commit & Push) 루틴
작업한 내용을 온라인 저장소에 반영하는 3단계 과정입니다.

1. **변경사항 확인**: 수정된 파일이 있으면 VS Code 왼쪽 '소스 제어' 탭에 숫자가 뜹니다.
2. **커밋(Commit)**: 
   - 메시지 창에 작업 내용(예: `README 수정`) 입력.
   - `✓ Commit` 버튼 클릭 (또는 `Command + Enter`).
3. **푸시(Push)**: 
   - `Sync Changes` 버튼 클릭하여 GitHub 서버로 전송.
   - 온라인(GitHub.com)에서 새로고침하여 반영 여부 확인.
   - git push origin main 코드로 푸시하기 이용

## 4. 맥북 꿀팁: .DS_Store 관리
맥북 시스템 파일인 `.DS_Store`가 깃에 올라가지 않게 하려면:
- `.gitignore` 파일을 생성하고 내용에 `.DS_Store`를