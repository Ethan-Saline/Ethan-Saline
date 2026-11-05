topics = ["Linear Regression", "Logistic Regression", "Holts Winters", "ARIMA",
          "Decision Tree", "Random Forest", "XGBoost", "Neural Networks",
          "CNNs", "RNNs", "Transformers", "Agents"]

out = ['---', 'title: "Models & Theory"', '---', '']
for t in topics:
    out += [
        f"# {t}", "",
        "::::: {.panel-tabset}", "",
        "## Overview", "", "Overview text.", "",
        "## Mathematical Model", "", "Math text.", "",
        "## Application", "",
        "::: {.panel-tabset}", "",
        "### Python", "", "Python text.", "",
        "### R", "", "R text.", "",
        ":::", "",
        ":::::", "",
    ]

with open("C:/Users/ethan/Documents/Projects/prof/Ethan-Saline/models/index.qmd", "w", encoding="utf-8") as f:
    f.write("\n".join(out))