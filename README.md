# Exam Bank

A centralized platform for storing, managing, and sharing past exam questions and answers. Easily organize question banks for different subjects and access them anytime.

---

## Features

- **Centralized Question Repository:** Store exams, past questions, and solutions.
- **Categorization:** Organize questions by subjects, topics, or difficulty.
- **Search Functionality:** Quickly find questions using keywords.
- **User-Friendly Interface:** Simple and intuitive navigation.
- **Contribution:** Allow users to add and modify questions (if enabled).

---

## Screenshots

> _Replace the image paths below with your actual screenshots stored in the `/screenshots` folder of your repository._

### Dashboard

![Dashboard Screenshot](screenshots/dashboard.png)

### Question View

![Question View Screenshot](screenshots/question-view.png)

---

## Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

---

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/prazim-projects/exam-bank.git
    cd exam-bank
    ```

2. **Set up the virtual environment with Pipenv:**

    ```bash
    pip install pipenv           # Install pipenv if you don't have it
    pipenv install               # Install dependencies as defined in Pipfile
    pipenv shell                 # Activate the virtual environment
    ```

    > _If you encounter issues, ensure `pipenv` is added to your PATH and you are using a compatible Python version._

3. **Configure environment variables:**

    - Copy the `.env.example` (if exists) to `.env` and update values as needed:

      ```bash
      cp .env.example .env
      ```

4. **Run database migrations** (if required by the project):

    ```bash
    # Example for Django
    python manage.py migrate
    ```

5. **Start the server:**

    ```bash
    # Example for Django
    python manage.py runserver
    ```

6. **Access the application:**

    Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Usage

- Browse, search, and filter questions.
- Add new exams or questions (if you have permission).
- Download or print question sets for offline use.

---

## Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For feedback or support, open an [issue](https://github.com/prazim-projects/exam-bank/issues) or contact the maintainer.
