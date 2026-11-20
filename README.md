<p align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/header-still.png">
    <img src="assets/header.gif" width="800" alt="Pixel art: a person in a lab coat signs HELLO in American Sign Language while a grasshopper hops through a field; each landing sends a data point to a chart on a laptop">
  </picture>
</p>

# Hi, I'm Matthew Thompson

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matthewqilanthompson/)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:matthewqilanthompson.work@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-181717?style=flat&logo=github&logoColor=white)](https://matthewqilanthompson.github.io/Data-Science-Portfolio/)

## Data Analyst · M.S. Data Science, B.S. Biology · SQL · Python · R · Research & health data

I started in biology research. During internships at Oklahoma State University (NSF ON-RaMP) and Maryland Sea Grant (NSF REU), I found that I enjoyed the data side most, so I went on to an M.S. in Data Science at the University of Arizona (May 2026).

I'm looking for data analyst, research data, data quality, health data and biology research roles where I can clean and organize data so others can use it. On one project an early model came back with a perfect score; instead of taking the win I went looking for the mistake, found leaked answer data, and re-validated until the number was real.

---

## <img src="assets/icons/education.png" width="32" height="32" alt=""> Education

| Degree                | Institution                                  | Status                 |
| --------------------- | -------------------------------------------- | ---------------------- |
| **M.S. Data Science** | University of Arizona (Online)               | Completed, May 2026   |
| **B.S. Biology**      | Gallaudet University *(Minor: Data Science)* | Completed, May 2023   |

---

## <img src="assets/icons/research.png" width="32" height="32" alt=""> Research Experience

| Role | Organization | Focus |
| ---- | ------------ | ----- |
| Post-Baccalaureate Research Intern | Oklahoma State University, National Science Foundation (NSF) ON-RaMP postbaccalaureate research training program | 1 year of full-time research: cleaned and validated 174 raw spectral files in R, built statistical models in R (regression, analysis of variance, repeatability) on grasshopper coloration & behavior, and wrote a Python automation script; presented a poster at the 2024 Society for Integrative and Comparative Biology (SICB) conference; co-author of a manuscript under peer review |
| Summer Research Intern, NSF Research Experiences for Undergraduates (REU) | Maryland Sea Grant | Selected from 400+ applicants; processed and counted 63 sample tubes of marine microbes from 4 m to 2,369 m deep, analyzed in R & Excel; extended into an Honors thesis · [poster and write-up](https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/research/reu-marine-snow) |

*Full work history on [LinkedIn](https://www.linkedin.com/in/matthewqilanthompson/).*

---

## <img src="assets/icons/projects.png" width="32" height="32" alt=""> Health & Biology Data Projects

<table>
<tr>
<td width="50%" valign="top">
<img src="assets/projects/readmission.png" width="32" height="32" align="left" alt="">
<a href="https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/data-science/foundation-of-data-science"><b>Healthcare Readmission Prediction</b></a><br>
<sub>ROC AUC 0.858 on held-out test · 587,801 synthetic EHR training rows · data leak caught</sub>
<p><code>Python</code> <code>Scikit-learn</code></p>
<details><summary>Details</summary>
<p>Built a Random Forest classifier for 30-day hospital readmission risk on 587,801 synthetic electronic health record (EHR) training rows, after comparing 9 algorithms. An early version scored a perfect 1.0; I traced it to a feature built from the target column, removed it and re-validated. Final score: ROC AUC 0.858 on the held-out test (0.901 in the dev phase). ROC AUC is a ranking score where 1.0 is perfect.</p>
</details>
</td>
<td width="50%" valign="top">
<img src="assets/projects/sql.png" width="32" height="32" align="left" alt="">
<a href="https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/database-systems/sql-nosql-databases-info579"><b>Healthcare Analytics with SQL</b></a><br>
<sub>3NF schema · 1,171 patients · 53,346 encounters · 6 analytical reports</sub>
<p><code>MySQL</code> <code>SQL</code> <code>Python</code></p>
<details><summary>Details</summary>
<p>Designed an 8-table third normal form (3NF) database for 1,171 patients and 53,346 encounters (~65MB synthetic Synthea EHR data, built from 6 source files), then wrote 6 documented analytical reports against 5 business objectives (profitability, clinical quality, provider utilization, readmission reduction, and expansion) using multi-table joins, CTEs, correlated subqueries, and temporal analysis. On the synthetic data, the reports surfaced a provider workload imbalance (busiest handled 3,000+ encounters vs. under 2,000 for peers). End-to-end reproducible via Docker.</p>
</details>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/icons/research.png" width="32" height="32" align="left" alt="">
<a href="https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/research/reu-marine-snow"><b>Microbial Abundance on Marine Snow (NSF REU)</b></a><br>
<sub>63 sample tubes · 4 m to 2,369 m · poster</sub>
<p><code>R</code> <code>Excel</code> <code>Microscopy</code></p>
<details><summary>Details</summary>
<p>Processed and counted stored samples from a 2019 East Pacific Rise research cruise with DAPI staining and epifluorescence microscopy, and analyzed the counts in R and Excel. Found no correlation between particle size and abundance, and flagged deep-ocean measurements that did not match a published study (Bergauer et al. 2018), naming possible reagent contamination as one explanation.</p>
</details>
</td>
<td width="50%" valign="top">
<img src="assets/projects/taxa.png" width="32" height="32" align="left" alt="">
<a href="https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/data-science/data-mining-final-project"><b>Trait-Based Prediction of Animal Taxa</b></a><br>
<sub>SHAP explainability · 1,087 families · 84 phylum-level rate estimates</sub>
<p><code>Python</code> <code>SHAP</code></p>
<details><summary>Details</summary>
<p>Compared two encodings of animal traits (presence/absence for 1,087 families vs. 84 phylum-level evolutionary rate estimates) for predicting 5 superphyla, and used SHAP (SHapley Additive exPlanations) to see which traits drove each model. The rate data gave the best macro F1 (0.31 vs. 0.13), a limited signal on a 28-row test set.</p>
</details>
</td>
</tr>
</table>

### Methods projects

<table>
<tr>
<td width="50%" valign="top">
<img src="assets/projects/emotion.png" width="32" height="32" align="left" alt="">
<a href="https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/deep-learning/emotion-classification-info557"><b>Multi-Label Emotion Classification</b></a><br>
<sub>5-seed Conv1D ensemble · 14 classes · test F1 0.672</sub>
<p><code>Python</code> <code>Keras</code> <code>Hugging Face</code></p>
<details><summary>Details</summary>
<p>Built a 5-seed ensemble of 1D convolutional neural networks (Conv1D / CNN) for 14-class GoEmotions text classification; scored an F1 of 0.672 on the test set (a balanced precision/recall metric where 1.0 is perfect), against 0.65 when the saved model was re-scored on dev data. A follow-up study after grading showed RoBERTa fine-tuning reached about 0.83 dev F1.</p>
</details>
</td>
<td width="50%" valign="top">
<img src="assets/projects/viz.png" width="32" height="32" align="left" alt="">
<a href="https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/r-analytics/data-visualization-portfolio"><b>Data Visualization Portfolio</b></a><br>
<sub>Wildlife ecology · occupational safety · housing economics</sub>
<p><code>R</code> <code>ggplot2</code></p>
<details><summary>Details</summary>
<p>Built statistical visualizations across wildlife ecology, occupational safety, and housing economics using ggplot2, including alluvial diagrams and faceted area plots</p>
</details>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/projects/kiosk.png" width="32" height="32" align="left" alt="">
<a href="https://github.com/matthewqilanthompson/Data-Science-Portfolio/tree/master/projects/capstone/ai4hc-info698"><b>AI4HC Capstone: Rural Health Kiosk Showcase Poster</b></a><br>
<sub>Team capstone · iShowcase poster (light/dark) · Python print-export pipeline</sub>
<p><code>HTML</code> <code>CSS</code> <code>Python</code></p>
<details><summary>Details</summary>
<p>Team capstone at the University of Arizona AI Core, AI for Healthcare program (AI4HC), building the Rural Health Kiosk, an AI-powered healthcare access system for underserved rural communities. Designed the team's iShowcase poster (HTML/CSS, light/dark variants) and built a Python print-export pipeline; <a href="https://matthewqilanthompson.github.io/Data-Science-Portfolio/projects/capstone/ai4hc-info698/index_v1.html">view live</a></p>
</details>
</td>
<td width="50%" valign="top">
<img src="assets/projects/bot.png" width="32" height="32" align="left" alt="">
<a href="https://github.com/matthewqilanthompson/ai-grammar-bot"><b>AI Grammar Bot</b></a> <sub>(finished project, archived)</sub><br>
<sub>Discord bot · OpenAI API · 98 passing tests</sub>
<p><code>Node.js</code> <code>discord.js</code> <code>OpenAI</code> <code>Jest</code></p>
<details><summary>Details</summary>
<p>A Discord bot that gives context-aware grammar feedback via the OpenAI API, with cost-monitored AI usage, MongoDB persistence (JSON fallback), per-user rate limiting, sensitive-info filtering, and 98 passing tests. Re-architected from Python to Node.js.</p>
</details>
</td>
</tr>
</table>

---

## <img src="assets/icons/presentations.png" width="32" height="32" alt=""> Presentations

- **2024 SICB Conference:** poster on temperature and developmental-environment effects on grasshopper coloration and behavior
- **2023 Esri Federal GIS Conference:** poster on ocean temperature and coral reefs · **2022 NGA GeoSpectrum Conference:** StoryMap on climate change and biodiversity

---

## <img src="assets/icons/skills.png" width="32" height="32" alt=""> Technical Skills

<details>
<summary><b>Full skills table</b></summary>

| Category             | Tools & Applications                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **SQL & Databases**  | SQL (multi-table joins, aggregations, CTEs, correlated subqueries, temporal analysis) • MySQL • 3NF schema design (1,171 patients, 53K encounters) • ETL |
| **Data Quality**     | Data validation & reconciliation • missing-link checks • data-leakage detection • cross-validation of measurement methods |
| **Languages**        | SQL • Python (pandas, NumPy, scikit-learn) • R (tidyverse) • JavaScript / Node.js                                                            |
| **Reporting & Visualization** | Excel (research use) • Tableau (coursework) • ggplot2 (advanced plots, alluvial diagrams) • Matplotlib • analytical report writing |
| **Statistics**       | Linear regression • ANOVA • hypothesis testing • experimental design • repeatability analysis                                                |
| **Machine Learning** | Scikit-learn (classification, model comparison) • Random Forest (readmission prediction, ROC AUC 0.858 on held-out test, 0.901 on dev) • SHAP / SHapley Additive exPlanations (model explainability) • NLP / transformer fine-tuning (RoBERTa) |
| **Lab & Research**   | Spectral data processing in R (`pavo`) • DAPI staining and epifluorescence microscopy • scientific posters |
| **Development**      | Git • Docker • Jupyter • RMarkdown / Quarto (reproducible research, automated reporting)                                                     |

</details>

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

## <img src="assets/icons/looking.png" width="32" height="32" alt=""> What I'm Looking For

Data analyst, research data, data quality, health data and biology research roles.

**What I bring**:

- **Data integrity**: cleaning, validating, and reconciling data before analysis. On one project I caught a leakage error inflating my model and re-validated until it held.
- **Biology + data**: a year of full-time research at Oklahoma State University (NSF ON-RaMP) and a summer NSF REU internship, so I understand where research data comes from and how it goes wrong
- **Technical breadth**: SQL, R, and Python across the data lifecycle, covering database design, statistics, ML, and visualization
- **Examples**: 3NF database design over 53K synthetic patient encounters, an ML model at ROC AUC 0.858 on a held-out test set (0.901 on dev), and 174 spectral files cleaned and validated in R

---

## <img src="assets/icons/connect.png" width="32" height="32" alt=""> Connect

<p align="center">
  <a href="https://www.linkedin.com/in/matthewqilanthompson/"><b>LinkedIn</b></a> &nbsp;·&nbsp;
  <a href="mailto:matthewqilanthompson.work@gmail.com"><b>Email</b></a> &nbsp;·&nbsp;
  <a href="https://matthewqilanthompson.github.io/Data-Science-Portfolio/"><b>Portfolio</b></a>
</p>
