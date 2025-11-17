# API Test Base

Framework for automated REST API testing with support for both synchronous and asynchronous requests.

## Project Structure

```
api-test-base/
├── tests_async/          # Asynchronous tests
├── tests_sync/           # Synchronous tests  
├── test_data/            # Test data
├── requirements.txt      # Dependencies
├── pytest.ini            # Pytest configuration
└── .env                  # Environment variables
```

## Features

- **Dual support**: synchronous and asynchronous HTTP requests
- **Modular architecture**: separate classes for each endpoint
- **Parameterized tests**: using pytest.mark.parametrize
- **Automatic cleanup**: fixtures for creating/deleting test data
- **Field validation**: checking data types and values
- **Error handling**: testing negative scenarios

## Tested Endpoints

### Apartments
- Create apartments
- Retrieve apartment list
- Get apartment by ID
- Update apartment data
- Delete apartments
- Filter apartments
- Upload apartment plans

### Users  
- User registration
- Authentication
- Get profile
- Update password
- Delete users

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create `.env` file with variables:

```env
BASE_URL=
TEST_USERNAME=
TEST_PASS=
ADMIN_USERNAME=
ADMIN_PASSWORD=
```

## Running Tests

```bash
# All tests
pytest

# Positive tests only
pytest -m positive

# Negative tests only  
pytest -m negative

# Asynchronous tests
pytest tests_async/

# Synchronous tests
pytest tests_sync/
```

## Architecture

Each endpoint is represented by a separate class inheriting from the base `Endpoint` class, which provides:

- HTTP client (httpx/requests)
- Authorization methods
- Response validation
- Status code checking
- Error handling

## Technologies

- **pytest** - testing framework
- **httpx** - asynchronous HTTP client
- **requests** - synchronous HTTP client
- **faker** - test data generation
- **python-dotenv** - environment variables management