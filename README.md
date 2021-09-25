### Simple-Movie-Recommender
![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![html](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![python](https://img.shields.io/badge/Python-0078D4?style=flat-square&logo=python&logoColor=white)
![numpy](https://img.shields.io/badge/Numpy-777BB4?style=flat-square&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=flat-square&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit_learn-0078D4?style=flat-square&logo=scikit-learn&logoColor=white)
![flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=flat-square&logo=visual%20studio%20code&logoColor=white)

#### app.py
- Import `CountVectorizer()`, `cosine_similarity()` from `sklearn` and `pandas` for reading dataset.
- Read the preprocessed dataset `movies_final.csv`
- Create objects for `CountVectorizer()` and use `fit_transform()` in `data['combined']` column.
- Define a function `recommend_movie()` which takes movie name as parameter and return list of recommended movies
- Import `Flask()`, `render_template()`, `request` from `flask` and `recommend_movie()` from `recommend.py`.
- Create app object from `Flask()` and create routes `home` and `predict`
- Define a function `home()` to render the homepage of the web app 
- Define function `predict()` to get movie name input from the user by html form and predict recommend movies using `recommend_movie()` and display the output as a unordered list.

#### Prediction with Correct Movie Name 👇
<img src="images/out1.gif" alt="Prediction with Correct Movie Name">

#### Prediction with Wrong Movie Name 👇
<img src="images/out2.gif" alt="Prediction with Wrong Movie Name">
