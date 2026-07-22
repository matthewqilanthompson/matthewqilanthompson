# Hi, I'm Matthew Thompson

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matthewqilanthompson/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:matthewqilanthompson.work@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/matthewqilanthompson/Data-Science-Portfolio)

## Data Analyst · SQL · Python · R · M.S. Data Science, University of Arizona

I'm a data analyst. I design databases and write the SQL that turns messy, large datasets into answers a business can act on, and I check the data before I trust it, cleaning, validating, and reconciling it so the results hold up. On one project an early model came back almost perfect; instead of taking the win I went looking for the mistake, found leaked answer data, and re-validated until the number was real.

I also build predictive models and ship production software. My background is in biology research, which is where I learned to work hypothesis-first in an unfamiliar domain, but the analysis travels, and I'm not limited to life sciences.

---

## Education

| Degree                | Institution                                  | Status                 |
| --------------------- | -------------------------------------------- | ---------------------- |
| **M.S. Data Science** | University of Arizona (Online)               | Completed, May 2026   |
| **B.S. Biology**      | Gallaudet University *(Minor: Data Science)* | Completed, May 2023   |

---

## Research Experience

| Role | Organization | Focus |
| ---- | ------------ | ----- |
| Research Intern | Oklahoma State University, National Science Foundation (NSF) ON-RaMP postbaccalaureate research training program | 1 year of independent research: statistical modeling in R (regression, analysis of variance, repeatability) on grasshopper coloration & behavior; built a Python automation script; presented at the 2024 Society for Integrative and Comparative Biology (SICB) conference |
| Summer Research Intern, NSF Research Experiences for Undergraduates (REU) | Maryland Sea Grant | Selected from 400+ applicants; quantified marine microbial abundance across depth gradients in R & Excel; extended into an Honors thesis |

