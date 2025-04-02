# Library Management System

This project is a **Library Management System** built using Django. It provides a platform to manage library operations such as book inventory, user management, and borrowing/returning books.

## Features

- User authentication and authorization.
- Add, update, and delete books.
- Borrow and return books.
- Track borrowing history.
- Admin dashboard for managing the library.

## Installation

1. Clone the repository:
  ```bash
  git clone <repository-url>
  cd library_management
  ```

2. Create a virtual environment and activate it:
  ```bash
  python -m venv django-env
  source django-env/bin/activate  # On Windows: django-env\Scripts\activate
  ```

3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. Apply migrations:
  ```bash
  python manage.py migrate
  ```

5. Run the development server:
  ```bash
  python manage.py runserver
  ```

6. Access the application at `http://127.0.0.1:8000`.

## Usage

- Register as a user or log in as an admin.
- Admins can manage books and users.
- Users can browse books, borrow, and return them.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Django framework.
- Inspired by library management needs.
