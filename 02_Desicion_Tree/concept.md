# 🌳 Decision Tree: 핵심 이론 정리

## 1. 개요 및 모델 선정 배경
Decision Tree는 데이터의 특성(Feature)을 기준으로 의사결정 규칙을 생성하여 데이터를 분류(Classification)하거나 예측(Regression)하는 모델입니다.
 장점: 모델의 판단 근거를 시각화할 수 있어 '화이트박스(White-box)' 모델이라 불리며, 비전문가에게 설명하기 용이합니다.
 단점: 트리가 깊어질수록 훈련 데이터에 과도하게 최적화되는 과적합(Overfitting) 문제가 빈번합니다.

## 2. 분할 기준 (Mathematical Metrics)
트리는 각 분기점에서 불순도(Impurity)를 가장 많이 낮추는 변수를 선택합니다.

 지니 불순도 (Gini Impurity): 
 Scikit-learn의 기본값으로, 계산 비용이 적어 대용량 데이터에 유리합니다.


 엔트로피 (Entropy / Information Gain): 
 지니 불순도보다 조금 더 균형 잡힌 트리를 만드는 경향이 있으나 로그 계산이 추가됩니다.

## 3. 주요 하이퍼파라미터 (과적합 제어)
실무에서 가장 중요한 부분입니다. 성능 최적화를 위해 다음 파라미터를 조정합니다.

| 파라미터 | 설명 | 전략 |
| --- | --- | --- |
| `max_depth` | 트리의 최대 깊이 | 너무 깊으면 과적합, 너무 낮으면 과소적합 발생. |
| `min_samples_split` | 노드를 분할하기 위한 최소 샘플 수 | 이 값이 클수록 분할이 제한되어 트리가 보수적으로 변함. |
| `min_samples_leaf` | 리프 노드가 가져야 할 최소 샘플 수 | 데이터가 적은 노드에 의한 이상치 민감도를 낮춤. |
| `ccp_alpha` | 비용 복잡도 가지치기 (Cost Complexity Pruning) | 트리의 크기에 페널티를 주어 불필요한 가지를 제거함. |

## 4. 모델의 평가 포인트

 Feature Importance (특성 중요도): 모델이 분할에 가장 많이 사용한 피처 순위를 통해 도메인 지식과 데이터의 일치성을 확인합니다.
 Overfitting Check: Train Accuracy와 Test Accuracy의 간극을 확인합니다. (예: Train 0.99 / Test 0.75라면 즉시 가지치기 필요)