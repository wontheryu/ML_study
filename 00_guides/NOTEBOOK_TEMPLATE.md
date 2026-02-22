# main.ipynb Template (고정)

> 이 노트북은 “이론 70% + 실험 30%” 비중을 지킨다.  
> 모든 플롯은 `assets/`에 저장한다.

---

## 1. 문제 정의 & 지표 선택
- 문제: (회귀/분류/비지도) 무엇을 예측/구분/구조화?
- 지표: (MSE/MAE/RMSE, AUC/PR-AUC, logloss, silhouette 등)
- 지표가 최적화하는 대상(리스크/손실)과 연결해서 설명

---

## 2. 모델 정의
- 가설공간(함수 클래스):
- 파라미터:
- 예측함수/결정경계:
- (필요시) 확률모형/링크함수/커널 등

---

## 3. 목적함수 & 최적화
- Empirical risk:
- Regularizer(있다면):
- closed-form vs iterative / convexity 여부
- 최적화 안정성 이슈(스케일링, 조건수, 초기값 등)

---

## 4. 가정과 진단
- 가정 리스트:
  - 예) 선형성, 독립성, 등분산, 정규성(오차), i.i.d, 마진/분리, 거리 의미 등
- 진단 플롯/검정:
  - 잔차 vs 예측값
  - QQ plot / 히스토그램
  - leverage / Cook’s distance
  - calibration curve(분류)
  - learning curve / validation curve
- 저장: `assets/diagnostic_*.png`

---

## 5. 일반화 이론
- bias–variance 관점에서 이 모델의 성질
- 규제의 의미: 제약/베이지안 prior 관점
- 복잡도: 차원/깊이/마진/프로토타입 수 등

---

## 6. 해석 가능성
- 계수/중요도/규칙/마진/프로토타입 관점으로 설명
- 무엇이 “해석 가능한 것”이고 무엇은 아닌지

---

## 7. 실패 모드(반례)
- 언제 깨지는가?
  - 예) 공선성, 이분산, 이상치, 고차원, 클래스 불균형, 분포 이동 등
- 그때 대안 모델은?
  - 예) Ridge/Lasso, Huber, Tree/GBM, SVM, calibration, robust scaling 등

---

## 8. 최소 실험
### 8.1 Toy Track (현상/반례 확인)
- 합성데이터를 직접 만들고 “깨지는 조건” 주입
- 진단 플롯 1개 이상 저장
- 관찰한 현상 3줄 요약

### 8.2 Real Track (Kaggle/실데이터 적용)
- 핵심 실험 1개만(짧게)
- 누수 방지: Pipeline 사용
- split 전략: Hold-out(+seed), 필요시 CV

---

## 9. 정리: 선택 규칙(Decision rule)
- “데이터가 ~이면 이 모델을 선택” 형태로 3~5문장
EOF