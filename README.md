# Ethan Saline

**Data Scientist** | B.A. Data Science, Minor in Statistics, Brigham Young University–Idaho (expected April 2027, GPA 3.96)

[LinkedIn](https://www.linkedin.com/in/ethan-saline) | [Email](mailto:e.s.w.saline@gmail.com) | [Portfolio](ethan-saline.github.io/Ethan-Saline/)

---

## About

I build explainable, production-style machine learning systems across computer vision, retrieval-augmented pipelines, and agentic AI. My work spans data engineering, automated MLOps pipelines (Airflow, Docker, PostgreSQL), and statistical modeling. I also designed my university's first Agentics AI course.

## Skills

| | |
|---|---|
| **Languages** | Python, R, SQL, C# |
| **ML / AI** | Predictive Modeling, Time Series Forecasting, Computer Vision (CNNs, YOLO), TensorFlow/Keras, Retrieval-Augmented Systems (FAISS), Grad-CAM Explainability, LLM Agents (LangChain, Ollama, Gemini) |
| **Data Engineering** | ETL/ELT, Data Modeling, Data Warehousing, Star Schema, PySpark, Polars, pandas, NumPy, PostgreSQL |
| **Tools & Platforms** | Airflow, Docker, Git/GitHub, Power BI, ggplot, Excel |
| **Techniques** | Machine Learning, Statistical Analysis, Data Visualization, Data Wrangling |
| **Languages (spoken)** | English, Portuguese |

## Experience

### Data Scientist, Pulse Decision Science
*Washington, DC | Apr 2026 – Sep 2026*

- Built SQL-backed data pipelines that ingest, clean, and prepare raw data for downstream machine learning.
- Developed multiple predictive models delivered to political campaign clients to support data-driven decisions.
- Cleaned and sampled datasets for delivery to external clients, with a focus on data quality.

### AI Curriculum Consultant, Brigham Young University–Idaho
*Rexburg, ID | Jan 2026 – Apr 2026*

- Designed and built the university's first Agentics AI course, including curriculum architecture, textbook website, and practice exercises, launching Fall 2026.
- Developed hands-on Colab labs for building LLM agents with Ollama and Gemini, orchestrated with LangChain.

### Data Science Lab Director, Brigham Young University–Idaho
*Rexburg, ID | Aug 2025 – Apr 2026*

- Directed day-to-day operations of the Data Science Lab, supporting students and faculty across research and coursework.
- Onboarded and mentored new lab members on data workflows, tools, and reproducible analysis.
- Established lab standards for timekeeping and data collection, improving handoffs between student cohorts.

### Big Data Analytics Teaching Assistant, Brigham Young University–Idaho
*Rexburg, ID | Apr 2026 – Present*

- Held weekly office hours to debug student code and explain Big Data architecture concepts.
- Collaborated with the professor to refine assignment rubrics and clarify instructions.
- Graded assignments and gave written feedback on technical accuracy and analytical thinking.

### MathLab Supervisor & Mentor, Brigham Young University–Idaho
*Rexburg, ID | Sep 2024 – Present*

- Supervised lab shifts of 8 tutors and resolved academic questions in real time.
- Tutored 15+ students per week one-on-one in calculus and statistics.
- Identified recurring student misconceptions in statistics and developed targeted explanation strategies.

### Data Science Programming TA, Brigham Young University–Idaho
*Rexburg, ID | Jun 2025 – Dec 2025*

- Assisted students across 3 sections in Python data science workflows (pandas, NumPy, Polars, visualization libraries).
- Debugged code in office hours, explaining root causes to build lasting understanding.

## Projects

### Multimodal Chest X-Ray Diagnosis Pipeline
`Python` `BioViL` `FAISS` `Airflow` `Docker` `PostgreSQL` `Redis`

- Built an end-to-end pipeline that turns chest X-ray DICOMs into radiology reports, per-pathology diagnosis probabilities, and Grad-CAM heatmaps (AUROC 0.72–0.82), with a human-in-the-loop validation step.
- Designed a FAISS retrieval layer returning the 5 most similar historical studies per image: 89.7% Recall@5 at 1,200 studies, under 2 seconds per inference.
- Orchestrated a 9-step Airflow DAG (ingest, encode, retrieve, report, diagnose, validate) in Docker, persisting outputs to PostgreSQL with Redis caching.
- Automated weekly retraining on 200 new MIMIC-CXR studies (377,000-image dataset) to simulate real hospital data influx, with uncertainty-label strategies chosen to reduce missed findings.

### COVID Chest X-Ray Diagnosis CNN
`Python` `TensorFlow` `Keras`

- Built a convolutional neural network to classify chest X-rays as COVID, pneumonia, tuberculosis, or healthy (89% accuracy).
- Preprocessed and augmented 7,500 images to improve generalization, and evaluated with AUC-ROC, precision, and recall to handle class imbalance.

### Assembly Line YOLO Detection
`Python` `YOLO` `CVAT`

- Trained a YOLO model on conveyor-belt video to classify candy by color in real time.
- Compared labeling approaches (including CVAT annotation) for speed, accuracy, and downstream performance, and built a custom dataset from labeled video frames.

### Heart Failure Mortality Prediction
`R` `Logistic Regression`

- Built a logistic regression model to predict mortality in 299 heart failure patients (80.3% accuracy at a 0.5 threshold).
- Identified serum creatinine as the strongest continuous risk factor (OR 1.94), with ejection fraction protective (OR 0.94) and age 80+ raising odds (OR 5.08).
- Showed that a 3-feature model can perform well on small clinical datasets.

### COVID-19 Transcriptomics
`R` `DESeq2`

- Analyzed 2,000+ differentially expressed genes and narrowed them to the 4 highest-confidence candidates tied to the COVID-19 immune response, using adjusted p-values and log2 fold-change thresholds.
- Communicated results with volcano plots and heatmaps.

### Influenza-Like Illness Time Series
`R` `STL` `ARIMA` `ETS`

- Decomposed surveillance data into trend, seasonal, and residual components, then forecast future activity with ARIMA/ETS models and visualized results for non-technical audiences.

### Recommender System
`Python`

- Built a co-occurrence recommender on anonymized interaction data using an optimized sparse matrix, and evaluated it with precision@k and recall@k.

## Education

**B.A. in Data Science, Minor in Statistics**
Brigham Young University–Idaho | Expected April 2027 | GPA 3.96

**Certificates**

- Machine Learning Specialization (Supervised ML, Unsupervised ML, Advanced Algorithms), Stanford Online
- Machine Learning, BYU–Idaho
- Databases, BYU–Idaho

## Leadership & Service

### Full-time Volunteer Missionary, São Paulo Interlagos Mission, Brazil
*Oct 2021 – Oct 2023*

- Served as Zone Leader, coordinating missionary teams, running weekly planning meetings, and setting goals with mission leadership.
- Managed finances as Financial Secretary for a mission of 80+ people, including budgets, reimbursements, and records.
- Trained new missionaries one-on-one, and led all meetings and training entirely in Portuguese.

---

*Open to data science and machine learning opportunities. Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/ethan-saline).*