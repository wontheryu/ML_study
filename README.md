# ML_study (Machine Learning Portfolio)

머신러닝을 공부로 끝내지 않고,
재현 가능한 실험 + 정리된 글 + 깔끔한 코드로 포트폴리오를 쌓아가는 저장소.

- 목표: 문제정의 → 데이터/가정 → 모델링 → 평가 → 인사이트 흐름으로 기록한다.
- 원칙: 결과보다 재현성/근거/해석을 우선한다.

---

## What’s inside

- 1_NOTES: 개념 정리(수학/통계/ML/DL)
- 2_LABS: 실습(알고리즘 구현, 실험 템플릿, 미니 실험)
- 3_PROJECTS: 완결형 프로젝트(README + 리포트 + 코드)
- 4_COMPETITIONS: Kaggle/대회 기록
- 5_PAPERS: 논문 읽기/요약/재현
- 0_SETUP: 환경 세팅/템플릿/규칙

---

## Repository Structure

```
ML_study/
├─ 0_SETUP/                # 개발환경/세팅/템플릿
├─ 1_NOTES/                # 개념 정리(수학/ML/DL/통계)
├─ 2_LABS/                 # 실습(알고리즘 구현, 실험)
├─ 3_PROJECTS/             # 포트폴리오 프로젝트(완결 단위)
├─ 4_COMPETITIONS/         # Kaggle/대회
├─ 5_PAPERS/               # 논문 읽기/요약/재현
├─ assets/                 # README 이미지, 다이어그램
└─ README.md
```

---

## Project Template (Standard)

각 프로젝트 폴더(예: `3_PROJECTS/프로젝트명/`)는 아래 구조를 권장한다.

```
프로젝트명/
├─ README.md               # 1페이지 요약(핵심 결과/표/그림 포함)
├─ src/                    # 학습/추론/평가 코드(모듈화)
├─ notebooks/              # EDA/실험 노트(핵심만)
├─ reports/                # 결과물(이미지/표/리포트)
├─ configs/                # 실험 설정(yaml/json 등)
└─ requirements.txt        # 또는 environment.yml
```

프로젝트 `README.md`에 최소 포함:
- 문제 정의(왜 중요한가)
- 데이터 설명(출처/기간/전처리/가정)
- 모델/베이스라인
- 평가 지표 및 실험 설정(분할/seed/누수 방지)
- 결과(표/그림) + 해석
- 한계와 다음 스텝

---

## Learning Roadmap

### A. Fundamentals
- 선형대수/미적분/확률통계 핵심 정리
- 회귀/분류 기본기 + 과적합 제어

### B. Practical ML
- 전처리/피처엔지니어링
- 실험 관리(seed 고정, 로그, 버전)
- 불균형/결측/이상치/데이터 누수 대응

### C. Modeling & Interpretation
- 트리계열(GBM) vs 신경망 비교
- 설명가능성(SHAP 등)과 모델 신뢰 관점 정리

### D. Portfolio-grade Projects
- 금융/보험 도메인 프로젝트 2~3개
- 가능하면 논문 스타일(가정/제약/재현성)로 작성

---

## Current Focus

- [ ] 첫 미니프로젝트 1개: EDA → baseline → 개선 → 리포트
- [ ] 노트: 분류/회귀 평가 지표 정리(ROC-AUC, PR-AUC, calibration)
- [ ] 실험 템플릿: `train / eval / predict` 표준화

---

## How to Run (Example)

> 프로젝트별 실행 방법은 각 프로젝트 `README.md`를 우선한다.

```bash
# 1) 환경 설치
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2) 학습/평가(예시)
python src/train.py --config configs/base.yaml
python src/eval.py  --config configs/base.yaml
```

---

## 기록 원칙

- "좋다/나쁘다"에서 끝내지 않고 왜 그런지까지 적는다.
- 비교는 항상 같은 데이터 분할/같은 지표/같은 기준에서 한다.
- 재현성: seed 고정, 데이터 버전, 실험 설정(config)을 남긴다.

---

## Links

- Projects: `3_PROJECTS/`
- Notes: `1_NOTES/`
- Labs: `2_LABS/`

(추후) Blog/Notion: TBD

---

## License

개인 학습/포트폴리오 목적. (필요 시 라이선스 명시)