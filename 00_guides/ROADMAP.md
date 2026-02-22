# ROADMAP (ML_STUDY)

이 저장소는 “성능 경쟁”이 아니라 **이론 검증(가설·반례·진단 플롯)** 중심으로 진행한다.

---

## 운영 원칙 (고정)
- 각 섹터 폴더는 반드시 3개를 갖는다:
  1) `main.ipynb` (이론 70% + 실험 30%)
  2) `README.md` (Decision rule + 실험로그 표)
  3) `assets/` (잔차/오차/진단 플롯 저장)

- 노트북 `main.ipynb` 고정 템플릿(순서 고정):
  1. 문제 정의 & 지표 선택
  2. 모델 정의
  3. 목적함수 & 최적화
  4. 가정과 진단
  5. 일반화 이론
  6. 해석 가능성
  7. 실패 모드(반례)
  8. 최소 실험 (Toy 1 + Real 1)
  9. 정리: 선택 규칙(Decision rule)

---

## 추천 학습 순서
### Phase 0: 공통 이론
1) Empirical vs Expected Risk  
2) Bias–Variance / Under–Overfitting 진단  
3) Regularization(L1/L2/early stopping) = 제약/사전분포 관점  
4) 데이터 분할(i.i.d / 그룹 / 시계열 / 누수)  
5) 불확실성(bootstrap, CI/PI)  
6) Metric 의미(특히 분류 threshold, calibration)

### Phase 1: 선형 모델
- 01 Linear Regression
- 02 Regularized Regression (Ridge/Lasso/ElasticNet)
- 03 Logistic Regression

### Phase 2: 트리/앙상블
- 04 Decision Tree
- 05 Random Forest
- 06 Gradient Boosting (XGBoost/LightGBM/CatBoost 중 1~2)

### Phase 3: 기하학적 모델
- 07 KNN
- 08 SVM (마진/커널)

### Phase 4: 비지도 + 표현
- 09 PCA (SVD 관점)
- 10 Clustering (K-means, GMM)

### Phase 5: PyTorch 트랙 (동일 결과 재현 → 확장)
- 11 PyTorch basics: Linear/Logistic/MLP를 sklearn 결과와 “동일하게” 맞추는 실험

---

## 섹터 진행 체크리스트 (매 섹터 공통)
1) `main.ipynb` 작성 (템플릿 1~9)
2) Toy 실험: “깨지는 조건” 1개 주입 + 진단 플롯 1개 이상 저장(`assets/`)
3) Real 실험: Kaggle/실데이터 1개만 짧게
4) `README.md`에 Decision rule 문장 3~5개로 정리 + 실험로그 표 업데이트

---

## 이번 주 1회차 목표(추천)
- 01_linear_regression: Toy(공선성/이분산 중 1개) + Real(작은 회귀 데이터 1개)
- 결과물: 진단 플롯 2장 이상 + Decision rule 3문장
EOF