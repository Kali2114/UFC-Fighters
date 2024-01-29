# UFC Fighters Application

Welcome to the UFC Fighters Application! This Django web application allows you to manage information about UFC fighters, their comments, and fighting styles.

## Features

- View a list of UFC fighters.
- Add, edit, and delete fighters.
- Leave comments on fighters.
- Track fighters' fighting styles and achievements.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ufc-fighters.git
Navigate to the project directory:

```
Copy code
cd ufc-fighters
```

Create a virtual environment:

```
Copy code
python -m venv env
```
Activate the virtual environment:

On Windows:

```
Copy code
.\env\Scripts\activate
```
On macOS/Linux:
```
Copy code
source env/bin/activate
Install dependencies:
```
```
Copy code
pip install -r requirements.txt
```
Apply database migrations:

```
Copy code
python manage.py migrate
```
Run the development server:

```
Copy code
python manage.py runserver
Access the application at http://127.0.0.1:8000/.
```
```
Login: admin<br>
Password: admin
```

## Usage
Navigate to the Fighters section to view, add, edit, or delete fighters.
Explore the Comments section to leave comments on your favorite fighters.
Check out the Fighting Styles to see the diverse martial arts styles covered.
Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.