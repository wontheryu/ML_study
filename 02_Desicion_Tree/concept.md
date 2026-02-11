# 🌳 Decision Tree: 고급 이론 및 실무 가이드

## 1. Decision Tree에 최적화된 데이터 조건
모델 선정의 논리적 근거(Rationale)를 확보하기 위해 다음 조건을 체크합니다.

 피처 타입의 유연성: 수치형과 범주형 변수가 혼합된 데이터에서도 전처리(스케일링 등) 부담 없이 즉시 적용 가능합니다.
 비선형성 대응: 데이터의 정규성이나 선형성 가정이 필요 없으며, 변수 간의 복잡한 상호작용이 존재하는 비선형 데이터에 강력합니다.
 데이터 규모: 수만 건 이내에서는 단일 트리로도 충분히 빠르고 강력하지만, 고차원 대용량 데이터로 갈수록 앙상블(RF, XGBoost)로의 확장을 고려해야 합니다.

## 2. 분할 기준: 수학적 핵심 원리

트리는 각 노드에서 다음 지표를 기준으로 최적의 분기점(Split Point)을 찾습니다.

### 📊 지니 불순도 (Gini Impurity)

클래스가 개일 때, 노드 내 클래스 의 비율 를 이용해 계산합니다.


### 📉 엔트로피 (Entropy) & 정보 이득

데이터의 무질서도를 측정하며, 정보 이득()이 최대화되는 방향으로 나뉩니다.

 Entropy: 
 Information Gain: 

### ⚖️ Gain Ratio (정보 이득비)

ID와 같이 고유값이 많은 변수가 선택되는 함정을 피하기 위해, 속성 자체의 엔트로피()로 를 정규화합니다.


## 3. 하이퍼파라미터 튜닝 포인트

단순 `max_depth` 조절 외에도 실무에서 중요하게 다루는 파라미터입니다.

 `max_features`: 각 분산에서 고려할 피처 수 제한. 트리 간 상관관계를 줄여 과적합을 방지합니다.
 `max_leaf_nodes`: 리프 노드 개수의 상한을 직접 제어하여 모델 복잡도를 직관적으로 관리합니다.

## 4. CART 알고리즘: 분류 vs 회귀

Scikit-learn은 이진 분할(Binary Split) 기반의 CART 알고리즘을 사용합니다.

 Classification: 지니/엔트로피 감소량을 최대화하는 지점을 찾습니다.
 Regression: 노드 내 타깃 값의 제곱 오차 합(SSE)을 최소화하는 분할을 수행하며, 예측값은 해당 영역의 평균값을 반환합니다.

## 5. 고급 기법: CCP (Cost Complexity Pruning)

가지치기(Pruning)를 과학적으로 수행하기 위해 복잡도 파라미터 를 활용합니다.


 메커니즘: 이면 과적합 트리가 되고, 값이 커질수록 노드 수를 줄여 단순한 모델을 만듭니다.
 실무 패턴: `cost_complexity_pruning_path`를 통해  후보군을 추출하고, 검증 데이터(CV) 성능이 가장 좋은 지점을 선택합니다.

## 6. 모델 평가 및 과적합 진단

 평가 지표: 분류 시 Accuracy뿐만 아니라 F1-score, ROC-AUC를 필히 확인합니다. 회귀 시에는 와 RMSE의 Train/Test 격차를 분석합니다.
 Overfitting 신호: Train 성능은 90% 이상인데 Test 성능이 급격히 낮다면, 즉시 `ccp_alpha`나 `min_samples_leaf` 조정을 검토해야 합니다.

---

### 🚀 실습 로드맵 (main.ipynb 설계)

1. Data Setup: 수치형+범주형 혼합 데이터 로드 (예: Titanic 또는 Adult Dataset).
2. Unconstrained Tree: 제약 없는 트리 학습을 통한 과적합 현상 시각화.
3. Tuning Loop: `max_depth`와 `max_leaf_nodes`에 따른 성능 변화 곡선 분석.
4. CCP Optimization: 최적의 `ccp_alpha`를 찾는 그래프 분석.
5. Final Interpretation: `dtreeviz`를 활용한 의사결정 경로 시각화 및 인사이트 도출.

🚀 Decision Tree 실무 심화 실습 로드맵
Phase 1: Baseline & Overfitting Diagnostic (진단)

실무에서는 가장 먼저 "제약 없는 트리"를 만들어 데이터의 잠재력을 확인합니다.

Full-Grown Tree 학습: 하이퍼파라미터 제한 없이 학습하여 훈련 데이터의 완벽한 분리 시도.

Learning Curve 분석: 샘플 수 증가에 따른 Train/Validation 점수 변화를 시각화하여 데이터 부족인지, 모델 복잡도 문제인지 판별.

Tree Depth vs Error Graph: 깊이(0∼30)에 따른 오차 곡선을 그려 'Golden Mean(최적의 지점)'을 시각적으로 탐색.

Phase 2: Scientific Pruning (과학적 가지치기)

max_depth를 감으로 찍는 것이 아니라 수치적으로 결정하는 단계입니다.

CCP(Cost Complexity Pruning) 실습: cost_complexity_pruning_path()를 호출하여 α 후보군을 추출.

Total Impurity vs Alpha: α 값 변화에 따른 전체 불순도 변화율을 분석하여 유의미한 분기점 확인.

Optimal Alpha Selection: 교차 검증(Cross-Validation)을 통해 Test 정확도가 가장 높은 α를 최종 모델에 적용.

Phase 3: Robustness & Strategy (해결 및 강화)

과적합을 잡았다면, 이제 모델의 신뢰도를 높이는 작업을 수행합니다.

Feature Importance & Selection: 중요도가 0에 가까운 피처를 제거하고 재학습하여 모델의 노이즈 감소.

Handling Imbalanced Data: 클래스 불균형이 심할 경우 class_weight='balanced' 적용 전후의 F1-score 및 Precision-Recall Curve 비교 분석.

Threshold Optimization: 분류 임계값(Threshold)을 조정하여 비즈니스 목적(예: 암 진단 시 Recall 극대화)에 최적화.

Phase 4: Interpretation & Action (해석 및 행동)

분석가는 결과 수치뿐만 아니라 "왜?"를 설명해야 합니다.

Decision Path Tracking: 특정 샘플(예: 이탈한 핵심 고객)이 어떤 노드들을 거쳐 최종 판단되었는지 경로 추적.

dtreeviz 시각화: 각 노드의 데이터 분포(히스토그램)를 시각화하여 모델의 판단 기준이 상식적인지 검토.

Error Analysis: 모델이 틀린 샘플들만 모아서 공통된 특징(패턴)을 찾아내고, 추가 피처 엔지니어링 아이디어 도출.

📂 추천 실습 과제: "대출 승인 여부 예측 (Loan Approval)"

이 로드맵을 적용하기 가장 좋은 데이터는 범주형(직업, 신용등급)과 수치형(연봉, 대출액)이 혼합되어 있고, 클래스 불균형이 존재하는 금융 데이터입니다.

다음 작업으로 무엇을 도와드릴까요?

"이 로드맵의 Phase 1~2를 구현한 코드를 보여줘"

"실습에 쓸 만한 고퀄리티 샘플 데이터셋 로드 코드부터 짜줘"