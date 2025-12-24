# API Test Base

Framework for automated REST API testing with comprehensive endpoint coverage and Allure reporting.

## Project Structure

```
api-test-base/
├── tests/
│   ├── endpoints/        # Endpoint helper classes
│   ├── tests_apartment/  # Apartment API tests
│   ├── tests_user/       # User API tests
│   ├── auth_tools.py     # Authentication utilities
│   ├── conftest.py       # Pytest fixtures
│   └── test_root.py      # Root endpoint tests
├── test_data/            # Test data and parameters
├── scripts/              # Utility scripts
├── .github/workflows/    # CI/CD configuration
├── requirements.txt      # Dependencies
├── pytest.ini           # Pytest configuration
└── .env                  # Environment variables
```

## Features

- **Modular architecture**: separate endpoint classes with inheritance
- **Parameterized tests**: using pytest.mark.parametrize for data-driven testing
- **Allure reporting**: detailed test reports with steps and attachments
- **Automatic cleanup**: fixtures for creating/deleting test data
- **Field validation**: comprehensive data type and value checking
- **Error handling**: testing negative scenarios and edge cases
- **Authentication**: token-based auth with admin/user roles

## Tested Endpoints

### Apartments
- Create apartments with validation
- Retrieve apartment list with pagination
- Get apartment by ID and unit_id
- Update apartment data (partial/full)
- Delete apartments (single/bulk)
- Filter apartments by multiple criteria
- Upload apartment floor plans

### Users  
- User registration with validation
- Authentication and token management
- Get user profile (me endpoint)
- Update password with security checks
- Delete users with proper authorization
- Retrieve all users (admin only)
- Retrieve user by ID

### Root
- Health check endpoint
- API status verification

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create `.env` file with required variables:

```env
BASE_URL=http://your-api-url/
TEST_USERNAME=test_user
TEST_PASS=test_password
ADMIN_USERNAME=admin_user
ADMIN_PASSWORD=admin_password
```

## Running Tests

```bash
# All tests
pytest

# Specific test categories
pytest -m smoke            # Smoke tests only
pytest -m positive          # Positive scenarios only
pytest -m negative          # Negative scenarios only

# Specific modules
pytest tests/tests_apartment/    # Apartment tests
pytest tests/tests_user/         # User tests

# With Allure reporting
pytest --alluredir=allure-results
allure serve allure-results

# Run specific test file
pytest tests/tests_apartment/test_create_apartment.py
```

## Architecture

### Base Endpoint Class
All endpoint classes inherit from `Endpoint` base class providing:
- HTTP client setup (requests library)
- Authorization header management
- Response validation methods
- Status code checking
- Field type and value validation
- Error message verification
- Allure step decorators

### Test Organization
- **Endpoint classes**: Handle API interactions and validations
- **Test files**: Contain pytest test functions with parametrization
- **Test data**: Centralized test parameters and expected values
- **Fixtures**: Setup and teardown for test isolation

### Key Components
- `auth_tools.py`: Token generation and management
- `conftest.py`: Shared fixtures and test configuration
- `test_data/`: Parameterized test data and validation rules
- `endpoints/`: API interaction classes with validation methods

## Technologies

- **pytest** - testing framework with fixtures and parametrization
- **requests** - HTTP client for API calls
- **allure-pytest** - test reporting and visualization
- **faker** - test data generation
- **python-dotenv** - environment variables management
- **flake8** - code linting and style checking

## CI/CD

GitHub Actions workflow for:
- Code linting with flake8
- Automated test execution
- Allure report generation