취업 포트폴리오의 첫인상을 결정할 루트(최상위) `README.md` 내용입니다. 이 저장소가 단순히 공부 기록용이 아니라, **"데이터에 근거해 모델을 선택하고 최적화할 줄 아는 분석가"**의 저장소임을 보여주는 데 초점을 맞췄습니다.

아래 내용을 복사해서 최상위 `README.md`에 붙여넣으세요.

---

# 🚀 ML_STUDY: 취업 역량 증명을 위한 머신러닝 마스터 로드맵

이 저장소는 단순한 코드 복사가 아닌, **데이터 특성에 따른 모델 선정 논리와 성능 최적화 과정**을 증명하기 위한 머신러닝 학습 프로젝트입니다.

## 🎯 학습 원칙 (Core Principles)

* **역량 증명:** 모델 선정 이유와 하이퍼파라미터 튜닝 과정을 논리적으로 서술한다.
* **도메인 확장성:** 데이터의 형태(수치형, 범주형 등)에 따른 최적의 모델 구조를 제안한다.
* **실무 중심:** 이론은 핵심 수식 위주로 정리하고, 고퀄리티의 실습 코드로 구현한다.
* **평가 지표의 심층 해석:** MSE, R2, F1-score, AUC 등 지표를 통해 모델의 한계와 개선점을 도출한다.

---

## 🗺️ 커리큘럼 로드맵 및 현황 (Status Board)

각 섹터는 독립적인 프로젝트 폴더로 구성되어 있으며, 상세 분석 내용은 폴더 내 `README.md`에서 확인 가능합니다.

| 단계 | 섹터 (Sector) | 핵심 주제 및 모델 | 상태 |
| --- | --- | --- | --- | --- |
| **01** | **Linear Regression** | 단순/다중 회귀, 선형성 가정 검정 | 🔄 진행 중 |
| **02** | **Regularized Regression** | Lasso, Ridge, ElasticNet (과적합 제어) | ⬜ 대기 |
| **03** | **Logistic Regression** | 이진/다중 분류, Sigmoid 함수, Odds Ratio | ⬜ 대기 |
| **04** | **Decision Tree** | Gini Impurity, Entropy, 시각화 및 해석 | ⬜ 대기 | 
| **05** | **Random Forest** | Bagging 앙상블, Feature Importance 분석 | ⬜ 대기 |
| **06** | **Boosting Models** | XGBoost, LightGBM, CatBoost 최적화 | ⬜ 대기 | 
| **07** | **SVM & KNN** | Kernel Trick, 거리 기반 모델링 | ⬜ 대기 |
| **08** | **Clustering & PCA** | K-Means, DBSCAN, 차원 축소 및 시각화 | ⬜ 대기 |

---

## 🛠️ 개발 환경 (Environment)

* **Language:** Python 3.x
* **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn
* **Tools:** VS Code, Jupyter Notebook

---

## 📂 폴더 구조 가이드

각 모델 폴더는 아래와 같은 표준 구조를 따릅니다.

* `main.ipynb`: 전체 분석 프로세스 (EDA -> 전처리 -> 모델링 -> 평가)
* `README.md`: 분석 결과 시각화 및 비즈니스 인사이트 정리

---

### 💡 Tip: 상태 표시 업데이트 방법

공부를 완료할 때마다 위 표의 **'상태'** 열을 ⬜(대기) -> 🔄(진행 중) -> ✅(완료)로 업데이트하며 잔디를 심어보세요!

이제 이 내용을 저장하신 후, **01_Linear_Regression**의 첫 번째 실습 데이터를 정해볼까요? (주택 가격 vs 자전거 대여 수요) 어떤 것이 좋을까요?