*Full work history on [LinkedIn](https://www.linkedin.com/in/matthewqilanthompson/).*

---

## Presentations

| Venue | Work |
| ----- | ---- |
| 2024 Society for Integrative and Comparative Biology (SICB) Conference | Poster on temperature and developmental-environment effects on grasshopper coloration and behavior |
| 2023 Esri Federal GIS Conference (Washington, D.C.) | ArcGIS Pro poster on how ocean temperature and climate trends affect coral reef ecosystems |
| 2022 NGA GeoSpectrum Conference | ArcGIS StoryMap on climate change's impact on biodiversity |

---

## Academic Projects

These projects demonstrate my data science capabilities across healthcare analytics, machine learning, database systems, and statistical visualization:

| Project                                                                                                                                                   | What I Applied                                                                                                                                      | Tech                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| [**Healthcare Analytics with SQL**](https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/database-systems/sql-nosql-databases-info579) | Designed third normal form (3NF) database schemas across 1,171 patients and 53,346 encounters (~65MB synthetic EHR data, 6 entities), then wrote 6 documented analytical reports against 5 business objectives (profitability, clinical quality, provider utilization, readmission reduction, and expansion) using multi-table joins, CTEs, correlated subqueries, and temporal analysis. Surfaced a provider workload imbalance (busiest handled 3,000+ encounters vs. under 2,000 for peers). End-to-end reproducible via Docker. | MySQL, SQL, Python |
| [**Healthcare Readmission Prediction**](https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/data-science/foundation-of-data-science) | Built a Random Forest classifier for 30-day hospital readmission risk on 587,801 synthetic electronic health record (EHR) training rows; scored ROC AUC 0.858 on the final held-out test, holding from 0.901 on the dev-phase leaderboard, after comparing 9 algorithms. ROC AUC is a classifier ranking score where 1.0 is perfect. | Python, Scikit-learn |
| [**Trait-Based Prediction of Animal Taxa**](https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/data-science/data-mining-final-project) | Used SHAP (SHapley Additive exPlanations), a machine-learning model-explainability technique, to identify evolutionary traits predicting animal taxonomy across 1,087 families | Python, SHAP |
| [**Data Visualization Portfolio**](https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/r-analytics/data-visualization-portfolio) | Built statistical visualizations across wildlife ecology, occupational safety, and housing economics using ggplot2, including alluvial diagrams and faceted area plots | R, ggplot2 |
| [**Multi-Label Emotion Classification**](https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/deep-learning/emotion-classification-info557) | Built a 5-seed ensemble of 1D convolutional neural networks (Conv1D / CNN) for 14-class GoEmotions text classification; placed 8th/15 on test set with an F1-score of 0.672 (a balanced precision/recall metric where 1.0 is perfect) and the 3rd-tightest dev-to-test gap on the leaderboard | Python, Keras, Hugging Face |
| [**AI4HC Capstone: Rural Health Kiosk Showcase Poster**](https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/capstone/ai4hc-info698) | Team capstone at the University of Arizona AI Core, AI for Healthcare program (AI4HC), building the Rural Health Kiosk, an AI-powered healthcare access system for underserved rural communities. Designed the team's iShowcase poster (HTML/CSS, light/dark variants) and built a Python print-export pipeline; [view live](https://matthewqilanthompson.github.io/Data-Science-Portfolio/projects/capstone/ai4hc-info698/index_v1.html) | HTML, CSS, Python |

---

## Software & Automation

Beyond analytics, I build and ship software:

| Project | What it is | Tech |
| ------- | ---------- | ---- |
| [**AI Grammar Bot**](https://github.com/matthewqilanthompson/ai-grammar-bot) | A production Discord bot that gives context-aware grammar feedback via the OpenAI API, with cost-monitored AI usage, MongoDB persistence (JSON fallback), per-user rate limiting, sensitive-info filtering, and 98 passing tests. Re-architected from Python to Node.js. | Node.js, discord.js, MongoDB, OpenAI, Jest |

---

## Technical Skills

| Category             | Tools & Applications                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **SQL & Databases**  | SQL (multi-table joins, aggregations, CTEs, correlated subqueries, temporal analysis) • MySQL • 3NF schema design (1,171 patients, 53K encounters) • ETL • MongoDB (NoSQL) |
| **Data Quality**     | Data validation & reconciliation • integrity checks (orphan-record detection) • data-leakage detection • cross-validation of measurement methods |
| **Languages**        | SQL • Python (pandas, NumPy, scikit-learn) • R (tidyverse) • JavaScript / Node.js                                                            |
| **Reporting & Visualization** | Excel (lookups, pivot tables) • Tableau (coursework) • ggplot2 (advanced plots, alluvial diagrams) • Matplotlib • analytical report writing |
| **Statistics**       | Linear regression • ANOVA • hypothesis testing • experimental design • repeatability analysis                                                |
| **Machine Learning** | Scikit-learn (classification, model comparison) • Random Forest (readmission prediction, ROC AUC 0.858 on held-out test, 0.901 on dev) • SHAP / SHapley Additive exPlanations (model explainability) • NLP / transformer fine-tuning (RoBERTa) |
| **Development**      | Git • Docker • Jupyter • RMarkdown / Quarto (reproducible research, automated reporting)                                                     |
| **Spatial / GIS**    | ArcGIS Pro • ArcGIS Online • ArcGIS StoryMaps • spatial analysis (coral reef & biodiversity mapping)                                        |

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![ggplot2](https://img.shields.io/badge/ggplot2-276DC3?style=flat-square&logo=r&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

---

## What I'm Looking For

Open to data work where domain knowledge and analytics overlap.

**Domain interests**: Life sciences, healthcare, environmental & ecological data, spatial/GIS, and climate & conservation, though I'm equally at home learning a new domain from scratch.

**What I bring**:

- **Data-integrity instinct**: I check before I trust, cleaning, validating, and reconciling data so the results hold up. On one project I caught a hidden leakage error inflating my model and re-validated until it held.
- **Technical breadth**: SQL, R, and Python across the data lifecycle, covering database design, statistics, ML, and visualization
- **Research instinct**: Biology background gives me a strong base for hypothesis-driven analysis in unfamiliar domains
- **Proven results**: 3NF database design over 53K patient encounters, an ML model at ROC AUC 0.858 on a held-out test set (0.901 on dev), and statistical analyses spanning wildlife ecology to housing economics

---

## Connect

<p align="center">
  <a href="https://www.linkedin.com/in/matthewqilanthompson/">
    <img src="https://img.shields.io/badge/LinkedIn-View%20Experience-0077B5?style=for-the-badge&logo=linkedin" alt="LinkedIn" />
  </a>
  <a href="mailto:matthewqilanthompson.work@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact%20Me-D14836?style=for-the-badge&logo=gmail" alt="Email" />
  </a>
  <a href="https://github.com/matthewqilanthompson/Data-Science-Portfolio">
    <img src="https://img.shields.io/badge/Portfolio-View%20Projects-181717?style=for-the-badge&logo=github" alt="Portfolio" />
  </a>
</p>
