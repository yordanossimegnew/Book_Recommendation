# Book Recommender System Using Clustering and Collaborative Filtering

This repository contains a **Book Recommender System** built using **Collaborative Filtering** and **Clustering** techniques. The project focuses on recommending books based on user ratings and provides an intuitive **Streamlit** web interface to display recommendations along with book covers.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Results](#results)
- [Future Enhancements](#future-enhancements)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Project Overview
This project implements a **Book Recommendation System** using collaborative filtering to recommend books to users based on their ratings. The system clusters similar users and books to generate suggestions for new books users may like. The final model is served as a web application using **Streamlit**, which allows users to select a book and receive recommendations.

## Dataset
The system uses the following datasets from the **Book-Crossing dataset**:
- **Books Dataset**: Contains book details (title, author, publication year, publisher, and cover image URL).
- **Users Dataset**: Contains demographic data about users.
- **Ratings Dataset**: Contains the ratings given by users to books.

The datasets were pre-processed to select relevant features, filter active users (who rated more than 200 books), and filter books with more than 50 ratings.

## Features
- **Collaborative Filtering**: Finds similar books based on user ratings.
- **Clustering**: Groups books and users based on rating patterns using Knearest Neighbours Algorithms.
- **Book Covers**: Displays book cover images alongside recommendations using URLs from the dataset.
- **Interactive Web App**: Uses **Streamlit** to let users select a book and get recommendations in real-time.

## Technologies Used
- **Python**: Core language for the project.
- **Pandas & NumPy**: For data manipulation and analysis.
- **SciPy & Scikit-learn**: For implementing clustering and collaborative filtering.
- **Streamlit**: For building the interactive web application.
- **Pickle**: For saving the trained models and pre-processed data(Serialization Task).
- **Matplotlib & Seaborn**: For visualizing the data.
- **IPython Kernel**: For running Jupyter Notebook.

## Installation
### Requirements
Make sure you have **Python 3.x** installed on your system. Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

### Running the Project
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/book-recommender-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd book-recommender-system
    ```
3. To run the recommender system:
    ```bash
    streamlit run app.py
    ```

This will start a local web server, and the Streamlit app can be accessed in your browser.

## Usage
1. Open the **Streamlit** web app.
2. Select a book from the dropdown menu.
3. Click **Show Recommendation** to view book recommendations along with their cover images.

## Project Structure
```
.
├── data
│   ├── raw_data
│   │   ├── BX-Books.csv
│   │   ├── BX-Users.csv
│   │   └── BX-Book-Ratings.csv
│   └── processed_data
│       ├── final_rating.pkl
│       ├── book_pivot.pkl
│       └── books_name.pkl
├── models
│   └── model.pkl
├── notebooks
│   └── book_recommender.ipynb
├── app.py
├── requirements.txt
└── README.md
```

- **data/raw_data**: Contains the original dataset files.
- **data/processed_data**: Contains the pre-processed datasets used in the model.
- **models**: Contains the saved machine learning model.
- **notebooks**: Jupyter notebooks for experimentation.
- **app.py**: Streamlit app file.
- **requirements.txt**: List of dependencies.

## How It Works
1. **Data Preprocessing**:
   - Filters active users and frequently rated books.
   - Merges user ratings with book information.
   - Creates a pivot table of book titles and user ratings.

2. **Collaborative Filtering**:
   - A **NearestNeighbors** model is used to find similar books.
   - The model is trained using the book-user rating matrix.

3. **Streamlit Web App**:
   - Users can select a book from the dropdown.
   - Upon selection, the app fetches and displays 5 similar books along with their cover images.

## Results
The recommender system provides accurate and relevant book recommendations based on user-selected books. The recommendations are visually enhanced with book cover images to improve the user experience.

## Future Enhancements
- **Content-Based Filtering**: Incorporate book genres, descriptions, and metadata for content-based recommendations.
- **User Profile Integration**: Allow users to log in and get personalized recommendations.
- **Improved UI**: Enhance the Streamlit interface with more interactive elements.
